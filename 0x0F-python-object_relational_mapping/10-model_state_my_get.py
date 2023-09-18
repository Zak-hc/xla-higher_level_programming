#!/usr/bin/python3
"""fiw"""
from sqlalchemy import *
from model_state import State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == "__main__":
    var = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    s = sessionmaker(var)
    session = s()
    ver = sys.argv[4]
    rr = session.query(State).filter(State.name.like(ver)
                                     ).first()
    if rr:
        print(rr.id)
    else:
        print('Not found')
