import pytest
from pathlib import Path
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.db_init import get_db, Base
from src.app import app


@pytest.fixture()
def resource():
    print("setup")
    yield "resource"
    print("teardown")

@pytest.fixture(scope="module")
def client_setup():
    try:
        os.remove("test.db")
    except FileNotFoundError:
        pass
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
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


@pytest.fixture()
def test_file_obj():
    return {'file': ('test.txt', open(Path(Path(__file__).parent,"ressources","test.txt"), 'rb'))}