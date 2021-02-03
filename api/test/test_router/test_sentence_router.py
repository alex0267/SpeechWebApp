from sqlalchemy.exc import IntegrityError
from ser_api.model.sentence_model import Sentence
from ser_api.utils.config import Config

API_VERSION = Config.VERSION


def test_create_sentence(helpers):
    """ Test route sentence creation """

    helpers.purge_data()
    client_app, client_session = helpers.client_setup()
    client_session.query(Sentence).filter(Sentence.sentence=="My name is Slim Shady 1").delete()
    client_session.commit()
    client_session.close()
    params = {'sentence': "My name is Slim Shady 1"}

    response = client_app.post(f"/api/{API_VERSION}/create_sentence/", params=params)

    data_test = response.json()

    # Check post response
    assert data_test["sentence"] == params["sentence"]
    assert response.status_code == 200

    # Check sentence has been add to test db
    sentence_test = client_app.get(f"/api/{API_VERSION}/get_sentence/{data_test['id']}")
    assert sentence_test.json()["id"] == data_test["id"]

    # Check uniqueness constraint
    try:
        response = client_app.post(f"/api/{API_VERSION}/create_sentence/", params=params)
        assert 0  # fail test
    except IntegrityError:
        pass


def test_get_sentence_not_exists(helpers):
    """ Test route get single sentence - based on its uuid """
    client_app, _ = helpers.client_setup()
    response = client_app.get(f"/api/{API_VERSION}/get_sentence/100")
    assert response.status_code == 404


def test_get_all_sentences(helpers):
    """ Test route get all sentences """
    client_app, _ = helpers.client_setup()
    params = {'sentence': "My name is Slim Shady 2"}

    client_app.post(
        "/create_sentence/",
        params=params,
    )
    response = client_app.get(f"/api/{API_VERSION}/get_all_sentences")
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) != 0


def test_delete_sentence(helpers):
    """ Test route sentence deletion """
    client_app, _ = helpers.client_setup()
    params = {'sentence': "My name is Slim Shady 3"}

    sentence_test = client_app.post(
        f"/api/{API_VERSION}/create_sentence/",
        params=params,
    )
    sentence_test_json = sentence_test.json()
    sentence_test_id = sentence_test_json["id"]

    # Delete sentence and check returned status code
    delete_response = client_app.delete(f"/api/{API_VERSION}/delete_sentence/{sentence_test_id}")
    assert delete_response.status_code == 200

    # Check sentence has been delete from sentence table
    check_response = client_app.get("/get_sentence/{}".format(sentence_test_id))
    assert check_response.status_code == 404


def test_delete_sentence_not_exists(helpers):
    """ Test delete sentence request with fake uuid """
    client_app, _ = helpers.client_setup()
    delete_response = client_app.delete(f"/api/{API_VERSION}/detele_sentence/100")

    # Delete request should return 404 because sentence not exists
    assert delete_response.status_code == 404


def test_get_random_sentence(helpers):
    """ Test get random sentence """
    client_app, _ = helpers.client_setup()
    response = client_app.get(f"/api/{API_VERSION}/get_random_sentence/")

    assert response.status_code == 200