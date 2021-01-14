from controller.record_controller import get_all_records
from model.record_model import Record
from model.sentence_model import Sentence
import datetime


def test_get_all_records(helpers):
    helpers.purge_data()
    _, session_db = helpers.client_setup()
    sentence_id=session_db.query(Sentence).first().id
    record = Record(record_url="url",emotion="sad",timestamp=datetime.datetime.now(),uuid="123",sentence_id=sentence_id)
    session_db.add(record)
    session_db.commit()
    res = get_all_records(session_db)
    session_db.close()
    assert len(res)==1