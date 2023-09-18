#!/usr/bin/python3
"""fiw"""
from sqlalchemy import *
from model_state import State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == "__main__":
    var = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    s = sessionmaker(var)
    session = s()

    rr = session.query(State).filter(State.name.like('Louisiana')).all()
    for i in rr:
        session.delete(i)
    session.commit()
    ver = State(name='Louisiana')
    session.add(ver)
    session.commit()
    rr = session.query(State).filter(State.name.like('Louisiana')).first()
    print(rr.id)
