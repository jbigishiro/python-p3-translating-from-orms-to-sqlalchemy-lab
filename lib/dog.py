from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_table(Base,engine):
    engine=create_engine('sqlite:///dogs.db')
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs=session.query(Dog)
    return [dog for dog in dogs]

def find_by_name(session, name):
    dogs_by_name = session.query(Dog).filter(Dog.name == name).first()
    return dogs_by_name


def find_by_id(session, id):
    dogs_by_id = session.query(Dog).filter(Dog.id == id).first()
    return dogs_by_id


def find_by_name_and_breed(session, name, breed):
    dogs_by_name_and_breed = session.query(Dog).filter(Dog.name == name , Dog.breed == breed).first()
    return dogs_by_name_and_breed


def update_breed(session, dog, breed):
    for dog in session.query(Dog):
        dog.breed = breed