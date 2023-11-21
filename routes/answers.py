from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.answers import add_answers, all_answers, update_answers, delete_answers
from schemas.answers import *

router_answer = APIRouter()

@router_answer.post('/add')
def add_answer(form:AnswerCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_answers(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_answer.get('/',status_code=200)
def get_answer(search:str=None,id:int=0,user_id:int=0,topic_id:int=0,question_id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_answers(db=db,status=status,search=search,id=id,user_id=user_id,topic_id=topic_id,question_id=question_id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_answer.put('/update',)
def update_answer(form:AnswerUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_answers(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_answer.delete('/del',)
def delete_answer(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_answers(id=id,db=db)



