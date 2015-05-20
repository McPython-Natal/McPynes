velo = int(input("Digite a velocidade: "))
if velo > 110:
	excesso = velo - 110
	multa = excesso * 5
	print ("Você irá pagar R$ %.2f de multa por excesso de velocidade!" %multa)
if velo <= 110:
	print ("Parabéns! Você está dentro do limite de velocidade.")