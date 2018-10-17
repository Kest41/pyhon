#!/usr/bin/python3
# -*- coding: utf-8 -*-

def gen_bin(M, prefix=""):
	if M == 0:
		print(prefix)
		return
	for digit in "0", "1":
		gen_bin(M-1, prefix+digit)

gen_bin(3)

