CC=gcc
CFLAGS=-Wall -I../common
LDFLAGS=
TARGETS=upinfo upshell upload

all: $(TARGETS)

upinfo: upinfo.c ../common/up3d.o ../common/up3dcomm.o ../common/up3ddata.o -lm -lusb-1.0

upshell: upshell.c ../common/up3d.o ../common/up3dcomm.o ../common/up3ddata.o -lm -lusb-1.0 -lncurses

upload: upload.c ../common/up3d.o ../common/up3dcomm.o ../common/up3ddata.o -lm -lusb-1.0

clean:
	$(RM) $(TARGETS) *.o