"""config.py: 

    Global variables.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sqlite3 as sql 

dbFile = '_profile.sqlite'
conn_ = sql.connect(dbFile)
cur_ = conn_.cursor()

cur_.execute(
        """CREATE TABLE IF NOT EXISTS profile ( time DATETIME 
        , no_of_compartment INTEGER 
        , whichrun INTEGER PRIMARY KEY ASC DEFAULT '0'
        , moosecore REAL DEFAULT -1
        , pymoose REAL DEFAULT -1
        , neuron REAL DEFAULT -1
        , moose_comment TEXT
        , neuron_comment TEXT
        )"""
        )

def insert(values):
    cur_.execute("""SELECT MAX(whichrun) FROM profile""")
    whichrun = cur_.fetchone()[0]
    if not whichrun:
        whichrun = 0
    cur_.execute("INSERT OR IGNORE INTO profile (whichrun) VALUES ('{}')".format(whichrun))
    stmt = []
    for k in values: stmt.append("%s='%s'"%(k, values[k]))
    stmt = ",".join(stmt)
    query = "UPDATE profile SET {} WHERE whichrun='{}'".format(stmt, whichrun)
    print("QUERY: %s" % query)
    cur_.execute(query)
    conn_.commit()

def main():
    insert({ 'no_of_compartment': 100, 'moosecore' : 0.0001 })

if __name__ == '__main__':
    main()
