from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.topics import Topics
from routes.auth import get_password_hash

from utils.pagination import pagination

def all_topics(search,id,from_date,end_date,page,limit,db,status):
    topics = db.query(Topics).options(joinedload(Topics.questions)).filter(Topics.id>=0)
    if search:
        topics = topics.filter(Topics.topic_name.like(search))

    if id:
        topics = topics.filter(Topics.id==id)

    if from_date and end_date:
        topics = topics.filter(Topics.date >= from_date, Topics.date <= end_date)

    if status == True:
     topics = topics.filter(Topics.status==status)

    elif status == False:
     topics = topics.filter(Topics.status==status)

    else:
        topics = topics.filter(Topics.id>=0)

    return pagination(form=topics, page=page, limit=limit)


def add_topics(form, db):
    new_topics = Topics(
        topic_name=form.topic_name,

    )
    db.add(new_topics)
    db.commit()
    db.refresh(new_topics)


    return {"data": "Topic add base"}


def update_topics(id, form, db):
    if one_topic(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli topic yo'q")

    db.query(Topics).filter(Topics.id == id).update({
        Topics.topic_name: form.topic_name,
        Topics.status: form.status,

    })
    db.commit()


def one_topic(id, db):
    return db.query(Topics).filter(Topics.id == id).first()


def delete_topics(id, db):
    db.query(Topics).filter(Topics.id == id).update({
        Topics.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
