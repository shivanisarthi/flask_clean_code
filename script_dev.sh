pip install -r requirements.txt
HOST_DB="localhost"
USER_DB="JohnDoe"
PASSWORD_DB="1234"
DATABASE="flask_database"
flask db upgrade
pytest
cd src/
flask run
python setup.py bdist_wheel
cd build/lib/src
env:DATABASE_URL = "postgresql://${USER_DB}:${PASSWORD_DB}@${HOST_DB}/${DATABASE}"
waitress-serve --call 'run:create_app'

