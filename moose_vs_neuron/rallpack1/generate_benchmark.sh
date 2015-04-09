#!/bin/bash
# This script generates benchamark.
set -x
set -e
echo "Run each benchmark 5 times"
for i in `seq 500 500 35000`
do
    for j in `seq 1 1 5` do
        python moose_sim.py --run_time 0.25 --ncomp $i
        python neuron_sim.py --run_time 0.25 --ncomp $i
    done
done
