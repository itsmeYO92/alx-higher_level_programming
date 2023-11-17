#!/usr/bin/python3
"""
    definition of the class state
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
        State class that defines state with an id and a name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable = False)
    cities = relationship('City', backref = 'state', cascade='all, delete')
