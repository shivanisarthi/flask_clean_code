# Clean architecture with flask

[![Build Status](https://app.travis-ci.com/vineboneto/flask_clean_code.svg?branch=main)](https://app.travis-ci.com/vineboneto/flask_clean_code)

Clean architecture object oriented using flask

#### Design Patterns & Methodologies

-   Clean Architecture
-   DDD
-   Adapter
-   Factory
-   Composition
-   Heritage
-   Refactoring
-   Dependency Injection
-   Singleton

---

## Environment

-   Windows 10 PRO
-   Python 3.9.6
-   PostgreSQL 13.2

## Settings

> **Flask**

```shell
$ pip install -r requirements.txt
```

> **Database**

I'm use postgres.

-   Setting .env in root dir with your data

```shell
# .env
HOST_DB="localhost"
USER_DB="JohnDoe"
PASSWORD_DB="1234"
DATABASE="flask_database"
```

-   Upgrade your database with migrations

```shell
$ flask db upgrade
```

> **Testing**

Just run

```shell
$ pytest
```

> **Server**

Just run

```shell
# Developer
cd src/
$ flask run

#Production
cd src/
waitress-serve --call 'run:create_app'
```

> **Deploy**

```shell
# Build
$ python setup.py bdist_wheel

# Open src build
$ cd build/lib/src

# set env
$env:DATABASE_URL = "postgresql://${USER_DB}:${PASSWORD_DB}@${HOST_DB}/${DATABASE}"

# start server
waitress-serve --call 'run:create_app'
```

Architecture Design [whimsical](https://whimsical.com/flask-cleancode-7oCzG2cZKzQmo4eyTpwfVb)

### More

-   [FlaskConfig](https://flask.palletsprojects.com/en/2.0.x/config/)
-   [FlaskDeploy](https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/)
-   [FlaskSetupTools](https://flask.palletsprojects.com/en/2.0.x/patterns/distribute/)
