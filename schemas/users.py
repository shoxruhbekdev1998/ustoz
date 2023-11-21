from pydantic import BaseModel
from typing import Optional,List

class UserBase(BaseModel):
    roll:Optional[str]=None
    name:str
    last_name: Optional[str]=None
    middle_name:Optional[str]=None
    phone_number:int
    tg_id:int
    tall:Optional[int]=None
    weight:Optional[int]=None
    region:Optional[str]=None
    city:Optional[str]=None
    village:Optional[str]=None
    home_number:Optional[int]=None
    birth_day:Optional[str]=None
    username:Optional[str]=None
    password:Optional[str]=None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    id:int
    status:bool



class Token(BaseModel):
    access_token=str
    token=str

class TokenData(BaseModel):
    id: Optional[str] = None

class UserCurrent(BaseModel):
    roll: str
    name: str
    last_name: str
    middle_name: str
    phone_number: int
    region: str
    city: str
    village: str
    home_number: int
    birth_day: int
    tg_id: int
    tall: int
    weight: int
    username: str
    password: str
    status: bool