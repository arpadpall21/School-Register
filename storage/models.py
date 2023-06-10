from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    name = Column(String(127))
    surname = Column(String(127))

    notes = relationship('Notes', backref='student', uselist=True)
    classes = relationship('Class', secondary='student_class_link')


class Notes(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    note = Column(SmallInteger)

    student = relationship('Student', backref='notes', uselist=False)


class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    class_name = Column(String(31))

    students = relationship('Student', secondary='student_class_link')


class StudentClassLink(Base):
    __tablename__ = 'student_class_link'

    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('classes.id'), primary_key=True)




# engine = create_engine('sqlite:///../school-register.db', echo=True)
# engine.connect()
    
    
    # sessionmaker = sessionmaker(bind=engine)
    # with sessionmaker() as session:                 # opens a session
    #     session