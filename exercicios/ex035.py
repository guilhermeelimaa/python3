print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
s1 = float(input('Digite o valor de um segmento: '))
s2 = float(input('Digite o valor de um segmento: '))
s3 = float(input('Digite o valor de um segmento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')