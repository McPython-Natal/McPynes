#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
print('Isso pode demorar um pouco...')
a = str(2 ** 1000000)
b = len(a)
print ('2 elevado a 1 milhão tem', b, 'dígitos')
