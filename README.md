# dummy-flask-api

A simple flask api with PostgreSQL database connnection

##Considerations
- This was made in one day
- The DB_URL is in the databaseEngine.py file, but this is not by any means the right way to do it. The safe way is to declare it on environment variables
- just type the command `flask run` at the projects folder to run the project
- The routes are at app.py, but probably you should extract this into another file
