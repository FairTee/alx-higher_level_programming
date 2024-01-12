#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


def list_cities_states(username, password, database):
    """List all City objects with their corresponding State objects"""
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        state_name = city.state.name
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    # Close the session
    session.close()


if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list cities and their corresponding states
    list_cities_states(username, password, database)
