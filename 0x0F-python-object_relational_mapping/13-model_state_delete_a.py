#!/usr/bin/python3
"""
    Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = (
        session.query(State)
        .filter(State.name.contains('a'))
        .all()
    )
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
            session.commit()

    session.close()
