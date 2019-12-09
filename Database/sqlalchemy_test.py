from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint

engine = create_engine('sqlite:////web/Sqlite-Data/example.db')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", backref="addresses")


Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_person1 = Person(name='Keith')
new_person2 = Person(name='Joe')
new_person3 = Person(name='Steve')

session.add(new_person1)
session.add(new_person2)
session.add(new_person3)
session.commit()

addresses = [
    Address(post_code='00001', person=new_person1),
    Address(post_code='00002', person=new_person2),
    Address(post_code='00003', person=new_person3),
]

for address in addresses:
    session.add(address)
    session.commit()

all_people = session.query(Person).join(Address).all()

for person in all_people:
    pprint(person.__dict__)
    for address in person.addresses:
        pprint(address.__dict__)

all_addresses = session.query(Address).join(Person).all()
for address in all_addresses:
    print(f'{address.person.name} has a postal code of {address.post_code}')