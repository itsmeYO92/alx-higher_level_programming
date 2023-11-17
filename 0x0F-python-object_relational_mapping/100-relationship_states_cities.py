#!/usr/bin/python3
"""
    Prints the city objects from a database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name = 'California')
    session.add(california)
    session.commit()
    san_francisco = City(name = 'San Francisco', state = california)
    session.add(san_francisco)
    session.commit()
