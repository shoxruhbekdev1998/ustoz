import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True,autoincrement=True)
    roll = Column(String(20), nullable=True)
    name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    middle_name = Column(String(30), nullable=True)
    phone_number = Column(Integer, nullable=True)
    region = Column(String(30), nullable=True)
    city = Column(String(30), nullable=True)
    village = Column(String(30), nullable=True)
    home_number = Column(Integer,nullable=True)
    username = Column(String(50),nullable=True)
    password = Column(String(200),nullable=True)
    birth_day = Column(String(200),nullable = True)
    tg_id = Column(Integer,nullable=True)
    tall = Column(Integer,nullable=True)
    weight = Column(Integer,nullable=True)
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)
    token = Column(String(400),default = '',nullable=True)


    answer = relationship("Answers", back_populates="user")