"""
SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
"""

import sqlite3
import json


conn = sqlite3.connect("dataset/rosterdb.sqlite")
curr = conn.cursor()

curr.executescript("""
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;
    CREATE TABLE User(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name TEXT
    );
    CREATE TABLE Course(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        title TEXT
    );
    CREATE TABLE Member(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        role INTEGER,
        user_id INTEGER,
        course_id INTEGER
);
""")

fname = input("Enter file name: ")

try:
    assert len(fname) > 1, "Please enter valid file name next time"
except AssertionError as e:
    print(e)
    fname = "dataset/roster_data.json"

str_data = open(fname).read()
data   = json.loads(str_data)

for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    curr.execute("""INSERT OR IGNORE INTO User(name)
    VALUES( ? )
    """, ( name ,) )
    curr.execute("SELECT id FROM User WHERE name = ?", (name, ) )
    user_id = curr.fetchone()[0]

    curr.execute("""INSERT OR IGNORE INTO Course(title)
    VALUES( ? )""", (title, ))
    curr.execute("SELECT id FROM Course WHERE title = ?", (title, ))
    course_id = curr.fetchone()[0]

    curr.execute("""INSERT OR REPLACE INTO Member(role, user_id, course_id)
    VALUES( ?, ? , ?)""", (role , user_id, course_id, ))

    conn.commit()

curr.execute("""
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
""")

for row in curr.fetchall():
    print(row)


conn.close()