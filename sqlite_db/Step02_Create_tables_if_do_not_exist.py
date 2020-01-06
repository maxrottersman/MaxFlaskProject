#import sqlite3
# For cross-db table definitions
from sqlalchemy import create_engine
# Also see: https://www.pythonsheets.com/notes/python-sqlalchemy.html#inspect-get-database-information
from sqlalchemy import inspect
# To work with files on any OS
from pathlib import Path

# assume script in root of our project
ScriptPath = Path.cwd()
# assume our database in folder /sqlite_db
dbPath = ScriptPath / 'sqlite_db'
# get system neutral (win/unix) path and convert to string
dbPathandFile = dbPath / 'DB.sqlite'

db_uri = r'sqlite:///' + str(dbPathandFile)

#db_uri = "sqlite:///db.sqlite"
engine = create_engine(db_uri)

# DBAPI - PEP249
# create table
if not engine.has_table('Funds'):
    engine.execute('CREATE TABLE "Funds" ('
                'id INTEGER NOT NULL,'
                'name VARCHAR, '
                'PRIMARY KEY (id));')

if not engine.has_table('FundData'):
    engine.execute('CREATE TABLE "FundData" ('
                'id INTEGER NOT NULL,'
                'name VARCHAR,'
                'fees NUMERIC, '
                'PRIMARY KEY (id));')

inspector = inspect(engine)

# Get table information
print(inspector.get_table_names())
   
