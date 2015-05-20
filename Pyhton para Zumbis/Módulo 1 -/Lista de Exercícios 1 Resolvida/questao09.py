#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
a = input('Informe a quantidade de km percorridos com o carro: ')
a = float(a)
b = int(input('Informe a quantidade de dias em que o carro foi alugado: '))

pdia = b * 60
pkm = a * 0.15

total = pdia + pkm

print('Valor total a pagar:', total)
