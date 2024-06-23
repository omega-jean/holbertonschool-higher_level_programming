#!/usr/bin/python3
# Prints the first State object from the database hbtn_0e_6_usa.
# Usage: ./8-model_state_fetch_first.py <mysql username> /
#                                       <mysql password> /
#                                       <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}\
                           @localhost:3306/{database}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
