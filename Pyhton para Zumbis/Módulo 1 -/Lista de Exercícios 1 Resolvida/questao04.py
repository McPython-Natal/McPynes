#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
a = input('Informe o salário: ')
a = float(a)
b = input('Informe a porcentagem do aumento: ')
b = float(b)
aumento = (a * (b/100))
total = a + aumento
print ('Valor do aumento:', aumento)
print ('Valor do novo salário:', total)
