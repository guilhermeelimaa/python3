a = int(input('Digite um valor:'))
b = int(input('Digite um valor:')) 
c = int(input('Digite um valor:')) 


# Verificando qual número é o MENOR
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


# Verificando qual número é o MAIOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O MENOR valor digitado foi {}'.format(menor))
print('O MAIOR valor digitado foi {}'.format(maior))