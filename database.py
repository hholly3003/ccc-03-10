#this file is specifically about connecting to our databse and well setup
import psycopg2
import os

#connection setup to the database -- currently setup to the ec2 instance
connection = psycopg2.connect(
    database="library_api",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="54.66.144.62",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()