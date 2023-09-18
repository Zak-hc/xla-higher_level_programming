#!/usr/bin/python3
"""nn"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    e = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    s = sessionmaker(e)
    r = s()
    vi = r.query(City).order_by(City.id).all()
    for i in vi:
        print(f"{i.state.name}: ({i.id}) {i.name}")
