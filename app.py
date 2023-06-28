from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/api/v1/longest-duration-movies', methods=['GET'])
def get_longest_duration_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    query = '''
        SELECT tconst, primaryTitle, runtimeMinutes, genres
        FROM movies2
        ORDER BY runtimeMinutes DESC
        LIMIT 10
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    movies = []
    for row in result:
        tconst, primaryTitle, runtimeMinutes, genres = row
        movies.append({
            'tconst': tconst,
            'primaryTitle': primaryTitle,
            'runtimeMinutes': runtimeMinutes,
            'genres': genres
        })

    return jsonify(movies)


@app.route('/api/v1/new-movie', methods=['POST'])
def add_new_movie():
    movie = request.get_json()

    # Extract movie details from the JSON object
    tconst = movie['tconst']
    primaryTitle = movie['primaryTitle']
    runtimeMinutes = movie['runtimeMinutes']
    genres = movie['genres']

    # Save the movie details into the database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    query = '''
        INSERT INTO movies2 (tconst, primaryTitle, runtimeMinutes, genres)
        VALUES (?, ?, ?, ?)
    '''
    cursor.execute(query, (tconst, primaryTitle, runtimeMinutes, genres))
    conn.commit()
    conn.close()

    return 'success'


@app.route('/api/v1/top-rated-movies', methods=['GET'])
def get_top_rated_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    query = '''
        SELECT m.tconst, m.primaryTitle, m.genres, r.averageRating
        FROM movies2 m
        JOIN ratings r ON m.tconst = r.tconst
        WHERE r.averageRating > 6.0
        ORDER BY r.averageRating DESC
    '''
    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    movies = []
    for row in result:
        tconst, primaryTitle, genres, averageRating = row
        movies.append({
            'tconst': tconst,
            'primaryTitle': primaryTitle,
            'genre': genres,
            'averageRating': averageRating
        })

    return jsonify(movies)


@app.route('/api/v1/genre-movies-with-subtotals', methods=['GET'])
def get_genre_movies_with_subtotals():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    query = '''
        SELECT genres, primaryTitle, numVotes
        FROM movies2
        GROUP BY genres, primaryTitle
        UNION ALL
        SELECT genres, 'TOTAL', SUM(numVotes) AS numVotes
        FROM movies
        GROUP BY genres
    '''
    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    movies = []
    for row in result:
        genre, primaryTitle, numVotes = row
        movies.append({
            'Genre': genre,
            'primaryTitle': primaryTitle,
            'numVotes': numVotes
        })

    return jsonify(movies)


@app.route('/api/v1/update-runtime-minutes', methods=['POST'])
def update_runtime_minutes():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Increment runtimeMinutes based on genre using SQL query
    query = '''
        UPDATE movies2
        SET runtimeMinutes = runtimeMinutes +
            CASE
                WHEN genres = 'Documentary' THEN 15
                WHEN genres = 'Animation' THEN 30
                ELSE 45
            END
    '''
    cursor.execute(query)
    conn.commit()
    conn.close()

    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
