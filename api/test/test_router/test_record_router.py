from api.utils.config import Config
from api.model.sentence_model import Sentence

API_VERSION = Config.VERSION


def test_create_record(test_file_obj, helpers):
    """ Test route record creation """
    client_app, client_session = helpers.client_setup()
    sentence_id = client_session.query(Sentence).first().id
    params = {'sentence_id': sentence_id}
    client_session.close()

    response = client_app.post(
        f"/api/{API_VERSION}/create_record/happiness",
        files=test_file_obj,
        params=params
    )

    data_test = response.json()

    # Check post response
    assert data_test["emotion"] == "happiness"
    assert response.status_code == 200

    # Check record has been add to test db
    record_test = client_app.get(f"/api/{API_VERSION}/get_record/{data_test['uuid']}")
    assert record_test.json()["uuid"] == data_test["uuid"]


def test_get_record_not_exists(helpers):
    """ Test route get single record - based on its uuid """
    client_app, _ = helpers.client_setup()
    response = client_app.get(f"/api/{API_VERSION}/get_record/fake-uuid")
    assert response.status_code == 404


def test_get_all_records(test_file_obj, helpers):
    """ Test route get all records """
    client_app, client_session = helpers.client_setup()
    sentence_id = client_session.query(Sentence).first().id
    params = {'sentence_id': sentence_id}
    client_session.close()
    response = client_app.post(f"/api/{API_VERSION}/create_record/happiness", files=test_file_obj, params=params)
    response = client_app.get(f"/api/{API_VERSION}/get_all_records")
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) != 0


def test_delete_record(test_file_obj, helpers):
    """ Test route record deletion """
    client_app, client_session = helpers.client_setup()
    sentence_id = client_session.query(Sentence).first().id
    client_session.close()
    params = {'sentence_id': sentence_id}
    record_test = client_app.post(
        f"/api/{API_VERSION}/create_record/happiness",
        files=test_file_obj,
        params=params,
    )
    record_test_json = record_test.json()
    record_test_uuid = record_test_json["uuid"]

    # Delete record and check returned status code
    delete_response = client_app.delete(f"/api/{API_VERSION}/delete_record/{record_test_uuid}")
    assert delete_response.status_code == 200

    # Check record has been delete from record table
    check_response = client_app.get(f"/api/{API_VERSION}/get_record/{record_test_uuid}")
    assert check_response.status_code == 404

    # Check record has been added to delete-record table
    response = client_app.get(f"/api/{API_VERSION}/get_deleted/{record_test_uuid}")
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["uuid"] == record_test_uuid


def test_delete_record_not_exists(helpers):
    """ Test delete record request with fake uuid """
    client_app, _ = helpers.client_setup()
    delete_response = client_app.delete(f"/api/{API_VERSION}/detele_record/fake-uuid")

    # Delete request should return 404 because record not exists
    assert delete_response.status_code == 404
