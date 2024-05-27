precios_productos = {
    "manzanas": 2.5,
    "lavadora": 1.8,
    "celular": 3.0,
    "nevera": 2.0,
    "moto": 4.0
}

# Pedimos al usuario el producto y la cantidad
producto = input("Ingrese el nombre del producto: ").lower()
cantidad = int(input("Ingrese la cantidad de productos: "))

# Verificamos si el producto está en el diccionario
if producto in precios_productos:
    precio_total = precios_productos[producto] * cantidad
    print(f"El precio total de {cantidad} {producto} es: {precio_total}")
else:
    print("El producto no está en el diccionario de precios.")