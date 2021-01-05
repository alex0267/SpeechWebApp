from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schema import sentence_schema
from src.controller import sentence_controller
from src.database.db_init import get_db
from src.utils.logging import logger


router = APIRouter()


@router.post("/create_sentence/", response_model=sentence_schema.Sentence, tags=["sentence"])
async def create_sentence(sentence: str, db: Session = Depends(get_db)):
    """
    Create sentence route
    :param sentence: sentence to record
    :param db: database session
    """
    return sentence_controller.add_sentence(db, sentence)


@router.get("/get_sentence/{id}", response_model=sentence_schema.Sentence, tags=["sentence"])
async def get_sentence(sentence_id: int, db: Session = Depends(get_db)):
    """
    Get single sentence route
    :param sentence_id: id identifying a sentence
    :param db: database session
    """
    db_sentence = sentence_controller.get_sentence(db, sentence_id)
    if db_sentence is None:
        logger.error("Cannot find sentence {} found in database".format(id))
        raise HTTPException(status_code=404, detail="sentence not found")
    return db_sentence


@router.get("/get_all_sentences", response_model=List[sentence_schema.Sentence], tags=["sentence"])
async def get_all_records(db: Session = Depends(get_db)):
    """
    Get all records route
    :param db: database session
    """
    all_db_sentences = sentence_controller.get_all_sentences(db)
    if all_db_sentences is None:
        logger.warn("Zero sentences found in database")
        raise HTTPException(status_code=404, detail="0 sentences found, empty table")
    return all_db_sentences


@router.delete("/delete_sentence/{id}", tags=["sentence"])
async def delete_record(sentence_id: str, db: Session = Depends(get_db)):
    """
    Delete sentence route
    :param sentence_id: id associate to a sentence
    :param db: database session
    """
    is_deleted = sentence_controller.delete_sentence(db, sentence_id)
    if is_deleted is None:
        logger.error("Fail to delete sentence {}, sentence doesn't exist".format(sentence_id))
        raise HTTPException(status_code=404, detail="Sentence {} doesn't exists in database".format(sentence_id))
    else:
        logger.info("Successfully remove sentence {}".format(sentence_id))
        return {"message": "Successfully sentence {}".format(sentence_id)}
