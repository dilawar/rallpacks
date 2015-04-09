#!/usr/bin/env python

"""compare.py: Compare data generated by MOOSE and NEURON.

Last modified: Wed Apr 08, 2015  09:55PM

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
import numpy as np
from scipy import ndimage

EPSILON = 1e-10

def findMaxima(y, x, filters=[], **kwargs):
    """Find the location of peaks in data 
    
    If type of peak is cap then 
    
    """
    maximas = []
    index = []
    for i, a in enumerate(y[1:-1]):
        if a >= y[i] and a > y[i+2]:
            # Check if point satisfies addtional condition.
            insert = True
            for f in filters:
                if not f(a):
                    insert = False
                    break
            if insert:
                maximas.append(a)
                index.append(x[i+1])
    return np.array(index), np.array(maximas)

def findMinima(y, x, filters=[], **kwargs):
    """Find all minimas on the curve 
    """
    minimas = []
    index = []
    for i, a in enumerate(y[1:-1]):
        if a <= y[i] and a < y[i+2]:
            # Check if point satisfies addtional condition.
            insert = True
            for f in filters:
                if not f(a):
                    insert = False
                    break
            if insert:
                minimas.append(a)
                index.append(x[i+1])
    return np.array(index), np.array(minimas)

def drawPlots(plots, labels = [], figName = None, **kwargs):
    """Saving plots to a file 
    """
    ps = []
    pylab.figure()
    for x, y in plots:
        p, = pylab.plot(x, y)
        ps.append(p)
    if figName is None:
        return
    print("[PLOT] Saving plot to {}".format(figName))
    pylab.savefig(figName)

def compareData(x1, y1, x2, y2, **kwargs):
    """
    """
    # First compare that there x-axis are same. else report warning.
    x1 = np.array(x1)
    x2 = np.array(x2)
    y1 = np.array(y1)
    y2 = np.array(y2)
    print("[INFO] Plotting")
    p1, = pylab.plot(x1, y1)
    p2, = pylab.plot(x2, y2)
    pylab.legend([p1, p2], ["MOOSE", "NEURON"])

    outfile = kwargs.get('outfile', None)
    if not outfile:
        pylab.show()
    else:
        mu.info("Saving figure to %s" % outfile)
        pylab.savefig(outfile)
    
    if len(y1) > len(y2): y1 = ndimage.zoom(y1, len(y1)/len(y2))
    else: y2 = ndimage.zoom(y2, len(y2)/len(y1))
    diff = y1 - y2
    linDiff = diff.sum()
    rms = np.zeros(len(diff))
    for i, d in enumerate(diff):
        rms[i] = d**2.0
    rms = rms.sum() ** 0.5
    print(" |- RMS diff is: {}".format(rms))

def sanitizeTuples(tuple1, tuple2):
    """Fix the lengths of tuples. 
    
    These tuples contain data of an event. If one needs to compare these events,
    one has to make sure that we are not comparing different no of events.
    
    Experience has it that in ActionPotential, the bad data about maxima and
    minima is in the first pulse. So we remove the data at the begining of the
    array. 
    
    """
    print("[WARN] This is a customized function for comparing maxima and minima")
    print("       Dont use it on generic data.")

    x1, y1 = tuple1
    x2, y2 = tuple2

    assert len(x1) == len(y1), "Length mismatch"
    assert len(x2) == len(y2), "Length mismatch"

    if len(y1) > len(y2):
        y1 = y1[-len(y2):]
        x1 = x1[-len(x2):]
    elif len(y2) > len(y1):
        y2 = y2[-len(y1):]
        x2 = x2[-len(x1):]
    return (x1, y1), (x2, y2)


def compare(mooseData, nrnData, outputFile = None):
    """Compare two data-vectors """
    mooseX, mooseY = mooseData
    nrnX, nrnY = nrnData
    mooseX = [ x * 1e3 for x in mooseX ]
    for v in mooseY:
        mooseY[v] = [ 1e3 * y for y in mooseY[v] ]
    for i, v in enumerate(mooseY):
        compareData(mooseX, mooseY.values()[i], nrnX, nrnY.values()[i])

def txtToData(txt):
    """Convert text to data"""
    vecX = []
    vecY = defaultdict(list)
    for line in txt.split("\n"):
        line = line.strip()
        line = line.replace(' ', ',')
        values = line.split(",")
        if not values:
            continue
        try:vecX.append(float(values[0].strip()))
        except:pass
        for i, v in enumerate(values[1:]):
            v = v.strip()
            try: vecY[i].append(float(v))
            except: pass
    return vecX, vecY

def main():
    print("[INFO] Second file will be scaled by a factor of 1e3")
    mooseFile = sys.argv[1]
    nrnFile = sys.argv[2]
    outputFile = None
    if len(sys.argv) > 3:
        outputFile = sys.argv[3]

    with open(mooseFile, "r") as f:
        mooseData = txtToData(f.read())
    with open(nrnFile, "r") as f:
        nrnData = txtToData(f.read())

    print("[INFO] Comparing MOOSE and NEURON data")
    compare(mooseData, nrnData, outputFile)

if __name__ == '__main__':
    print("[WARN] Must not be used on generic data. You have been warned")
    main()
