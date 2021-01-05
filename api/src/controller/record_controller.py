import uuid
from sqlalchemy.orm import Session
from src.model import record_model
from datetime import datetime


def get_record(db: Session, record_uuid: str):
    """
    Get single record from database based on its record_id
    :param db: database session
    :param record_uuid: uuid identifying a record
    :return: record
    """
    return db.query(record_model.Record).filter(record_model.Record.uuid == record_uuid).first()


def get_all_records(db: Session):
    """
    Get all records from database
    :param db: database session
    :return: list of records
    """
    return db.query(record_model.Record).all()


def add_record(db: Session, emotion: str, sentence_id: int, file: bytes):
    """
    Create a new record in database
    :param db: database session
    :param emotion: emotion name
    :param sentence_id: id of associated sentence
    :param file: record audio file as bytes
    :return: record
    """
    db_record = record_model.Record(
                record_url="http://fake_url",
                emotion=emotion,
                timestamp=datetime.now(),
                uuid=str(uuid.uuid1()),
                sentence_id=sentence_id,
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record


def delete_record(db: Session, record_uuid: str):
    """
    Delete a record base on its uuid
    :param db: database session
    :param record_uuid: uuid identifying a record
    :return: None if record not found, true if success
    """

    record_to_delete = db.query(record_model.Record).filter(record_model.Record.uuid == record_uuid)
    deleted_record = record_to_delete.delete()

    if deleted_record == 0:
        return None
    else:
        db.commit()
        return True

