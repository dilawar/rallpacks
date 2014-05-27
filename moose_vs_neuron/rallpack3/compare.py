#!/usr/bin/env python

"""compare.py: Compare data generated by MOOSE and NEURON.

Last modified: Sat Jan 18, 2014  05:01PM

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2013, NCBS Bangalore"
__credits__          = ["NCBS Bangalore", "Bhalla Lab"]
__license__          = "GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@iitb.ac.in"
__status__           = "Development"

import os
import sys
from collections import defaultdict
import pylab

def compare(mooseData, nrnData, outputFile = None):
    """Compare two data-vectors """
    mooseX, mooseY = mooseData
    nrnX, nrnY = nrnData
    mooseX = [ x*1e3 for x in mooseX ]
    for v in mooseY:
        mooseY[v] = [ 1e3*y for y in mooseY[v]]
    for i, v in enumerate( mooseY ):
        pylab.plot(mooseX, mooseY.values()[i])
        pylab.plot(nrnX, nrnY.values()[i])
        if outputFile is None:
            pylab.show()
        else:
            outputFile = "{}{}.png".format(outputFile, i)
            print("[INFO] Dumping plot to {}".format(outputFile))
            pylab.savefig(outputFile)

def txtToData(txt):
    """Convert text to data"""
    vecX = []
    vecY = defaultdict(list)
    for line in txt.split("\n"):
        line = line.strip()
        values = line.split()
        if not values:
            continue
        vecX.append(float(values[0].strip()))
        for i, v in enumerate(values[1:]):
            v = v.strip()
            vecY[i].append(float(v))
    return vecX, vecY

def main():
    print("[INFO] Second file will be scaled by a factor of 1e3")
    mooseFile = sys.argv[1]
    nrnFile = sys.argv[2]
    if len(sys.argv) > 3:
        outputFile = sys.argv[3]

    with open(mooseFile, "r") as f:
        mooseData = txtToData(f.read())
    with open(nrnFile, "r") as f:
        nrnData = txtToData(f.read())
    compare(mooseData, nrnData, outputFile)

if __name__ == '__main__':
    main()
