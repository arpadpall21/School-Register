# Shool-Register
Storing and retrieving student data with SQLAlchemy and Alembic ORM tools




- Alembic migration (2 steps at least)
- tables in db that demos one-to-many and many-to-many demos






- Document these 
  - Alembic usage for db migrations 
  - relation description 
  - this is not a production code, table schemas are ment to demonstrate relations between them (relations work like a charm) (ther are some warnings about this)
  
- Do this 
  - implement argparser
  - connection to a real db?
  - python app.py -h
  - python app.py upload (create)
  - python app.py get <studentId>
  - python app.py search [name]
  - python app.py delete <studentId>
  - python app.py clear 
  
  
  
- can I omit the name from Column() method?? -> updated this at the end of project
- TinyInteger in SQLAlchemy?
    -> Well NO! :D