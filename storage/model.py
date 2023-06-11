from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(127))
    surname = Column(String(127))
    grades = relationship('Grade', back_populates='student', uselist=True)
    classes = relationship('Class', secondary='student_class_link', overlaps='classes')


class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.student_id'))
    grade = Column(SmallInteger)
    student = relationship('Student', back_populates='grades', uselist=False)


class Class(Base):
    __tablename__ = 'class'
    class_name = Column(String(31), primary_key=True)
    students = relationship('Student', secondary='student_class_link', overlaps='classes')


class StudentClassLink(Base):
    __tablename__ = 'student_class_link'
    student_id = Column(Integer, ForeignKey('student.student_id'), primary_key=True)
    class_name = Column(String(31), ForeignKey('class.class_name'), primary_key=True)


def connect_to_database(url: str) -> sessionmaker:
    try:
        engine = create_engine(url, echo=False)
        engine.connect()
        return sessionmaker(bind=engine)
    except Exception as e:
        raise Exception(f'Could not connect to database: {e}')
