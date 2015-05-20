#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
a = input('Informe o preço da mercadoria: ')
a = float(a)
b = input('Informe o percentual de desconto: ')
b = float(b)
desconto = a * (b/100)
total = a - desconto
print ('Valor do desconto:', desconto)
print ('Valor a pagar', total)
