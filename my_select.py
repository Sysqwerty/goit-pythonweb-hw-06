from enum import Enum
from pprint import pprint

from sqlalchemy import select, func, and_
from connect import session
from models import Student, Score, Subject, Group, Teacher, student_m2m_group
from sqlalchemy import cast, Float


# Зробити наступні вибірки з отриманої бази даних:

# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    result = (session.execute(
        select(
            Student.name,
            cast(func.avg(Score.score), Float).label("avg_score")
        )
        .join(Score)
        .group_by(Student)
        .order_by(func.avg(Score.score).desc())
        .limit(5)
    ).mappings().all())

    print("1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
    return result


# 2. Знайти студента із найвищим середнім балом з певного предмета.
def select_2(subject: str):
    result = (session.execute(
        select(
            Student.name,
            cast(func.avg(Score.score), Float).label("avg_score"),
            Subject.name
        )
        .select_from(Student)
        .join(Score)
        .join(Subject)
        .where(Subject.name == subject)
        .group_by(Student.name, Subject.name)
        .order_by(func.avg(Score.score).desc())
        .limit(1)
    ).mappings().one())

    print(f"\n2. Знайти студента із найвищим середнім балом з певного предмета '{subject}'.")
    return result


# 3. Знайти середній бал у групах з певного предмета.
def select_3(subject: str):
    result = (session.execute(
        select(
            Subject.name.label("Subject_name"),
            Group.name.label("Group_name"),
            cast(func.avg(Score.score), Float).label("avg_score")
        )
        .select_from(Score)
        .join(Subject)
        .join(Student)
        .join(student_m2m_group)
        .join(Group)
        .where(Subject.name == subject)
        .group_by(Subject.name, Group.name)
    ).mappings().all())

    print(f"\n3. Знайти середній бал у групах з певного предмета '{subject}'.")
    return result


# 4. Знайти середній бал на потоці(по всій таблиці оцінок).
def select_4():
    result = (session.execute(
        select(
            cast(func.avg(Score.score), Float).label("avg_score")
        )
        .select_from(Score)
    ).mappings().one())

    print("4. Знайти середній бал на потоці(по всій таблиці оцінок).")
    return result


# 5. Знайти які курси читає певний викладач.
def select_5(teacher: str):
    result = (session.execute(
        select(
            Teacher.name.label("Teacher_name"),
            Subject.name.label("Subject_name")
        )
        .select_from(Teacher)
        .join(Subject)
        .where(Teacher.name == teacher)
    ).mappings().all())

    print(f"\n5. Знайти які курси читає певний викладач '{teacher}'.")
    return result


# 6. Знайти список студентів у певній групі.
def select_6(group: str):
    result = (session.execute(
        select(
            Group.name.label("Group_name"),
            Student.name.label("Student_name")
        )
        .select_from(Group)
        .join(student_m2m_group)
        .join(Student)
        .where(Group.name == group)
    ).mappings().all())

    print(f"\n6. Знайти список студентів у певній групі '{group}'.")
    return result


# 7. Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(group: str, subject: str):
    result = (session.execute(
        select(
            Student.name.label("Student_name"),
            Group.name.label("Group_name"),
            Subject.name.label("Subject_name"),
            Score.score.label("Score")
        )
        .select_from(Score)
        .join(Subject)
        .join(Student)
        .join(student_m2m_group)
        .join(Group)
        .where(and_(Group.name == group, Subject.name == subject))
    ).mappings().all())

    print(f"\n7. Знайти оцінки студентів у окремій групі '{group}' з певного предмета '{subject}'.")
    return result


# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.

def select_8(teacher: str):
    result = (session.execute(
        select(
            Teacher.name.label("Teacher_name"),
            Subject.name.label("Subject_name"),
            cast(func.avg(Score.score), Float).label("avg_score")
        )
        .select_from(Teacher)
        .join(Subject)
        .join(Score)
        .where(Teacher.name == teacher)
        .group_by(Teacher.name, Subject.name)
    ).mappings().all())

    print(f"\n8. Знайти середній бал, який ставить певний викладач '{teacher}' зі своїх предметів.")
    return result


# 9. Знайти список курсів, які відвідує певний студент.

def select_9(student: str):
    result = (session.execute(
        select(
            Student.name.label("Student_name"),
            Subject.name.label("Subject_name")
        )
        .select_from(Student)
        .join(Score)
        .join(Subject)
        .where(Student.name == student)
        .group_by(Student.name, Subject.name)
    ).mappings().all())

    print(f"\n9. Знайти список курсів, які відвідує певний студент '{student}'.")
    return result


# 10. Список курсів, які певному студенту читає певний викладач.

def select_10(student: str, teacher: str):
    result = (session.execute(
        select(
            Student.name.label("Student_name"),
            Subject.name.label("Subject_name"),
            Teacher.name.label("Teacher_name")
        )
        .select_from(Student)
        .join(Score)
        .join(Subject)
        .join(Teacher)
        .where(and_(Student.name == student, Teacher.name == teacher))
        .group_by(Student.name, Subject.name, Teacher.name)
    ).mappings().all())

    print(f"\n10. Список курсів, які певному студенту '{student}' читає певний викладач '{teacher}'.")
    return result


if __name__ == "__main__":
    pprint(select_1())
    pprint(select_2("Physics"))
    pprint(select_3("Biology"))
    pprint(select_4())
    pprint(select_5("Kara Shaffer"))
    pprint(select_6("Group-3"))
    pprint(select_7("Group-3", "Mathematics"))
    pprint(select_8("Kara Shaffer"))
    pprint(select_9("Desiree Hendrix"))
    pprint(select_10("Desiree Hendrix", "Kara Shaffer"))
