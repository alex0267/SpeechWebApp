from src.utils.config import Config
from test.test_router.test_db import client

API_VERSION = Config.VERSION


def test_get_deleted_not_exists():
    """ Test get deleted record that not exists"""
    response = client.get(f"/api/{API_VERSION}/get_deleted/a-fake-uuid")

    assert response.status_code == 404


def test_get_deleted():
    """ Test get deleted record that exists """

    # Create a new record
    files = {'file': ('test.txt', open('test/test_router/test.txt', 'rb'))}

    record_test = client.post(f"/api/{API_VERSION}/create_record/happiness", files=files)
    record_test_json = record_test.json()
    record_test_uuid = record_test_json["uuid"]

    # Delete previously created record
    client.delete(f"/api/{API_VERSION}/delete_record/{record_test_uuid}")

    # Check deleted record has been added to deleted table
    response = client.get(f"/api/{API_VERSION}/get_deleted/{record_test_uuid}")

    assert response.status_code == 200


def test_get_all_deleted():
    """Test get all deleted records"""
    response = client.get(f"/api/{API_VERSION}/get_all_deleted/")
    assert response.status_code == 200
