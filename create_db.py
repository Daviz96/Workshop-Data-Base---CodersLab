from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateTable

DB_USER = "postgres"
DB_HOST = "localhost"
DB_PASSWORD = "postgres"
CREATE_DATABASE = 'CREATE DATABASE workshop_db'

CREATE_USERS_TABLE = '''CREATE TABLE users(
id serial primary key,
user_name varchar(255) unique,
hashed_password varchar(255));'''

CREATE_MESSAGES_TABLE = '''CREATE TABLE messages(
id serial primary key,
from_id integer references users(id) on delete cascade,
to_id integer references users(id) on delete cascade,
creation_date timestamp default current_timestamp,
text varchar(255));'''

try:
    cnx = connect(user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DATABASE)
    except DuplicateDatabase:
        print("Database already exist")

    cnx.close()
except OperationalError as e:
    print(e)



try:
    cnx = connect(user=DB_USER, host=DB_HOST, password=DB_PASSWORD, dbname = workshop_db)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_USERS_TABLE)
        print('CREATED TABLE users')
    except DuplicateTable as e:
        print(e)
    try:
        cursor.execute(CREATE_MESSAGES_TABLE)
        print('CREATED TABLE messages')
    except DuplicateTable as e:
        print(e)
    cnx.close()
except OperationalError as e:
    print(e)
