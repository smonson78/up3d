CC=gcc
CFLAGS=-Wall -I../common
LDFLAGS=
TARGETS=upinfo upshell upload

all: $(TARGETS)

upinfo: upinfo.c ../common/up3d.c ../common/up3dcomm.c ../common/up3ddata.c -lm -lusb-1.0

upshell: upshell.c ../common/up3d.c ../common/up3dcomm.c ../common/up3ddata.c -lm -lusb-1.0 -lncurses

upload: upload.c ../common/up3d.c ../common/up3dcomm.c ../common/up3ddata.c -lm -lusb-1.0

clean:
	$(RM) $(TARGETS) *.o