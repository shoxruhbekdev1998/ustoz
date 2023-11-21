from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.questions import add_questions, all_questions, update_questions, delete_questions
from schemas.questions import *

router_question = APIRouter()

@router_question.post('/add')
def add_question(form:QuestionsCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_questions(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_question.get('/',status_code=200)
def get_question(search:str=None,id:int=0,topic_id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_questions(db=db,status=status,search=search,id=id,topic_id=topic_id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_question.put('/update',)
def update_question(form:QuestionsUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_questions(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_question.delete('/del',)
def delete_question(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_questions(id=id,db=db)


