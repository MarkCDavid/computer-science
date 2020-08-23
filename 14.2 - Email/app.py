import sqlite3
import re

db_connection = sqlite3.connect('database.sqlite')
db_cursor = db_connection.cursor()

db_cursor.execute('DROP TABLE IF EXISTS Counts')

db_cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()

for org in re.findall("^From:.*?@(\S+)", file_handle.read(), flags=re.MULTILINE):
    db_cursor.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        db_cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    db_connection.commit()

result_sql = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in db_cursor.execute(result_sql):
    print(str(row[0]), row[1])

db_cursor.close()