# onito-api-data-endpoints

# README
This repository contains a Python Flask backend that implements various tasks using an SQLite database. Below are the details of the tasks and their corresponding routes:

## Task 1: Create SQL Tables and Populate CSV Data
- Two SQL tables named `movies` and `ratings` have been created.
- Data in these tables has been populated from given CSV files.

## Task 2: HTTP Server Routes
The Flask server provides the following routes:

### Route: GET /api/v1/longest-duration-movies
- Returns the top 10 movies with the longest runtime in JSON format.
- The output includes the following information: tconst, primaryTitle, runtimeMinutes, and genres.

### Route: POST /api/v1/new-movie
- Allows adding a new movie to the database.
- Accepts a JSON input containing the details of the new movie.
- On successful save, it returns the message "success".

### Route: GET /api/v1/top-rated-movies
- Returns the movies with an average rating greater than 6.0 in JSON format.
- The output is sorted by average rating.
- Includes the following information: tconst, primaryTitle, genre, and averageRating.

### Route: GET /api/v1/genre-movies-with-subtotals
- Displays a list of all movies grouped by genre, along with their respective numVotes subtotals.
- The calculation of subtotals is done within the SQL query, not the API code.

### Route: POST /api/v1/update-runtime-minutes
- Increments the runtimeMinutes of all movies using a SQL query.
- The increment value is as follows:
  - 15 if the genre is Documentary
  - 30 if the genre is Animation
  - 45 for all other genres

Please refer to the API documentation for more detailed information on how to use these routes.

## Database Details
- The backend uses an SQLite database to store the movies and ratings data.
- The SQL tables `movies` and `ratings` are created and populated with data from CSV files.
