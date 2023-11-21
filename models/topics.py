import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Topics(Base):
    __tablename__ = "Topics"
    id = Column(Integer, primary_key=True,autoincrement=True)
    topic_name = Column(String(30), nullable=True)
    status = Column(Boolean, nullable = True ,default=True)




    answer = relationship("Answers", back_populates="topic")

    questions = relationship("Questions", back_populates="topic")