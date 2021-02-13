CC=gcc
CFLAGS=-Wall -I../common
LDFLAGS=
TARGETS=parse convg
all: $(TARGETS)

parse: parse.c -lm
convg: convg.c -lm

clean:
	$(RM) $(TARGETS) *.o