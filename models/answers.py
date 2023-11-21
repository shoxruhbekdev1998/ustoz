import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Answers(Base):
    __tablename__ = "Answers"
    id = Column(Integer, primary_key=True,autoincrement=True)
    answer = Column(Text, nullable=True)

    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

    user_id = Column(Integer, ForeignKey("Users.id"), nullable=True)
    topic_id = Column(Integer, ForeignKey("Topics.id"), nullable=True)
    question_id = Column(Integer, ForeignKey('Questions.id'), nullable=True)

    user = relationship("Users", back_populates="answer")
    topic = relationship("Topics", back_populates="answer")
    questions = relationship("Questions", back_populates="answer")
