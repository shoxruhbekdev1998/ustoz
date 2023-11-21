import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Questions(Base):
    __tablename__ = "Questions"
    id = Column(Integer, primary_key=True,autoincrement=True)
    question = Column(Text,nullable=True)
    option_a = Column(Text, nullable=True)
    option_b = Column(Text, nullable=True)
    option_c = Column(Text, nullable=True)
    option_d = Column(Text, nullable=True)
    option_e = Column(Text, nullable=True)
    option_f = Column(Text, nullable=True)

    status = Column(Boolean, nullable = True ,default=True)

    topic_id = Column(Integer, ForeignKey("Topics.id"), nullable=True)


    answer = relationship("Answers", back_populates="questions")
    topic = relationship("Topics",back_populates="questions")