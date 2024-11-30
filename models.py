import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, Text, String
from sqlalchemy.orm import Session, declarative_base

load_dotenv()
engine = create_engine(os.getenv('db'))
session = Session(bind=engine)

DB = declarative_base()

class Answers(DB):
    """
    класс  описывает модель Answer из BD
    id - id ответа
    answer - текст ответа
    mp3_file - имя привязанного mp3 файла
    """
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer = Column(Text, nullable=False)
    mp3_file = Column(String(1024), nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.answer[:10]}, {self.mp3_file}"
