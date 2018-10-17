def generate_permitations(N:int, M:int=-1, prefix=None):
	""" Генерация всех перестановок N чисел в M позициях,
		с префиксом prefix
	"""
	M = N if M == -1 else M # по умолчанию N чисел в N позициях
	preix = prefix or [0]
	if M == 0:
		print(prefix)
		return
	for number in range(1, N+1):
