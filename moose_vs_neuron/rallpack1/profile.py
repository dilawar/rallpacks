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
tableName = 'rallpack1'

cur_.execute(
        """CREATE TABLE IF NOT EXISTS {} ( time DATETIME 
        , no_of_compartment INTEGER 
        , whichrun INTEGER PRIMARY KEY ASC 
        , moosecore REAL DEFAULT -1
        , pymoose REAL DEFAULT -1
        , neuron REAL DEFAULT -1
        , moose_comment TEXT
        , neuron_comment TEXT
        )""".format(tableName)
        )

def insert(values):
    cur_.execute("""SELECT MAX(whichrun) FROM %s"""%tableName)
    whichrun = cur_.fetchone()[0]
    print whichrun
    if whichrun is None:
        whichrun = 0
    else: whichrun += 1
    cur_.execute("INSERT OR IGNORE INTO {} (whichrun) VALUES ('{}')".format(
        tableName, whichrun
        ))
    stmt = []
    for k in values: stmt.append("%s='%s'"%(k, values[k]))
    stmt.append("time=datetime('now')")
    stmt = ",".join(stmt)
    query = "UPDATE {} SET {} WHERE whichrun='{}'".format(tableName, stmt, whichrun)
    print("Excuting: %s" % query)
    cur_.execute(query)
    conn_.commit()

def main():
    insert({ 'no_of_compartment': 100, 'moosecore' : 0.0001 })
    for c in cur_.execute("SELECT * from %s"%tableName):
        print c

if __name__ == '__main__':
    main()
