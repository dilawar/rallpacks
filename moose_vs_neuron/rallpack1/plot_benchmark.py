"""plot_benchmark.py: 

    Plot the benchmarks.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import profile
import pylab
import sqlite3 as sql
from collections import defaultdict

benchmark = defaultdict(list)

dbFile = profile.dbFile
tableName = profile.tableName



def plotBenchmark():
    db = sql.connect(dbFile)
    cur = db.cursor()
    for sim in ['moose', 'neuron']:
        query = """SELECT coretime, no_of_compartment FROM {} WHERE
        simulator='{}'""".format(tableName, sim)
        for c in cur.execute(query):
            benchmark[sim].append(c)
    for k in benchmark:
        vals = benchmark[k]
        time, compt = zip(*vals)
        pylab.plot(compt, time, '.', label=k)
        pylab.legend(loc='best', framealpha=0.4)
        pylab.xlabel("No of compartment in rallpack1")
        pylab.ylabel("Time taken (sec)")
    pylab.show()

def main():
    plotBenchmark()


if __name__ == '__main__':
    main()
