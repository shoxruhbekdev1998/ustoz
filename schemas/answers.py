from pydantic import BaseModel
from typing import Optional,List

class AnswerBase(BaseModel):
    answer:str
    user_id:int
    topic_id:int
    question_id:int

class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
    id:int
    status:bool
