from test.test_router.test_db import client
from src.utils.config import Config
from sqlalchemy.exc import IntegrityError

API_VERSION = Config.VERSION


def test_create_sentence():
    """ Test route sentence creation """
    params = {'sentence': "My name is Slim Shady 1"}

    response = client.post(f"/api/{API_VERSION}/create_sentence/", params=params)

    data_test = response.json()

    # Check post response
    assert data_test["sentence"] == params["sentence"]
    assert response.status_code == 200

    # Check sentence has been add to test db
    sentence_test = client.get(f"/api/{API_VERSION}/get_sentence/{data_test['id']}")
    assert sentence_test.json()["id"] == data_test["id"]

    # Check uniqueness constraint
    try:
        response = client.post(f"/api/{API_VERSION}/create_sentence/", params=params)
        assert 0  # fail test
    except IntegrityError:
        pass


def test_get_sentence_not_exists():
    """ Test route get single sentence - based on its uuid """
    response = client.get(f"/api/{API_VERSION}/get_sentence/100")
    assert response.status_code == 404


def test_get_all_sentences():
    """ Test route get all sentences """
    params = {'sentence': "My name is Slim Shady 2"}

    client.post(
        "/create_sentence/",
        params=params,
    )
    response = client.get(f"/api/{API_VERSION}/get_all_sentences")
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) != 0


def test_delete_sentence():
    """ Test route sentence deletion """
    params = {'sentence': "My name is Slim Shady 3"}

    sentence_test = client.post(
        f"/api/{API_VERSION}/create_sentence/",
        params=params,
    )
    sentence_test_json = sentence_test.json()
    sentence_test_id = sentence_test_json["id"]

    # Delete sentence and check returned status code
    delete_response = client.delete(f"/api/{API_VERSION}/delete_sentence/{sentence_test_id}")
    assert delete_response.status_code == 200

    # Check sentence has been delete from sentence table
    check_response = client.get("/get_sentence/{}".format(sentence_test_id))
    assert check_response.status_code == 404


def test_delete_sentence_not_exists():
    """ Test delete sentence request with fake uuid """
    delete_response = client.delete(f"/api/{API_VERSION}/detele_sentence/100")

    # Delete request should return 404 because sentence not exists
    assert delete_response.status_code == 404


def test_get_random_sentence():
    """ Test get random sentence """
    response = client.get(f"/api/{API_VERSION}/get_random_sentence/")

    assert response.status_code == 200
