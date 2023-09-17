#!/usr/bin/python3
"""
Module to define the State class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class City(Base):
    """Class representing a state in the database.
    Attributes:
    id (int): An auto-generated,
    unique integer representing the primary key.
    name (str): A string with a maximum of
    128 characters representing the state name.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = column(Integer, ForeignKey("states.id"), nullable=False)
