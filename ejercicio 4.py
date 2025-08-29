compra = float(input("Ingrese el monto de su compra: "))

if compra > 1000:
        descuento = compra * 0.10
else:
        descuento = 0

print("El descuento aplicado es:", descuento)