carrito = {}

while True:
    articulo = input("Ingrese el nombre del artículo (o 'pagar' para finalizar la compra): ")
    if articulo.lower() == 'pagar':
        break
    precio = float(input("Ingrese el precio del artículo: "))
    carrito[articulo] = precio

print("\nLista de la compra:")
total = 0
for articulo, precio in carrito.items():
    print(f"{articulo}: ${precio:.2f}")
    total += precio

print(f"\nTotal a pagar: ${total:.2f}")

