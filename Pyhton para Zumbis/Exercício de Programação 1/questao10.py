#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
a = int(input('Informe quantos cigarros você fuma por dia: '))
b = int(input('Informe por quantos anos(arredonde o valor) você já fumou: '))

dias = b * 365
cigas = a * dias
#10 minutos igual a 600 segundos

perdido = cigas * 600
perddias = int(perdido / 87840)

print('Você fumou', cigas, 'cigarros e com isto perdeu um pouco mais de', perddias, 'dias de vida')
