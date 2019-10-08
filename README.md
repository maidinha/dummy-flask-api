# dummy-flask-api

A simple flask api with PostgreSQL database connnection

## Observations
- This was made in one day
- The DB_URL is in the databaseEngine.py file, but this is not by any means the right way to do it. The safe way is to declare it on environment variables or in a file or so.
- The DB_URL is pointing to the default postgresql database, but you can change it if you wish
- The routes are at app.py, but probably you should extract this into another file

## How to run
Just type the command `flask run` at the project folder to run the project
