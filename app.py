import json

from storage.model import connect_to_database, Student
from utils.query import create, update, get, search, delete, clear


def main():
    sessionmaker = connect_to_database('sqlite:///storage/school-register.db')
    with sessionmaker() as session:

        # # upload
        # for entry in json.load(open('upload.json')):
        #     student_record = session.query(Student).get(entry['studentId'])
        #     if student_record is None:
        #         create(session, entry)
        #         continue
        #     update(session, entry, student_record)
        # session.commit()
        
        
        # # get
        # student_id = 324
        # get(session, student_id, )
        
        
        # # search
        # student_name = 'Pamella'
        # student_name = None
        # search (session, student_name)
        
        
        # # delete
        # student_id = 123
        # deleted_record_count = delete(session, student_id)
        # session.commit()
        # if deleted_record_count > 0:
        #     print(f'student deleted with student_id: {student_id}')

        
        # # clear
        # clear(session)
        # session.commit()
        
        
if __name__ == '__main__':
    main()
