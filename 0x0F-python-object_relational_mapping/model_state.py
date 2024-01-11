#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """Class representing the states table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table in the database
    Base.metadata.create_all(engine)

    # Optionally, you can check the created table
    # for column in Base.metadata.tables['states'].columns:
    #     print(column)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example: Add a new state to the 'states' table
    new_state = State(name='New State')
    session.add(new_state)
    session.commit()

    # Query and print all states in the 'states' table
    states = session.query(State).all()
    for state in states:
        print(state.id, state.name)

    # Close the session
    session.close()
