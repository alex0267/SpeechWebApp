from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from random import randint
from starlette.requests import Request
from starlette.responses import Response
from ser_api.schema import sentence_schema
from ser_api.controller import sentence_controller
from ser_api.database.db_init import get_db
from ser_api.utils.logging import logger
from ser_api.utils.auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/create_sentence/", dependencies=[Depends(JWTBearer())], response_model=sentence_schema.Sentence, tags=["sentence"])
async def create_sentence(sentence: str, db: Session = Depends(get_db)):
    """
    Create sentence route
    :param sentence: sentence to record
    :param db: database session
    """
    return sentence_controller.add_sentence(db, sentence)


@router.get("/get_sentence/{id}", dependencies=[Depends(JWTBearer())],  response_model=sentence_schema.Sentence, tags=["sentence"])
async def get_sentence(id: int, db: Session = Depends(get_db)):
    """
    Get single sentence route
    :param id: id identifying a sentence
    :param db: database session
    """
    db_sentence = sentence_controller.get_sentence(db, id)
    if db_sentence is None:
        logger.error("Cannot find sentence {} found in database".format(id))
        raise HTTPException(status_code=404, detail="sentence not found")
    return db_sentence


@router.get("/get_all_sentences", dependencies=[Depends(JWTBearer())],  response_model=List[sentence_schema.Sentence], tags=["sentence"])
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


@router.delete("/delete_sentence/{id}", dependencies=[Depends(JWTBearer())],  tags=["sentence"])
async def delete_record(id: str, db: Session = Depends(get_db)):
    """
    Delete sentence route
    :param id: id associate to a sentence
    :param db: database session
    """
    is_deleted = sentence_controller.delete_sentence(db, id)
    if is_deleted is None:
        logger.error("Fail to delete sentence {}, sentence doesn't exist".format(id))
        raise HTTPException(status_code=404, detail="Sentence {} doesn't exists in database".format(id))
    else:
        logger.info("Successfully remove sentence {}".format(id))
        return {"message": "Successfully sentence {}".format(id)}


@router.get("/get_random_sentence/", tags=["sentence"])
async def get_random_sentence(request: Request, db: Session = Depends(get_db)):
    """
    Get random sentence route
    :param db: database session
    """
    all_db_sentences = sentence_controller.get_all_sentences(db)
    rand_id = randint(0, len(all_db_sentences) - 1)
    return all_db_sentences[rand_id]
