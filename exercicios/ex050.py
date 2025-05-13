s = 0  

print("Digite 6 números inteiros:")
for i in range(6):  
    n= int(input(f"Número {i + 1}: ")) 
    if n % 2 == 0: 
        s += n
        
print(f"A soma dos números pares digitados é: {s}")