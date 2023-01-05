from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based Model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    Price = Column(Float)


# Creates instance of a session
Session = sessionmaker(db)
# Opens a session
session = Session()
# Creates the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - Select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - Select all names from "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - Select Queen from Artist table
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")
# select_query = artist_table.select().where(artist_table.c.Name == "Queen")

