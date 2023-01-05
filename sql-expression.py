from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Executing the instruction our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create varibale for "artist" tab;e
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("Price", Float)
)

# Making the Connection
with db.connect() as connection:
    # Query 1 - Select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - Select all names from "Artist" table
    # select_query = artist_table.select().with_only_columns(
    # [artist_table.c.Name])

    # Query 3 - Select Queen from Artist table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
