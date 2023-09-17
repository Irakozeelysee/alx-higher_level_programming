#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database.
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

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
