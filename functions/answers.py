from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.answers import Answers

from routes.auth import get_password_hash

from utils.pagination import pagination


def all_answers(search,user_id,topic_id,question_id, id, from_date, end_date, page, limit, db, status):
    answers = db.query(Answers).options(joinedload(Answers.user),joinedload(Answers.questions),joinedload(Answers.topic)).filter(Answers.id >= 0)
    if search:
         answers= answers.filter(Answers.answer.like(search))

    if user_id:
        answers = answers.filter(Answers.user_id == user_id)
    if topic_id:
        answers = answers.filter(Answers.order_id == topic_id)
    if question_id:
        answers = answers.filter(Answers.question_id == question_id)

    if id:
        answers = answers.filter(Answers.id == id)

    if from_date and end_date:
        answers = answers.filter(Answers.date >= from_date, Answers.date <= end_date)

    if status == True:
        answers = answers.filter(Answers.status == status)

    elif status == False:
        answers = answers.filter(Answers.status == status)

    else:
        answers = answers.filter(Answers.id >= 0)

    return pagination(form=answers, page=page, limit=limit)


def add_answers(form, db):
    new_answers = Answers(
        answer=form.answer,
        user_id =form.user_id,
        topic_id=form.topic_id,
        question_id =form.question_id ,


    )
    db.add(new_answers)
    db.commit()
    db.refresh(new_answers)

    return {"data": "Answer add base"}


def update_answers(id, form, db):
    if one_answer(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli answer yo'q")

    db.query(Answers).filter(Answers.id == id).update({
        Answers.answer: form.answer,
        Answers.option_a: form.option_a,
        Answers.user_id: form.user_id,
        Answers.topic_id: form.topic_id,
        Answers.question_id: form.question_id,
    })
    db.commit()


def one_answer(id, db):
    return db.query(Answers).filter(Answers.id == id).first()


def delete_answers(id, db):
    db.query(Answers).filter(Answers.id == id).update({
        Answers.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
