from pydantic import BaseModel
from typing import Optional,List

class QuestionsBase(BaseModel):
    topic_id:int
    question:str
    option_a:str
    option_b:str
    option_c:str
    option_d:str
    option_e:str
    option_f:str


class QuestionsCreate(QuestionsBase):
    pass

class QuestionsUpdate(QuestionsBase):
    id:int
    status:bool
