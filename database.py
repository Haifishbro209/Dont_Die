from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///users.db"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)

class Stats(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
   

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

    date = Column(Date, default=datetime.date.today)
    score = Column(Integer)

    KFA = Column(Integer)
    weight_in_kg = Column(Integer)
    height_in_cm = Column(Integer)
    BMI = Column(Integer)
    chill_HR = Column(Integer)
    systole = Column(Integer)
    dyastole = Column(Integer)

    Food_score = Column(Integer)
    Food_kcal = Column(Integer)
    Food_protein = Column(Integer)
    Food_junk = Column(Boolean)
    Food_suggar = Column(Integer)
    Food_notes_combined = Column(String)

    Sport_cardio = Column(Boolean)
    Sport_strenght = Column(Boolean)
    Sport_minutes = Column(Integer)
    Sport_steps = Column(Integer)

    Sleep_hours = Column(Float)
    Sleep_mood = Column(Integer)
    Sleep_continuity = Column(Boolean)

class FoodEntry(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey('days.id'), nullable=False)
    kcal = Column(Integer)
    junk = Column(Boolean)
    suggar = Column(Integer)
    note = Column(String)
    protein = Column(Integer)

class SportEntry(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey('days.id'), nullable=False)
    cardio = Column(Boolean)
    minutes = Column(Integer)
    strength = Column(Boolean)
    steps= Column(Integer)







Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_user(username):
    user = session.query(User).filter(User.username == username).first()
    if user:
        return
    new_user = User(username=username)
    session.add(new_user)
    session.commit()
