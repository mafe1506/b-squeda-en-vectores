def buscar_cedula(cedula, lista_cedulas):
    for c in lista_cedulas:
        if c == cedula:
            return True
    return False

# Lista de cédulas habilitadas para votar
cedulas_habilitadas = [1111111,2222222,3333333]

# Cédula a buscar
cedula_usuario = int(input("Ingrese su número de cédula: "))

if buscar_cedula(cedula_usuario, cedulas_habilitadas):
    print("Usted puede votar en las elecciones presidenciales de este año.")
else:
    print("Usted no puede votar en las elecciones presidenciales de este año.")

