print("Introduce un número: ")
numero = int( input("Num: "))
while numero > 0 :
    suma = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            suma += i
            
    print("La suma de los divisores del numero es: ", suma)
            
    print("Para salir ingresar un numero negativo")
    numero = int( input("Num: "))