#!/usr/bin/python3
"""fiw"""
from sqlalchemy import Column, String, Integer
from model_state import State, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
if __name__ == "__main__":
    f = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    s = sessionmaker(f)
    sizo = s()
    u = sizo.query(State).first()
    if not u:
        print("Nothing")
    else:
        print(u.id, u.name, sep=': ')
