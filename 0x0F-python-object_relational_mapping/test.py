#!/usr/bin/python3
from sqlalchemy import Column, Integer, String  
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

db_url = "mysql+mysqldb://root:root@localhost/hbtn_0e_4_usa"
engine = create_engine(db_url)

Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()
Stateq = session.query(State).order_by(State.id).all()
for state in Stateq: # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
