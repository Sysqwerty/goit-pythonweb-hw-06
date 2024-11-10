from faker import Faker
from sqlalchemy.orm import Session
from connect import session
from models import Group, Subject, Teacher, Student, Score

faker = Faker()


def seed_database():
    with session as sess:
        sess: Session

        # Create 5 teachers
        teachers = [Teacher(name=faker.name()) for _ in range(5)]
        sess.add_all(teachers)
        sess.commit()

        # Create 5 subjects
        custom_subjects = ["Mathematics", "Physics", "Biology", "Chemistry", "History"]

        subjects = [
            Subject(name=name, teacher_id=faker.random_element(teachers).id)
            for name in custom_subjects
        ]
        sess.add_all(subjects)
        sess.commit()

        # Create 3 groups
        groups = [Group(name=f"Group-{i + 1}") for i in range(3)]
        sess.add_all(groups)
        sess.commit()

        # Create 50 students
        students = []
        for _ in range(50):
            student = Student(name=faker.name())
            group = faker.random_element(groups)
            group.students.append(student)
            students.append(student)

        sess.add_all(students)
        sess.commit()

        # Set 20 scores for each student
        scores = []
        for student in students:
            total_scores = 20
            generated_scores = 0

            while generated_scores < total_scores:
                subject = faker.random_element(subjects)
                score = Score(
                    score=faker.random_int(min=60, max=100),
                    student_id=student.id,
                    subject_id=subject.id,
                    created=faker.date_time_this_year()
                )
                scores.append(score)
                generated_scores += 1

        sess.add_all(scores)
        sess.commit()

        print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
