from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db.create_engine("postgresql:///chinook")
base = declarative_base()


Session = sessionmaker(db)
