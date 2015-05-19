#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
#A formula de conversão esta errada, a certa é F = C * 1.8 + 32
a = input('Informe a temperatura em Celsius: ')
a = float(a)
f = a * 1.8 + 32
print (a,'º C em Fahrenheit é: %.2f' %f)
