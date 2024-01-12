#!/usr/bin/python3
"""Print State object with the name passed as an argument
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database, state_name = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the State object with the specified name
    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
