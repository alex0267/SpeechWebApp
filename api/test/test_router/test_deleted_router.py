from ser_api.utils.config import Config
from ser_api.model.sentence_model import Sentence
API_VERSION = Config.VERSION



def test_get_deleted_not_exists(helpers):
    """ Test get deleted record that not exists"""
    client_app, _ = helpers.client_setup()
    response = client_app.get(f"/api/{API_VERSION}/get_deleted/a-fake-uuid")

    assert response.status_code == 404


def test_get_deleted(test_file_obj,helpers):
    """ Test get deleted record that exists """
    client_app, client_session = helpers.client_setup()
    # Create a new record
    sentence_id=client_session.query(Sentence).first().id
    client_session.close()
    params = {'sentence_id': sentence_id}

    record_test = client_app.post(
        f"/api/{API_VERSION}/create_record/happiness",
        files=test_file_obj,
        params=params,
    )
    record_test_json = record_test.json()
    record_test_uuid = record_test_json["uuid"]

    captcha_response = "03AGdBq27wDU10_olSGG4Po6m7CPebDfCv_QK7mDi0y3UO3DhV15SxL-9K6-3GKH06NE4ZAxb2cWVozIdBTqNAO5apERY8jRueHt1-DhbhFcYt2LwQQ9i42xJ_5x0s_DCOdlVnycdln2fneOuzuhZDQNHvMJs71AETj2u9CGI18z-9rl7uXWnEWKii7ewgKzhHCerkWF-ataXTwA8gYw7pF-SOIbj89pZH2rb4VC6l8sTiviohgnEXzrRbOWKtVMwGBaabzx0SQ5wSj0ihSl_crMTWCZ3sAvfC8bDWiPkdu4GhxzwkTFrkGe_FtZrXSbSa67Fccp0fTCYUVL9v2RkBWq7Uvx9YzkUL3Xp0m9uoLOzyvh3JHw2gHxB5w8vvfNjCywTOD1LVMrxw6HATt6w74g9bezBcvLcwNg"

    # Delete previously created record
    client_app.delete(f"/api/{API_VERSION}/delete_record/{record_test_uuid}?captcha_response={captcha_response}")

    # Check deleted record has been added to deleted table
    response = client_app.get(f"/api/{API_VERSION}/get_deleted/{record_test_uuid}")

    assert response.status_code == 200


def test_get_all_deleted(helpers):
    """Test get all deleted records"""
    client_app, _ = helpers.client_setup()
    response = client_app.get(f"/api/{API_VERSION}/get_all_deleted/")
    assert response.status_code == 200
