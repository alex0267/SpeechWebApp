import uuid
from sqlalchemy.orm import Session
from src.model import record_model
from datetime import datetime
from fastapi import UploadFile
from src.utils.config import config, CONFIG_ENV
from pathlib import Path

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


def add_record(db: Session, emotion: str, sentence_id: int, file: UploadFile):
    """
    Create a new record in database
    :param db: database session
    :param emotion: emotion name
    :param sentence_id: id of associated sentence
    :param file: record audio file as Uploadfile
    :return: record
    """

    #upload file
    import gcsfs
    my_uuid = str(uuid.uuid1())
    my_url = f"{config[CONFIG_ENV].BUCKET_NAME}/{my_uuid}{Path(file.filename).suffix}"
    my_complete_url = f"gs://{my_url}"
    fs = gcsfs.GCSFileSystem(project=config[CONFIG_ENV].PROJECT_ID,token=config[CONFIG_ENV].GOOGLE_APPLICATION_CREDENTIALS_PATH)

    with fs.open(my_url, 'ab') as f:
        f.write(file.file.read())
    db_record = record_model.Record(
                record_url=my_complete_url,
                emotion=emotion,
                timestamp=datetime.now(),
                uuid=my_uuid,
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

    from utils.gc_utils import get_gcs_client
    client = get_gcs_client()
    bucket = client.bucket(config[CONFIG_ENV].BUCKET_NAME)
    for blob in bucket.list_blobs(prefix='record_uuid'):
        blob.delete()

    if deleted_record == 0:
        return None
    else:
        db.commit()
        return True

