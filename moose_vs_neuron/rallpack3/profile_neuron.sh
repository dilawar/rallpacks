#!/usr/bin/env bash
echo "Profiling neuron simulator of rallpack3"
ncomp=10
while [ $ncomp -lt 50000 ]; do
    echo "Cable with compartment $ncomp"
    python ./neuron_sim.py --ncomp $ncomp --data L$ncomp.out 
    ncomp=$(echo $ncomp+50 | bc)
done
