#!/usr/bin/python3
"""Change the name of a State object in the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query and update the name of the State where id = 2 to "New Mexico"
        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
    except Exception as e:
        print("Error:", e)
        session.rollback()

    finally:
        # Close the session
        session.close()
