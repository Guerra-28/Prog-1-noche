valorNeto = int(input("ingrese el valor"))
#iva = int(input("Ingrese el iva"))
valorTotal = valorNeto * 1.19
valorCompra = valorTotal - (valorTotal * 0.05)
print(valorCompra)