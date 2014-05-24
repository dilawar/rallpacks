CC=cc
CFLAGS=-Wall -Werror
TARGETS = rms srms scaler filesplit

all: ${TARGETS}

rms: rms.c
	${CC} ${CFLAGS} $< -o $@ -lm

srms: simplerms.c
	${CC} ${CFLAGS} $< -o $@ -lm

scaler: scaler.c
	${CC} ${CFLAGS} $< -o $@

filesplit: filesplit.c
	${CC} ${CFLAGS} $< -o $@

clean:
	rm -rf $(TARGETS)

