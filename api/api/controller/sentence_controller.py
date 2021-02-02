import uuid
from sqlalchemy.orm import Session
from datetime import datetime
from api.model.sentence_model import Sentence

def get_sentence(db: Session, sentence_id: int):
    """
    Get single sentence from database based on its sentence_id
    :param db: database session
    :param sentence_id: id identifying a sentence
    :return: sentence
    """
    return db.query(Sentence).filter(Sentence.id == sentence_id).first()


def get_all_sentences(db: Session):
    """
    Get all sentences from database
    :param db: database session
    :return: list of sentences
    """
    return db.query(Sentence).all()


def add_sentence(db: Session, sentence: str):
    """
    Create a new sentence in database
    :param db: database session
    :param sentence: sentence to record
    :return: sentence
    """
    db_sentence = Sentence(
                sentence=sentence,
    )

    db.add(db_sentence)
    db.commit()
    db.refresh(db_sentence)

    return db_sentence


def delete_sentence(db: Session, sentence_id: str):
    """
    Delete a sentence base on its id
    :param db: database session
    :param sentence_id: id identifying a sentence
    :return: None if sentence not found, true if success
    """

    sentence_to_delete = db.query(Sentence).filter(Sentence.id == sentence_id)
    deleted_sentence = sentence_to_delete.delete()

    if deleted_sentence == 0:
        return None
    else:
        db.commit()
        return True
