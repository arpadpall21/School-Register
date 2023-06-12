from argparse import ArgumentParser, RawTextHelpFormatter
from typing import Union


def parse_cli_args() -> tuple[Union[str, None], Union[str, None]]:
    action_help_message = '''
    upload                 -> registers student entrys from upload.json
    get <student_id>       -> prints the specified <studentId> on stdout
    serach [student_name]  -> prints the serached <student_name> on stdout (or all records when [student_name] omitted)
    delete <student_id>    -> removes the specified <student_id> from the database
    clear                  -> purges all records from the database
    '''

    argument_parser = ArgumentParser(prog='school-register', formatter_class=RawTextHelpFormatter)
    argument_parser.add_argument('action', nargs='*', help=action_help_message)
    cli_args = argument_parser.parse_args()
    action = cli_args.action
    return (
        action[0] if len(action) > 0 else None,
        action[1] if len(action) > 1 else None
    )
