from test.test_router.test_db import client
from src.utils.config import Config

API_VERSION = Config.VERSION


def test_create_record():
    """ Test route record creation """
    files = {'file': ('test.txt', open('test/test_router/test.txt', 'rb'))}

    response = client.post(
        f"/api/{API_VERSION}/create_record/happiness",
        files=files
    )

    data_test = response.json()

    # Check post response
    assert data_test["emotion"] == "happiness"
    assert response.status_code == 200

    # Check record has been add to test db
    record_test = client.get(f"/api/{API_VERSION}/get_record/{data_test['uuid']}")
    assert record_test.json()["uuid"] == data_test["uuid"]


def test_get_record_not_exists():
    """ Test route get single record - based on its uuid """
    response = client.get(f"/api/{API_VERSION}/get_record/fake-uuid")
    assert response.status_code == 404


def test_get_all_records():
    """ Test route get all records """
    files = {'file': ('test.txt', open('test/test_router/test.txt', 'rb'))}

    client.post(
        "/create_record/happiness",
        files=files
    )
    response = client.get(f"/api/{API_VERSION}/get_all_records")
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) != 0


def test_delete_record():
    """ Test route record deletion """
    files = {'file': ('test.txt', open('test/test_router/test.txt', 'rb'))}

    record_test = client.post(f"/api/{API_VERSION}/create_record/happiness", files=files)
    record_test_json = record_test.json()
    record_test_uuid = record_test_json["uuid"]

    # Delete record and check returned status code
    delete_response = client.delete(f"/api/{API_VERSION}/delete_record/{record_test_uuid}")
    assert delete_response.status_code == 200

    # Check record has been delete from record table
    check_response = client.get("/get_record/{}".format(record_test_uuid))
    assert check_response.status_code == 404

    # Check record has been added to delete-record table
    response = client.get(f"/api/{API_VERSION}/get_deleted/{record_test_uuid}")
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["uuid"] == record_test_uuid


def test_delete_record_not_exists():
    """ Test delete record request with fake uuid """
    delete_response = client.delete(f"/api/{API_VERSION}/detele_record/fake-uuid")

    # Delete request should return 404 because record not exists
    assert delete_response.status_code == 404
