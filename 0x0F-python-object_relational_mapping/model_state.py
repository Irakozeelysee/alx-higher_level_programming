#!/usr/bin/python3
"""Module to define the State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing a state in the database.
    Attributes:
    id (int): An auto-generated, unique integer representing the primary key.
    name (str): A string with a maximum of
    128 characters representing the state name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
