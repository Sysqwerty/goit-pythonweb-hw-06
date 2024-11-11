# goit-pythonweb-hw-06

This project allows to run and check DB migration process on example of Postgres DB
which is running on a docker container.

In order to try it out, open the commandline terminal in the root folder of the project and execute:

Download postgres image and run its container

```shell
docker run --name my-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
```

Install all project dependencies

```shell
poetry update
```

Do migration to the last version (in current case create empty tables in DB)

```shell
alembic upgrade head
```

Add test data to the DB

```shell
python seeds.py
```

Run SQL select queries

```shell
python my_select.py
```

Please update names of teachers, subjects, students etc. before running SQL queries because test data is generating each
time new using Faker module.

<details>
  <summary>You should get output like this (click me)</summary>

```
1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
[{'name': 'Max Kidd', 'avg_score': 85.5},
 {'name': 'Dr. James Moyer', 'avg_score': 85.1},
 {'name': 'Madison Green', 'avg_score': 84.5},
 {'name': 'Stephanie Adkins PhD', 'avg_score': 84.45},
 {'name': 'James Meyer', 'avg_score': 84.1}]

2. Знайти студента із найвищим середнім балом з певного предмета 'Physics'.
{'name': 'James Meyer', 'avg_score': 99.0, 'name_1': 'Physics'}

3. Знайти середній бал у групах з певного предмета 'Biology'.
[{'Subject_name': 'Biology', 'Group_name': 'Group-1', 'avg_score': 77.59649122807018},
 {'Subject_name': 'Biology', 'Group_name': 'Group-2', 'avg_score': 81.20289855072464},
 {'Subject_name': 'Biology', 'Group_name': 'Group-3', 'avg_score': 80.95294117647059}]

4. Знайти середній бал на потоці(по всій таблиці оцінок).
{'avg_score': 79.935}

5. Знайти які курси читає певний викладач 'Kara Shaffer'.
[{'Teacher_name': 'Kara Shaffer', 'Subject_name': 'Physics'},
 {'Teacher_name': 'Kara Shaffer', 'Subject_name': 'History'}]

6. Знайти список студентів у певній групі 'Group-3'.
[{'Group_name': 'Group-3', 'Student_name': 'Melanie Deleon'},
 {'Group_name': 'Group-3', 'Student_name': 'Gavin Young'},
 {'Group_name': 'Group-3', 'Student_name': 'Desiree Hendrix'},
 {'Group_name': 'Group-3', 'Student_name': 'Mark Gonzalez'},
 {'Group_name': 'Group-3', 'Student_name': 'Brianna Dillon'},
 {'Group_name': 'Group-3', 'Student_name': 'Bradley Gonzalez'},
 {'Group_name': 'Group-3', 'Student_name': 'John Wagner'},
 {'Group_name': 'Group-3', 'Student_name': 'Paul Rodriguez PhD'},
 {'Group_name': 'Group-3', 'Student_name': 'Dr. James Moyer'},
 {'Group_name': 'Group-3', 'Student_name': 'Mr. David Marsh'},
 {'Group_name': 'Group-3', 'Student_name': 'Julie Harrison'},
 {'Group_name': 'Group-3', 'Student_name': 'Stephanie Adkins PhD'},
 {'Group_name': 'Group-3', 'Student_name': 'Max Kidd'},
 {'Group_name': 'Group-3', 'Student_name': 'Edward Hernandez'},
 {'Group_name': 'Group-3', 'Student_name': 'Kristin Williams'},
 {'Group_name': 'Group-3', 'Student_name': 'Madison Green'},
 {'Group_name': 'Group-3', 'Student_name': 'Jack Taylor'},
 {'Group_name': 'Group-3', 'Student_name': 'James Meyer'}]

7. Знайти оцінки студентів у окремій групі 'Group-3' з певного предмета 'Mathematics'.
[{'Student_name': 'Melanie Deleon', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 61},
 {'Student_name': 'Melanie Deleon', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 81},
 {'Student_name': 'Melanie Deleon', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 95},
 {'Student_name': 'Gavin Young', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 63},
 {'Student_name': 'Gavin Young', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 76},
 {'Student_name': 'Gavin Young', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 80},
 {'Student_name': 'Desiree Hendrix', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 66},
 {'Student_name': 'Desiree Hendrix', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 84},
 {'Student_name': 'Desiree Hendrix', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 82},
 {'Student_name': 'Mark Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 82},
 {'Student_name': 'Mark Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 96},
 {'Student_name': 'Mark Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 82},
 {'Student_name': 'Mark Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 61},
 {'Student_name': 'Bradley Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 81},
 {'Student_name': 'Bradley Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 78},
 {'Student_name': 'Bradley Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 99},
 {'Student_name': 'Bradley Gonzalez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 65},
 {'Student_name': 'John Wagner', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 79},
 {'Student_name': 'John Wagner', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 68},
 {'Student_name': 'John Wagner', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 83},
 {'Student_name': 'Paul Rodriguez PhD', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 94},
 {'Student_name': 'Paul Rodriguez PhD', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 79},
 {'Student_name': 'Paul Rodriguez PhD', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 64},
 {'Student_name': 'Paul Rodriguez PhD', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 85},
 {'Student_name': 'Paul Rodriguez PhD', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 68},
 {'Student_name': 'Dr. James Moyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 88},
 {'Student_name': 'Dr. James Moyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 94},
 {'Student_name': 'Dr. James Moyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 84},
 {'Student_name': 'Dr. James Moyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 62},
 {'Student_name': 'Dr. James Moyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 87},
 {'Student_name': 'Dr. James Moyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 91},
 {'Student_name': 'Mr. David Marsh', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 100},
 {'Student_name': 'Mr. David Marsh', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 91},
 {'Student_name': 'Mr. David Marsh', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 70},
 {'Student_name': 'Julie Harrison', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 92},
 {'Student_name': 'Julie Harrison', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 77},
 {'Student_name': 'Julie Harrison', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 75},
 {'Student_name': 'Stephanie Adkins PhD', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 94},
 {'Student_name': 'Max Kidd', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 86},
 {'Student_name': 'Max Kidd', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 88},
 {'Student_name': 'Max Kidd', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 91},
 {'Student_name': 'Max Kidd', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 100},
 {'Student_name': 'Max Kidd', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 78},
 {'Student_name': 'Max Kidd', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 95},
 {'Student_name': 'Edward Hernandez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 71},
 {'Student_name': 'Edward Hernandez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 81},
 {'Student_name': 'Edward Hernandez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 65},
 {'Student_name': 'Edward Hernandez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 62},
 {'Student_name': 'Edward Hernandez', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 74},
 {'Student_name': 'Kristin Williams', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 66},
 {'Student_name': 'Kristin Williams', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 91},
 {'Student_name': 'Kristin Williams', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 66},
 {'Student_name': 'Kristin Williams', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 68},
 {'Student_name': 'Kristin Williams', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 61},
 {'Student_name': 'Madison Green', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 68},
 {'Student_name': 'Madison Green', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 94},
 {'Student_name': 'Jack Taylor', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 83},
 {'Student_name': 'Jack Taylor', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 60},
 {'Student_name': 'James Meyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 62},
 {'Student_name': 'James Meyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 80},
 {'Student_name': 'James Meyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 99},
 {'Student_name': 'James Meyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 77},
 {'Student_name': 'James Meyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 96},
 {'Student_name': 'James Meyer', 'Group_name': 'Group-3', 'Subject_name': 'Mathematics', 'Score': 98}]

8. Знайти середній бал, який ставить певний викладач 'Kara Shaffer' зі своїх предметів.
[{'Teacher_name': 'Kara Shaffer', 'Subject_name': 'History', 'avg_score': 81.07729468599034},
 {'Teacher_name': 'Kara Shaffer', 'Subject_name': 'Physics', 'avg_score': 80.20304568527919}]

9. Знайти список курсів, які відвідує певний студент 'Desiree Hendrix'.
[{'Student_name': 'Desiree Hendrix', 'Subject_name': 'Biology'},
 {'Student_name': 'Desiree Hendrix', 'Subject_name': 'Chemistry'},
 {'Student_name': 'Desiree Hendrix', 'Subject_name': 'History'},
 {'Student_name': 'Desiree Hendrix', 'Subject_name': 'Mathematics'},
 {'Student_name': 'Desiree Hendrix', 'Subject_name': 'Physics'}]

10. Список курсів, які певному студенту 'Desiree Hendrix' читає певний викладач 'Kara Shaffer'.
[{'Student_name': 'Desiree Hendrix', 'Subject_name': 'History', 'Teacher_name': 'Kara Shaffer'},
 {'Student_name': 'Desiree Hendrix', 'Subject_name': 'Physics', 'Teacher_name': 'Kara Shaffer'}]
```

</details>