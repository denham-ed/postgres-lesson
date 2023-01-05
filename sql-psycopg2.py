import psycopg2

# Connect to "Chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select all names from "Artist" table
# cursor.execute('SELECT "Name" from "Artist"')

# Query 3 - Select Queen from Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only albums where the artistId is 51 on the 'Album' table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 4 - Select all tracks where the composer is Queen from the Track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen'])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the results (single)
# results = cursor.fetchone()

# Close the conntection
connection.close()

#print
for result in results:
    print(result)
