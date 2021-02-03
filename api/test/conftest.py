import pytest
from pathlib import Path
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ser_api.database.db_init import get_db, Base
from ser_api.app import app
from ser_api.utils.config import config, CONFIG_ENV

@pytest.fixture()
def resource():
    """
    dummy one
    :return:
    """
    print("setup")
    yield "resource"
    print("teardown")


class Helpers:
    @staticmethod
    def client_setup():
        SQLALCHEMY_DATABASE_URL = config[CONFIG_ENV].db_url_string()
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
        def override_get_db():
            try:
                db = TestingSessionLocal()
                yield db
            finally:
                db.close()
        app.dependency_overrides[get_db] = override_get_db
        return TestClient(app),TestingSessionLocal()
    @staticmethod
    def purge_data():
        from ser_api.model.record_model import Record
        from ser_api.model.deleted_model import Deleted
        _ , session= Helpers.client_setup()
        session.query(Record).delete()
        session.query(Deleted).delete()
        session.commit()
        session.close()
    @staticmethod
    def purge_bucket():
        from ser_api.utils.gc_utils import get_gcs_client
        client = get_gcs_client()
        bucket = client.bucket(config[CONFIG_ENV].BUCKET_NAME)
        for blob in bucket.list_blobs():
            blob.delete()

@pytest.fixture
def helpers():
    return Helpers


@pytest.fixture()
def test_file_obj():
    return {'file': ('file_example_OOG_1MG.ogg', open(Path(Path(__file__).parent,"ressources","file_example_OOG_1MG.ogg"), 'rb'),"audio/ogg")}