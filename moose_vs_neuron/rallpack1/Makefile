PYC=python
MOOSE_SCRIPT=moose_sim.py
NRN_SCRIPT=neuron_sim.py
MOOSE_DATA=data/moose.dat
NEURON_DATA=data/nrn.dat
RUN_TIME=0.25
NUM_COMPT=20000


all: data  compare

compare: compare.py $(MOOSE_DATA) $(NEURON_DATA) 
	@echo "[MAKE] Comparing data"
	$(PYC) $< $(MOOSE_DATA) $(NEURON_DATA)

data: $(MOOSE_DATA) $(NEURON_DATA)
	@echo [MAKE] Finished generating data.
	@echo "Check *.log file for time taken by simulations"

$(MOOSE_DATA): moose_sim.py
	@echo "[MAKE] Running moose on rallpack3"
	time $(PYC) $< --run_time $(RUN_TIME) --ncomp $(NUM_COMPT) --output $@

$(NEURON_DATA): neuron_sim.py passive_cable_template.nrn
	@echo "[MAKE] Running NEURON on rallpack3"
	time $(PYC) $< --run_time $(RUN_TIME) --ncomp $(NUM_COMPT) --data $@

clean:
	rm -f $(MOOSE_DATA) $(NEURON_DATA) 


purge: 
	make clean
	rm -rf *.sqlite *.log
