#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
