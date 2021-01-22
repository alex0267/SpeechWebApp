from fastapi import APIRouter, HTTPException, Depends, UploadFile
from typing import List
from sqlalchemy.orm import Session
from src.schema import record_schema
from src.controller import record_controller, deleted_controller
from src.database.db_init import get_db
from src.utils.logging import logger
from fastapi import File


router = APIRouter()


@router.post("/create_record/{emotion}", response_model=record_schema.Record, tags=["record"])
async def create_record(emotion: str, sentence_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Create record route
    :param emotion: emotion name
    :param file: file as UploadFile
    :param db: database session
    """
    return record_controller.add_record(db, emotion, sentence_id, file)


@router.get("/get_record/{uuid}", response_model=record_schema.Record, tags=["record"])
async def get_record(uuid: str, db: Session = Depends(get_db)):
    """
    Get single record route
    :param uuid: uuid identifying a record
    :param db: database session
    """
    db_record = record_controller.get_record(db, uuid)
    if db_record is None:
        logger.error("Cannot find record {}  found in database".format(uuid))
        raise HTTPException(status_code=404, detail="record not found")
    return db_record


@router.get("/get_all_records", response_model=List[record_schema.Record], tags=["record"])
async def get_all_records(db: Session = Depends(get_db)):
    """
    Get all records route
    :param db: database session
    """
    all_db_record = record_controller.get_all_records(db)
    if all_db_record is None:
        logger.warn("Zero records found in database")
        raise HTTPException(status_code=404, detail="0 record found, empty table")
    return all_db_record


@router.delete("/delete_record/{uuid}", tags=["record"])
async def delete_record(uuid: str, db: Session = Depends(get_db)):
    """
    Delete record route
    :param uuid: uuid associate to a record
    :param db: database session
    """
    is_deleted = record_controller.delete_record(db, uuid)
    if is_deleted is None:
        logger.error("Fail to delete record {}, record doesn't exist".format(uuid))
        raise HTTPException(status_code=404, detail="Record {} doesn't exists in database".format(uuid))
    else:
        deleted_controller.add_deleted_record(db, uuid)
        logger.info("Successfully remove record {}, save deletion track in deleted-records table".format(uuid))
        return {"message": "Successfully delete record".format(uuid)}
