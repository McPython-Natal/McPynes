numero = int(input('Digite um número: '))
x = 1
while x <= numero:
	if x % 2 != 0:
		print (x)
	x = x + 1

print ('Imprimindo os 10 primeiros múltiplos de 3')
z = 1
while z <= 10:
	print (z * 3)
	z = z + 1

b = 1
soma = 0
while b <= 10:
	a = int(input('Digite o %dº numero: ' %b))
	soma = soma + a
	b = b + 1
print ('Média: ', soma / 10)
