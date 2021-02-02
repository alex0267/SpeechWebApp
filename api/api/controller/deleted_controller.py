from sqlalchemy.orm import Session
from datetime import datetime
from api.model import deleted_model


def get_deleted_record(db: Session, record_uuid: str):
    """
    Get record from database based on its record_id
    :param db: database session
    :param record_uuid: uuid identifying a record
    :return: deleted
    """
    return db.query(deleted_model.Deleted).filter(deleted_model.Deleted.uuid == record_uuid).first()


def get_all_deleted_records(db: Session):
    """
    Get all deleted records
    :param db: database session
    :return: list of all deleted records
    """
    return db.query(deleted_model.Deleted).all()


def add_deleted_record(db: Session, record_uuid: str):
    """
    Add deleted record to deleted table
    :param db: database session
    :param record_uuid: uuid identifying a record
    :return: deleted record
    """
    deleted_record = deleted_model.Deleted(
        uuid=record_uuid,
        timestamp=datetime.now()
    )

    db.add(deleted_record)
    db.commit()
    db.refresh(deleted_record)

    return deleted_record
