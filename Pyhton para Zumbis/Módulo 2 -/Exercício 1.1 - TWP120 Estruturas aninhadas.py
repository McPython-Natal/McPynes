minutos = int(input('Informe a quantidade de minutos: '))
if minutos < 200:
	valor = minutos * 0.2
else: 
	if minutos <= 400: 
		valor = minutos * 0.18 
	else:
		if minutos <= 800:
			valor = minutos * 0.15
		else:
			valor = minutos * 0.08
print ('Conta de telefone: R$ %.2f' %valor)