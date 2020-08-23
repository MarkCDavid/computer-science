import json
import sqlite3

db_connection = sqlite3.connect('database.sqlite')
db_cursor = db_connection.cursor()

db_cursor.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')


filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()

json_data = json.loads(file_handle.read())

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title))

    db_cursor.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', ( name, ) )
    db_cursor.execute('SELECT id FROM User WHERE name = ? ', (name, ) )
    user_id = db_cursor.fetchone()[0]

    db_cursor.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', ( title, ) )
    db_cursor.execute('SELECT id FROM Course WHERE title = ? ', (title, ) )
    course_id = db_cursor.fetchone()[0]

    db_cursor.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role) )

    db_connection.commit()