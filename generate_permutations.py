#!/usr/bin/python3
# -*- coding: utf-8 -*-

def find(number, A):
	""" Ищет number в A и возвращает true, если такой есть,
		False, если такого нет
	"""
	flag = False
	for x in A:
		if number == x:
			flag = True
	return flag

def generate_permutations(N:int, M:int=-1, prefix=None):
	""" Генерация всех перестановок N чисел в M позициях,
		с префиксом prefix
	"""
	M = N if M == -1 else M # по умолчанию N чисел в N позициях
	preix = prefix or [0]
	if M == 0:
		print(prefix)
		return
	for number in range(1, N+1):
		if find(number, prefix): prefix:
			continue
		prefix.append(number)
		generate_permutations(N, M-1, prefix)
		prefix.pop()
