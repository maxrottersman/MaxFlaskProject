import sqlite3
# To work with files on any OS
from pathlib import Path

# assume script in root of our project
ScriptPath = Path.cwd()
# assume our database in folder /sqlite_db
dbPath = ScriptPath / 'sqlite_db'
# get system neutral (win/unix) path and convert to string
dbPathandFileStr = str(dbPath / 'DB.sqlite')

#print(dbPath)

# if we error, we rollback automatically, else commit!
with sqlite3.connect(dbPathandFileStr) as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchone()
    print('SQLite version:', data)