from src.controller.record_controller import get_all_records
from src.model.record_model import Record



def test_get_all_records(client_setup):
    _, session_db = client_setup
    record = Record(record_url="url",emotion="sad",timestamp=None,uuid="123")
    session_db.add(record)
    session_db.commit()
    res = get_all_records(session_db)
    assert len(res)==1