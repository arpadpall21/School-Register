from storage.model import Student, Grade, Class


def create(entry: dict, session: object) -> None:
    session.add(Student(
        student_id=entry['studentId'],
        name=entry['name'],
        surname=entry['surname'],
        grades=[Grade(student_id=entry['studentId'], grade=grade) for grade in entry['grades']],
        classes=_get_or_create_class_records(entry['classes'], session)))


def update(student_record: Student, entry: dict, session: object) -> None:
    student_record.name = entry['name']
    student_record.surname = entry['surname']
    student_record.classes = _get_or_create_class_records(entry['classes'], session)


def get(student_id: int, session: object) -> None:
    pass


def delete(student_id: int, session: object) -> None:
    pass


def search(student_name: str, session: object) -> None:
    pass


def _get_or_create_class_records(classes: list[str], session: object) -> list[Class]:
    result = []
    for class_name in classes:
        class_record = session.query(Class).get(class_name)
        if class_record is None:
            class_record = Class(class_name=class_name)
        result.append(class_record)
    return result
