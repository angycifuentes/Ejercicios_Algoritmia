# Nombre: Programa para obtener si es numero par o impar

# Entrada:
# Numero digitado

# Salida: 
#Identificar si el numero es par o impar 

# Proceso: Pedir numero y identificar si es par o impar 

# Pedir numero
numero = int(input("Ingrese un número: "))

# Mostrar resultado
if numero % 2 == 0:
        print("El número es par")
else:
        print("El número es impar")