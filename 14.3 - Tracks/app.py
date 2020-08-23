import xml.etree.ElementTree as ET
import sqlite3

db_connection = sqlite3.connect('database.sqlite')
db_cursor = db_connection.cursor()

# Make some fresh tables using executescript()
db_cursor.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(x_dict, key):
    key_value_pairs = zip(x_dict[::2], x_dict[1::2])
    for x_key, x_value in key_value_pairs:
        if x_key.text == key :
            return x_value.text
    return None

xml_data = ET.parse(file_handle).findall('dict/dict/dict')
print('Dict count:', len(xml_data))
for entry in xml_data:
    if lookup(entry, 'Track ID') is None: 
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or genre is None or album is None : 
        continue

    print(name, artist, album, count, rating, length)

    db_cursor.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', (artist, ) )
    db_cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ) )
    artist_id = db_cursor.fetchone()[0]

    db_cursor.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )', (genre, ) )
    db_cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ) )
    genre_id = db_cursor.fetchone()[0]

    db_cursor.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', (album, artist_id) )
    db_cursor.execute('SELECT id FROM Album WHERE title = ? ', (album, ) )
    album_id = db_cursor.fetchone()[0]

    db_cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    db_connection.commit()
