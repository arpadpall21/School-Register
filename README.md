# Shool-Register
## Description
- This is a school register storage application demo where student entries can be stored and retrieved in a database, for the sake of simplicity sqlite is used as a database (`storage/school-register.db` file)
- SQLAlchemy ORM is used for database operations
- Alembic is used to control database migrations (2 migration versions are deployed)
- This is a fully working tool but not a production code, the goal is to demonstrate SQL table relations through ORM as follows:
  - one-to-many relation between `Student` and `Grade` tables
  - many-to-many relation between `Student` and `Class` tables (`StudentClassLink` is the link table between them)
## Setup
- Run `pip install -r requirements.txt` to install required packages (recommend using virtual environment)
- Run `alembic upgrade heads` to migrate the database to the latest version
## Usage
- The `upload.json` file contains student records to be uploaded to the database (modify this file to upload student entries)
- Running the `app.py` file with various arguments will trigger different actions as follows:
  - `python app.py --help` will display a help message (list available arguments)
  - `python app.py upload` will upload student entries from the `upload.json` file to the database 
    - to update an existing student record simply modify the student entry in the `upload.json` file and run the `python app.py upload` command again
  - `python app.py get <studentId>` retrieve and print the student entry with the given id from the database
  - `python app.py search [name]` will search for student entries with the given name (if no name is provided all student entries will be printed)
  - `python app.py delete <studentId>` delete the student entry with the given id from the database
  - `python app.py clear` deletes all student entries from the database (purges the database)
