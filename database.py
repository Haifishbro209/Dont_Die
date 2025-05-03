from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///db.db"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    date = Column(Date, default=datetime.date.today)
    score = Column(Integer, default=0)

    KFA = Column(Integer, default=0)
    weight_in_kg = Column(Integer, default=0)
    height_in_cm = Column(Integer, default=0)
    BMI = Column(Integer, default=0)
    chill_HR = Column(Integer, default=0)
    systole = Column(Integer, default=0)
    dyastole = Column(Integer, default=0)

    Food_score = Column(Integer, default=0)
    Food_kcal = Column(Integer, default=0)
    Food_protein = Column(Integer, default=0)
    Food_junk = Column(Boolean, default=False)
    Food_suggar = Column(Integer, default=0)
    Food_notes_combined = Column(String, default="")

    Sport_cardio = Column(Boolean, default=False)
    Sport_strenght = Column(Boolean, default=False)
    Sport_minutes = Column(Integer, default=0)
    Sport_steps = Column(Integer, default=0)

    Sleep_hours = Column(Float, default=0.0)
    Sleep_mood = Column(Integer, default=0)
    Sleep_continuity = Column(Boolean, default=False)

class FoodEntry(Base):
    __tablename__ = "food_entries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey('days.id'), nullable=False)
    kcal = Column(Integer, default=0)
    junk = Column(Boolean, default=False)
    suggar = Column(Integer, default=0)
    note = Column(String, default="")
    protein = Column(Integer, default=0)

class SportEntry(Base):
    __tablename__ = "sport_entries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey('days.id'), nullable=False)
    cardio = Column(Boolean, default=False)
    minutes = Column(Integer, default=0)
    strength = Column(Boolean, default=False)
    steps = Column(Integer, default=0)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def check_day(user_id):
    date = datetime.date.today()
    day_exists_id = session.query(Day.id).filter(
        Day.date == date,
        Day.user_id == user_id
    ).scalar()
    if day_exists_id:
        return day_exists_id
    else:
        new_day = Day(user_id=user_id, date=date)
        session.add(new_day)
        session.commit()
        return new_day.id
    

def add_sport_Entry(user_id,cardio = False,strength= False,minutes= 0,steps= 0):
    day_id = check_day(user_id)
    new_entry = SportEntry(day_id = day_id,cardio = cardio, strength = strength,minutes = minutes,steps= steps)
    session.add(new_entry)
    day = session.query(Day).filter(Day.id == day_id).first()

    day.Sport_minutes += minutes
    day.Sport_steps += steps
    if cardio:
        day.Sport_cardio = True
    if strength:
        day.Sport_strenght = True
    
    session.add(day)
    session.commit()

def add_user(username):
    user = session.query(User).filter(User.username == username).first()
    if user:
        return
    new_user = User(username=username)
    session.add(new_user)
    session.commit()
