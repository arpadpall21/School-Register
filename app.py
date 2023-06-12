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
        elif action == 'get':
            if action_value is None:
                print('No student id provided: [python app.py get <student_id>]')
                return
            get(session, int(action_value))
        elif action == 'search':
            search(session, action_value)
        elif action == 'delete':
            if action_value is None:
                print('No student_id provided: [python app.py delete <student_id>]')
                return
            delete(session, int(action_value))
        elif action == 'clear':
            clear(session)
        else:
            if action is None:
                print('No action provided')
            else:
                print(f'Invalid action: {action}')


if __name__ == '__main__':
    main()
