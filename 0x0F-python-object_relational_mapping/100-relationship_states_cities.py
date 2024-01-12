#!/usr/bin/python3
"""Create the State"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create the State "California" with the City "San Francisco"
        california = State(
                name='California', cities=[City(name='San Francisco')])

        # Add the new state to the session
        session.add(california)

        # Commit the changes to the database
        session.commit()

    except Exception as e:
        print("Error:", e)
        session.rollback()

    finally:
        # Close the session
        session.close()
