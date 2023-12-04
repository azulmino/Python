#FOR y WHILE
print("Introduce un numero: ")
num = int( input())

while num > 0 :
    resto = num % 10
    print(resto)
    
    nim = num // 10
