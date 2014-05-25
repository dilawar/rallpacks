NRN=nrniv -nogui -nobanner
NRN_SRC=$(wildcard *.hoc)
LOGFILE="__neuron__.dat"
OUT_FILES=$(NRN_SRC:.hoc=.out)
    
all: ${OUT_FILES}

%.out: %.hoc
	T1=$(shell date +%s%N)
	${NRN} $< 
	T2=$(shell date +%s%N)
	timeTaken=$(shell echo $(T1)-$(T2) | bc)

	

clean:
	rm -rf *.out
