# SECCIÓN A: clasificación y visualización

def clasificar_existencia(cantidad):
    # TODO A1: retornar la clasificación correspondiente.
    if cantidad == 0:
        return "Agotado"
    elif cantidad <= 5:
        return "Bajo"
    else:
        return "Suficiente"

  # TODO A2:
    # Mostrar número de producto, cantidad y clasificación.
def mostrar_inventario(existencias):
    if not existencias:
        return print("El inventario está vacío.")
    elif len (existencias) >= 1 and len(existencias) <= 20:
        return print (f"El inventario tiene {len(existencias)} productos.")
    else:
        return print ("El inventario tiene más de 20 productos.")
        

  # SECCIÓN B: validación de entradas

def pedir_entero_en_rango(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}. Intente de nuevo.")
        except ValueError:
            print("Error: Entrada inválida. Ingrese un número entero válido.")

# SECCIÓN C: operaciones de inventario

def retirar_unidades(disponible, cantidad):
    # TODO C1:
    # Si no hay unidades suficientes, informar y retornar disponible.
    # Si hay suficientes, retornar disponible - cantidad.
    return disponible


def reponer_unidades(disponible, cantidad):
    # TODO C2: retornar disponible + cantidad.
    return disponible


# SECCIÓN D: programa principal

existencias = [8, 0, 4]

while True:
    # TODO D1: mostrar el menú de opciones.
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Mostrar inventario")
    print("2. Retirar unidades")
    print("3. Reponer unidades")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            mostrar_inventario(existencias)

        case "2" | "3":
            numero_producto = pedir_entero_en_rango(
                f"Número de producto (1 a {len(existencias)}): ",
                1,
                len(existencias)
            )

            cantidad = pedir_entero_en_rango(
                "Cantidad de unidades (1 a 20): ",
                1,
                20
            )

            indice = numero_producto - 1

            if opcion == "2":
                existencias[indice] = retirar_unidades(
                    existencias[indice],
                    cantidad
                )
            else:
                existencias[indice] = reponer_unidades(
                    existencias[indice],
                    cantidad
                )

            print(f"Existencia actual: {existencias[indice]}")

        case "4":
            print("Programa finalizado.")
            break

        case _:
            print("Error: selecciona una opción entre 1 y 4.")