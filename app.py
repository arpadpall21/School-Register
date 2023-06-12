import json

from storage.model import connect_to_database, Student
from utils.query import create, update, get, search, delete, clear
from utils.arg_parser import parse_cli_args


def main():
    action, action_value = parse_cli_args()
    sessionmaker = connect_to_database('sqlite:///storage/school-register.db')
    with sessionmaker() as session:
        if action == 'upload':
            for entry in json.load(open('upload.json', 'r')):
                student_record = session.query(Student).get(entry['studentId'])
                if student_record is None:
                    create(session, entry)
                    continue
                update(session, entry, student_record)
            session.commit()

        if action == 'get':
            student_id = action_value
            get(session, student_id)

        if action == 'search':
            student_name = action_value
            search(session, student_name)

        if action == 'delete':
            student_id = action_value
            deleted_record_count = delete(session, student_id)
            session.commit()
            if deleted_record_count == 1:
                print(f'student deleted with student_id: {student_id}')

        if action == 'clear':
            clear(session)
            session.commit()


if __name__ == '__main__':
    main()
