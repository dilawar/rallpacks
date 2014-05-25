NRN=nrniv -nogui
NRN_SRC=$(wildcard *.hoc)
OUT_FILES=$(NRN_SRC:.hoc=.out)
    
all: ${OUT_FILES}

%.out: %.hoc
	time ${NRN} $< 

clean:
	rm -rf *.out
