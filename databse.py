import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create movies table
cursor.execute('''
    CREATE TABLE movies2 (
        tconst TEXT PRIMARY KEY,
        titleType TEXT,
        primaryTitle TEXT,
        runtimeMinutes INTEGER,
        genres TEXT
    )
''')

# Create ratings table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratings (
        tconst TEXT PRIMARY KEY,
        averageRating REAL,
        numVotes INTEGER
    )
''')

# Import data from movies.csv
movies_data = pd.read_csv('movies.csv')
movies_data.to_sql('movies2', conn, if_exists='append', index=False)

# Import data from ratings.csv
ratings_data = pd.read_csv('ratings.csv')
ratings_data.to_sql('ratings', conn, if_exists='append', index=False)

# Commit changes and close the connection
conn.commit()

conn.close()
