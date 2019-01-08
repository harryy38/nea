import sqlite3 as sql

con = sql.connect("database.db")
cur = con.cursor()
cur.execute("""
drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);""")
con.commit()
con.close()
