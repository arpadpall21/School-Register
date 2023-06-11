import json

from storage.model import connect_to_database, Student
from utils.query import create, update, get, delete, search


def main():
    sessionmaker = connect_to_database('sqlite:///storage/school-register.db')
    with sessionmaker() as session:

        # upload
        for entry in json.load(open('upload.json')):
            student_record = session.query(Student).get(entry['studentId'])
            if student_record is None:
                create(entry, session)
                continue
            update(student_record, entry, session)
        session.commit()
        
        # get
        # get(student_id, session)
        
        # delete
        # get(student_id, session)
        
        # search
        # get(student_name, session)

if __name__ == '__main__':
    main()
