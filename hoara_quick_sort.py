#!/usr/bin/python3
# -*- coding: utf-8 -*-

def merge(A:list, B:list):
	""" Слияние двух отсортированных массивов
	"""
	C = [0]*(len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return 

def hoar_sort(A):
	if len(A) <= 1:
		return
	barrier = A[0]
	L = []
	M = []
	R = []
	for x in A:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else:
			R.append(x)
	hoar_sort(L)
	hoar_sort(R)
	k = 0
	for x in L + M + R:
		A[k] = x
		k += 1

