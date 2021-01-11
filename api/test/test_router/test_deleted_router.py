from src.utils.config import Config

API_VERSION = Config.VERSION


def test_get_deleted_not_exists(client_setup):
    """ Test get deleted record that not exists"""
    client_app, _ = client_setup
    response = client_app.get(f"/api/{API_VERSION}/get_deleted/a-fake-uuid")

    assert response.status_code == 404


def test_get_deleted(test_file_obj,client_setup):
    """ Test get deleted record that exists """
    client_app, _ = client_setup
    # Create a new record
    params = {'sentence_id': 1}

    record_test = client_app.post(
        f"/api/{API_VERSION}/create_record/happiness",
        files=test_file_obj,
        params=params,
    )
    record_test_json = record_test.json()
    record_test_uuid = record_test_json["uuid"]

    # Delete previously created record
    client_app.delete(f"/api/{API_VERSION}/delete_record/{record_test_uuid}")

    # Check deleted record has been added to deleted table
    response = client_app.get(f"/api/{API_VERSION}/get_deleted/{record_test_uuid}")

    assert response.status_code == 200


def test_get_all_deleted(client_setup):
    """Test get all deleted records"""
    client_app, _ = client_setup
    response = client_app.get(f"/api/{API_VERSION}/get_all_deleted/")
    assert response.status_code == 200
