from enum import Enum

from sqlalchemy import select, func
from connect import session
from models import Student, Score, Subject, Group, Teacher
from sqlalchemy import cast, Float


# Зробити наступні вибірки з отриманої бази даних:
# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
# Знайти студента із найвищим середнім балом з певного предмета.
# Знайти середній бал у групах з певного предмета.
# Знайти середній бал на потоці(по всій таблиці оцінок).
# Знайти які курси читає певний викладач.
# Знайти список студентів у певній групі.
# Знайти оцінки студентів у окремій групі з певного предмета.
# Знайти середній бал, який ставить певний викладач зі своїх предметів.
# Знайти список курсів, які відвідує певний студент. Список курсів, які певному студенту читає певний викладач.

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
    return result


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
    return result


if __name__ == "__main__":
    # print(select_1())
    # custom_subjects = ["Mathematics", "Physics", "Biology", "Chemistry", "History"]
    print(select_2("Physics"))
