import urlparse
import os
import psycopg2
result = urlparse.urlparse(os.environ['DATABASE_URL'])
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
connection = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname
)

cursor = connection.cursor()
cursor.execute('select * from wind')
print cursor.fetchall()

connection.close()