import pytest
from pathlib import Path
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_init import get_db, Base,db_url_string
from app import app

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
        SQLALCHEMY_DATABASE_URL = db_url_string()
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
        from model.record_model import Record
        from model.deleted_model import Deleted
        _ , session= Helpers.client_setup()
        session.query(Record).delete()
        session.query(Deleted).delete()
        session.commit()
        session.close()


@pytest.fixture
def helpers():
    return Helpers



@pytest.fixture()
def test_file_obj():
    return {'file': ('test.txt', open(Path(Path(__file__).parent,"ressources","test.txt"), 'rb'))}