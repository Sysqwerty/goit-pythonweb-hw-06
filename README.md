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