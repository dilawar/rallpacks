RMS=rms
SIM=genesis
SRC=scale_cable.g

all: rms 
	$(SIM) $(SRC) 5e-6 1e-3 cable1

rms: rms.c
	cc $< -o $@ -lm

clean:
	rm -rf rms *.out

