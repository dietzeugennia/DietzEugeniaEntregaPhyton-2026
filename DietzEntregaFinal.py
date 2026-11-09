LILA = "\033[95m"
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"

import json


productos = ["arandano", "banana", "ciruela","durazno","fresa"]



def sincronizar():
    with open("datos.json", "w") as archivo:
        json.dump(productos, archivo)


try:
    with open("datos.json", "r") as archivo:
        productos = json.load(archivo)


except FileNotFoundError:
    with open("datos.json", "w") as archivo:
        json.dump([], archivo)


def actualizar():
    with open("datos.json","w") as archivo:
        json.dump(productos,archivo)



while True:


    opcion = input(f"{LILA}***INVENTARIO DE PRODUCTOS***\n B- Buscar producto\n L-Listar producto\n A-Agregar producto\n R-Remover producto\n \n-------------------\nS-Salir de la lista\n\n"f"{RESET}\n").upper()


    if opcion == "B":
        buscar = input("\nBuscar producto: ").strip().lower()


        if  buscar in productos:
            print(f"{VERDE}{buscar} existe en inventario\n{RESET}")
        else:
            print(f"{ROJO}{buscar} no existe en inventario\n{RESET}")
        sincronizar()


    if opcion == "L":
        print(productos)

    elif opcion == "A":
        agregar = input("\nAgregar producto: ").strip().lower()
        productos.append(agregar)
        print(f"\n{agregar} se ha agregado con exito!\n")
        sincronizar()


    
    match opcion:
        case "R":
            remover = input("\nRemover producto: ").strip().lower()
            productos.remove(remover)
            print(f"\n {remover} se ha removido con exito!\n")
            sincronizar()
        case "S":
            break
