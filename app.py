import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT,
    year INTEGER,
    rating FLOAT
)
''')


conn.commit()


movies = [
    ('The Shawshank Redemption', 'Frank Darabont', 1994, 9.3),
    ('Inception', 'Christopher Nolan', 2010, 8.8),
    ('The Matrix', 'Lana and Lilly Wachowski', 1999, 8.7),
    ('Interstellar', 'Christopher Nolan', 2014, 8.6)
]

cursor.executemany('''
INSERT INTO movies (title, director, year, rating)
VALUES (?, ?, ?, ?)
''', movies)


conn.commit()


cursor.execute('SELECT * FROM movies')
all_movies = cursor.fetchall()
print("All movies:")
for movies in all_movies:
    print(movies)

conn.commit()
conn.close()