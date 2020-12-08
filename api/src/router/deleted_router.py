from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schema import deleted_schema
from src.controller import deleted_controller
from src.database.db_init import get_db

router = APIRouter()


@router.get("/get_deleted/{uuid}", response_model=deleted_schema.Deleted, tags=["deleted"])
async def get_deleted_record(uuid: str, db: Session = Depends(get_db)):
    """
    Get deleted record from deleted table
    :param uuid: uuid associate to a record
    :param db: database session
    :return: deleted
    """
    db_record = deleted_controller.get_deleted_record(db, uuid)
    if db_record is None:
        raise HTTPException(status_code=404, detail="deleted record not found")
    return db_record


@router.get("/get_all_deleted", response_model=List[deleted_schema.Deleted], tags=["deleted"])
async def get_all_deleted_records(db: Session = Depends(get_db)):
    """
    Get all deleted records from deleted table
    :param db: database session
    :return: list of deleted
    """
    all_db_delete_requests = deleted_controller.get_all_deleted_records(db)
    if all_db_delete_requests is None:
        raise HTTPException(status_code=404, detail="0 deleted records found, empty table")
    return all_db_delete_requests
