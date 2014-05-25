NRN=nrniv -nogui -nobanner
NRN_SRC=$(wildcard *.hoc)
LOGFILE="__neuron__.dat"
OUT_FILES=$(NRN_SRC:.hoc=.out)
    
all: ${OUT_FILES}

%.out: %.hoc
	${NRN} $< 

	

clean:
	rm -rf *.out
