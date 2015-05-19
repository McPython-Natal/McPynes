#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
d = int(input('Informe a quantidade de dias: '))
h = int(input('Informe a quantidade de horas: '))
m = int(input('Informe a quantidade de minutos: '))
s = int(input('Informe a quantidade de segundos: '))
d = d * 87840
h = h * 3660
m = m * 60
total = d + h + m + s
print ('Total de segundos:', total)
