PYC=python
MOOSE_SCRIPT=moose_sim.py
NRN_SCRIPT=neuron_sim.py
MOOSE_DATA=data/moose.dat
NEURON_DATA=data/nrn.dat
RUN_TIME=1


all: data compare

compare: compare.py ${MOOSE_DATA} ${NEURON_DATA} 
	@echo "[MAKE] Comparing data"
	${PYC} $< ${MOOSE_DATA} ${NEURON_DATA}

data: ${MOOSE_DATA} ${NEURON_DATA}
	@echo [MAKE] Finished generating data.

${MOOSE_DATA}: moose_sim.py
	@echo "[MAKE] Running moose on rallpack3"
	${PYC} $< --run_time ${RUN_TIME} --output $@

${NEURON_DATA}: neuron_sim.py active_cable_template.nrn
	@echo "[MAKE] Running NEURON on rallpack3"
	${PYC} $< --run_time ${RUN_TIME} --data $@

clean:
	rm -f ${MOOSE_DATA} ${NEURON_DATA} 
	rm -rf *.pyc
