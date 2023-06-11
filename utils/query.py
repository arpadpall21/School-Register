from storage.model import Student, Grade, Class, StudentClassLink


def create(session: object, entry: dict) -> None:
    session.add(Student(
        student_id=entry['studentId'],
        name=entry['name'],
        surname=entry['surname'],
        grades=[Grade(grade=grade) for grade in entry['grades']],
        classes=_get_or_create_class_records(entry['classes'], session)))


def update(session: object, entry: dict, student_record: Student) -> None:
    student_record.name = entry['name']
    student_record.surname = entry['surname']
    student_record.grades = _overide_grade_records(entry['studentId'], entry['grades'], session)
    student_record.classes = _get_or_create_class_records(entry['classes'], session)


def get(session: object, student_id: int) -> None:
    student_record = session.query(Student).get([student_id])
    if student_record is None:
        print(f'No record found with student_id: {student_id}')
        return
    _print_student_record(student_record)


def search(session: object, student_name: str = None) -> None:
    if student_name is None:
        search_results = session.query(Student).all()
        for student_record in search_results:
            _print_student_record(student_record)
        return
    search_results = session.query(Student).filter(Student.name == student_name).all()
    if len(search_results) == 0:
        print(f'No record found with student_name: {student_name}')
    for student_record in search_results:
        _print_student_record(student_record)


def delete(session: object, student_id: int) -> int:
    return session.query(Student).filter(Student.student_id == student_id).delete()


def clear(session: object) -> None:
    for Model in [Student, Grade, Class, StudentClassLink]:
        session.query(Model).delete()


def _get_or_create_class_records(classes: list[str], session: object) -> list[Class]:
    result = []
    for class_name in classes:
        class_record = session.query(Class).get(class_name)
        if class_record is None:
            class_record = Class(class_name=class_name)
        result.append(class_record)
    return result


def _overide_grade_records(student_id: int, grades: list[str], session: object) -> list[Grade]:
    session.query(Grade).filter(Grade.student_id == student_id).delete()
    return [Grade(grade=grade) for grade in grades]


def _print_student_record(student_record: Student) -> None:
    print({
        'student_id': student_record.student_id,
        'name': student_record.name,
        'surname': student_record.surname,
        "grades": [grade.grade for grade in student_record.grades],
        "classes": [_class.class_name for _class in student_record.classes],
    })
