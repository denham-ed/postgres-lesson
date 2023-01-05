from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Creates instance of a session
Session = sessionmaker(db)
# Opens a session
session = Session()
# Creates the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table

ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programme"
)

# Add each instance of programme to your session
session.add(ada_lovelace)

# Commit our session to the database
session.commit()

# Query to find all programmes
programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.first_name, programmer.last_name)
