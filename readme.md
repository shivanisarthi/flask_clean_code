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

Run

```shell
$ pip install -r requirements.txt
$ set FLASK_APP=run.py
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

to configure the tests, you need to set the DATABASE_URL manually, which is in `src/main/config/config_by_name.py`, find the TestingConfig class and set SQLALCHEMY_DATABASE_URI

```shell
# src/main/config/config_by_name.py
SQLALCHEMY_DATABASE_URI = "postgresql://testing:1234@localhost/flask"
```

Then run

```shell
$ pytest
```

> **Server**

Just run

```shell
$ flask run
```

Architecture Design [whimsical](https://whimsical.com/flask-cleancode-7oCzG2cZKzQmo4eyTpwfVb)
