CC=gcc
CFLAGS=-Wall -I../common
LDFLAGS=
TARGETS=up3dtranscode
all: $(TARGETS)

up3dtranscode: up3dtranscode.c up3dconf.c hoststepper.c hostplanner.c gcodeparser.c umcwriter.c ../common/up3ddata.c -lm

clean:
	$(RM) $(TARGETS) *.o