#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    filtered_states = session.query(State).filter(
            State.name.like('%a%')
    ).order_by(State.id).all()

    for state in filtered_states:
        print("{}: {}".format(state.id, state.name))

    session.close()
