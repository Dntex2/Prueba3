import numpy as np
asientos = [["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],
["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],
["A","A","A","A","A","A","A","A","A","A","X","A","A","A","A"],
["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],
["A","A","A","A","A","A","A","X","A","A","A","A","A","A","A"],
["A","A","A","A","A","A","A","A","A","A","X","A","A","A","A"],
["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],
["A","A","A","A","A","A","A","A","X","A","A","A","A","A","A"],
["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],
["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"]]
pelicula = ["AVATAR 2 3D"]
fila = 10
columna = 15
while True:
    try:
        print("Para iniciar debe rellenar los siguentes datos")
        nombre = str(input("Ingrese su nombre: "))
        break
    except ValueError:
        print("Ingrese un nombre valido")

while True:
    try:
        print("====¿usted es alumno duoc uc?====")
        print("[1] SI")
        print("[2] NO")
        opc_duoc = int(input("Ingrese una opcion: "))
        if opc_duoc == 1:
            print("¡Usted es alumno de DUOCUC!")
            print("Se le dara un descuento de 10%")
            descuento_duoc = 1
            break
        elif opc_duoc == 2:
            print("Usted no es alumno de duoc")
            descuento_duoc = 2
            break
    except ValueError:
        print("ERROR")

precio = 0

def imprimir():
    for fila in range(10):
        for columna in range(15):
            print(f"[{asientos[fila][columna]} ]", end="")
        print("")
def es_disponible(fila,columna):
    asientos[fila][columna] = "XD"
while True:
    try:
        print("=====CINE DUOC UC=====")
        print("Ingrese una de las siguientes opciones")
        print("[1] COMPRAR ENTRADA")
        print("[2] VER ASIENTOS")
        print("[3] Seleccionar asientos")
        print("[4] FINALIZAR COMPRA")
        opc = int(input("Ingrese la opcion: "))
        if opc == 1:
            if descuento_duoc == 1:
                print("Se le a aplicado un descuento de un 10%")
                precio = 9000
            elif descuento_duoc == 2:
                print("Su entrada fue comprada exitosamente")
                precio = 10000
        elif opc == 2:
            print("Los asientos disponibles son los siguientes: ")
            imprimir()
        elif opc == 3:
            while True:
                try:
                    fila = int(input("Seleccione la fila"))
                    columna = int(input("Seleccione la columna"))
                    if (es_disponible(fila,columna)):
                        print("Su asiento esta disponible")
                    else:
                        print("Su asiento no esta disponible")
                except ValueError:
                    print("error")
        elif opc == 4:
            if descuento_duoc == 1:
                print("=====BOLETA=====")
                print("PRECIO ORIGINAL = $10000")
                print(f"DESCUENTO = {precio}")
                print(f"NOMBRE = {nombre}")
                print("PELICULA = AVATAR 2 3D")
                break
            elif descuento_duoc == 2:
                print("=====BOLETA=====")
                print("PRECIO ORIGINAL = $10000")
                print(f"NOMBRE = {nombre}")
                print("PELICULA = AVATAR 2 3D")
                break
    except ValueError:
        print("Ingrese una opcion valida")


