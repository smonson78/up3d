#!/usr/bin/python

import sys

dummy = bytearray([3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

infile = open(sys.argv[1], "rb")
outfile = open("dump.umc", "wb")
state = "default"
for line in infile:
  line = line.strip().split("\t")
  if len(line) > 2:
    line_data = [int(x, 16) for x in line[2].split(":")]
  else:
    continue

  if line[0] == "host":
    # Host is sending data
    if line_data[0] == 0x2f:
      # Sending data blocks
      print "data", len(line_data), "bytes"
      bytedata = bytearray(line_data[2:])
      outfile.write(bytedata)

      # This is meant to keep the XY/ZE command (3) in pairs. There's a flag that resets at the beginning of each
      # 0x2f block, and since I'm throwing those groupings away I'm just going to insert a dummy if needed.
      threecount = 0
      pos = 0
      while pos < len(line_data) - 2:
        if line_data[2 + pos] == 3:
          threecount = threecount + 1
        pos = pos + 20

      # If odd number of "6" blocks, pad with a dummy one
      if threecount % 2 == 1:
        outfile.write(dummy)

    elif line_data[0] == 0x46:
      # Requesting the number of free blocks
      print "Free blocks query"
    else:
      print "Stopped at", line[1], "because of command", hex(line_data[0])
      break
  else:
    continue

  #print line[0], line[1], line_data


infile.close()
outfile.close()