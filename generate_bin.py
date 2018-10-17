#!/usr/bin/python3
# -*- coding: utf-8 -*-

def gen_bin(M, prefix=""):
	if M == 0:
		print(prefix)
		return
	gen_bin(M-1, prefix+"0")
	gen_bin(M-1, prefix+"1")
	gen_bin(M-1, prefix+"2")
	gen_bin(M-1, prefix+"3")
	gen_bin(M-1, prefix+"4")
	gen_bin(M-1, prefix+"5")
	gen_bin(M-1, prefix+"6")
	gen_bin(M-1, prefix+"7")
	gen_bin(M-1, prefix+"8")
	gen_bin(M-1, prefix+"9")

gen_bin(4)

