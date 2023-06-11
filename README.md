# Shool-Register
Storing and retrieving student data with SQLAlchemy and Alembic ORM tools




- Alembic migration (2 steps at least)
- tables in db that demos one-to-many and many-to-many demos






- Document these 
  - Alembic usage for db migrations 
  - relation description 
  - this is not a production code, table schemas are ment to demonstrate relations between them (relations work like a charm)
  
- Do this 
  - implement argparser
  - connection to a real db?
  - python app.py upload (create)
  - python app.py clear 
  - python app.py get [studentId]
  - python app.py delete <studentId>
  - python app.py search [name]
  
  
  
- can I omit the name from Column() method?? -> updated this at the end of project
- TinyInteger in SQLAlchemy?
    -> Well NO! :D