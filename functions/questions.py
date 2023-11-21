from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.questions import Questions
from routes.auth import get_password_hash

from utils.pagination import pagination


def all_questions(search, id,topic_id, from_date, end_date, page, limit, db, status):
    questions = db.query(Questions).options(joinedload(Questions.topic)).filter(Questions.id >= 0)
    if search:
         questions= questions.filter(Questions.question.like(search)|
                                     Questions.option_a.like(search) |
                                     Questions.option_b.like(search) |
                                     Questions.option_c.like(search) |
                                     Questions.option_d.like(search) |
                                     Questions.option_e.like(search) |
                                     Questions.option_f.like(search))

    if id:
        questions = questions.filter(Questions.id == id)

    if topic_id:
        questions = questions.filter(Questions.topic_id == topic_id)

    if from_date and end_date:
        questions = questions.filter(Questions.date >= from_date, Questions.date <= end_date)

    if status == True:
        questions = questions.filter(Questions.status == status)

    elif status == False:
        questions = questions.filter(Questions.status == status)

    else:
        questions = questions.filter(Questions.id >= 0)

    return pagination(form=questions, page=page, limit=limit)


def add_questions(form, db):
    new_question = Questions(
        topic_id=form.topic_id,
        question=form.question,
        option_a=form.option_a,
        option_b=form.option_b,
        option_c=form.option_c,
        option_d=form.option_d,
        option_e=form.option_e,
        option_f=form.option_f,

    )
    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return {"data": "Topic add base"}


def update_questions(id, form, db):
    if one_question(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli question yo'q")

    db.query(Questions).filter(Questions.id == id).update({
        Questions.question: form.question,
        Questions.option_a: form.option_a,
        Questions.option_b: form.option_b,
        Questions.option_c: form.option_c,
        Questions.option_d: form.option_d,
        Questions.option_e: form.option_e,
        Questions.option_f: form.option_f,
        Questions.status: form.status,

    })
    db.commit()


def one_question(id, db):
    return db.query(Questions).filter(Questions.id == id).first()


def delete_questions(id, db):
    db.query(Questions).filter(Questions.id == id).update({
        Questions.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
