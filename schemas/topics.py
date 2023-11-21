from pydantic import BaseModel
from typing import Optional,List

class TopicBase(BaseModel):
    topic_name:str


class TopicCreate(TopicBase):
    pass

class TopicUpdate(TopicBase):
    id:int
    status:bool
