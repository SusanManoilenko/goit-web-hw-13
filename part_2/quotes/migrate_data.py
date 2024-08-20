import pymongo
import psycopg2
from psycopg2.extras import execute_values

# Підключення до MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["Cluster0"]
authors_collection = mongo_db["authors"]
quotes_collection = mongo_db["quotes"]

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="django",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    options="-c client_encoding=UTF8"
)
cursor = conn.cursor()

# Перенесення авторів
authors = list(authors_collection.find())
author_values = [(author['name'], author['bio']) for author in authors]
execute_values(cursor, "INSERT INTO quotes_author (name, bio) VALUES %s", author_values)
conn.commit()

# Перенесення цитат
quotes = list(quotes_collection.find())
quote_values = [(quote['text'], quote['author']) for quote in quotes]
execute_values(cursor, "INSERT INTO quotes_quote (text, author_id) VALUES %s", quote_values)
conn.commit()

cursor.close()
conn.close()