#!/usr/bin/python3
"""Prints the State object ID with the given name from the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
            format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == argv[4]).all()

    if states == []:
        print("Not found")
    else:
        for state in states:
            print("{}".format(state.id))

    session.close()
