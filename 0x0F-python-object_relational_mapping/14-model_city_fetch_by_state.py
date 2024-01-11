#!/usr/bin/python3
"""Fetch all City objects from the database and print them by state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query and print all City objects by state in ascending order by cities.id
        cities_by_state = session.query(State, City).join(City).order_by(City.id).all()

        for state, city in cities_by_state:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        session.close()
