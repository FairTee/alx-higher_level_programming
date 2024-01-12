#!/usr/bin/python3
"""Delete all State objects with a name containing the letter a
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
        # Query and delete all State objects
        # With a name containing the letter 'a'
        states_to_delete = session.query(State).filter(
                State.name.like('%a%')).all()

        for state in states_to_delete:
            session.delete(state)

        session.commit()

    except Exception as e:
        print("Error:", e)
        session.rollback()

    finally:
        # Close the session
        session.close()
