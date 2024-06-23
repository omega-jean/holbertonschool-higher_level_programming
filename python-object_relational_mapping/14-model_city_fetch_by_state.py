#!/usr/bin/python3
"""task 14"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
                           {password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
