# Nombre: Programa para obtener si es mayor o menor de edad 

# Entrada:
# Edad digitada 

# Salida:
# Identificar si el usuario es mayor o menor de edad

# Proceso: Pedir la edad y extraer si es mayor o menor de edad

# Pedir edad 
edad = int(input("Ingrese su edad: "))

# Mostrar el resultado
if edad >= 18:
        print("Usted es mayor de edad")
else:
        print("Usted es menor de edad")