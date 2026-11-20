nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    while True:
        try:
            cantidad = int(input("\n¿Cuántas canciones deseas agregar?: "))
            if cantidad >= 0:
                break
            print("Ingresa un número igual o mayor que cero.")
        except ValueError:
            print("Ingresa un número entero válido.")

    for i in range(cantidad):
        print(f"\n--- Canción {i + 1} ---")

        nombre = input("Nombre de la canción: ").strip()
        artista = input("Nombre del artista: ").strip()

        while True:
            try:
                duracion = float(input("Duración en minutos: "))
                if duracion > 0:
                    break
                print("La duración debe ser mayor que cero.")
            except ValueError:
                print("Ingresa una duración válida.")

        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                print("La popularidad debe estar entre 1 y 100.")
            except ValueError:
                print("Ingresa un número entero válido.")

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\n¡Canciones agregadas correctamente!")

def ver_reportes():
    if not nombres:
        print("\nNo hay canciones registradas.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    indice_mayor = popularidades.index(max(popularidades))
    indice_menor = popularidades.index(min(popularidades))
    promedio = sum(popularidades) / total_canciones

    print("\n========== REPORTES ==========")
    print("Número total de canciones:", total_canciones)
    print("Duración total:", round(duracion_total, 2), "minutos")
    print(
        "Canción más popular:",
        nombres[indice_mayor],
        "- Popularidad:", popularidades[indice_mayor]
    )
    print(
        "Canción menos popular:",
        nombres[indice_menor],
        "- Popularidad:", popularidades[indice_menor]
    )
    print("Promedio de popularidad:", round(promedio, 2))

def buscar_canciones():
    if not nombres:
        print("\nNo hay canciones registradas.")
        return

    print("\n--- BUSCAR CANCIONES ---")
    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        artista_buscar = input("Nombre del artista: ").strip().lower()
        encontrado = False

        for i in range(len(nombres)):
            if artista_buscar in artistas[i].lower():
                print("\nCanción:", nombres[i])
                print("Artista:", artistas[i])
                print("Duración:", duraciones[i], "minutos")
                print("Popularidad:", popularidades[i])
                encontrado = True

        if not encontrado:
            print("\nNo se encontraron canciones de ese artista.")

    elif opcion == "2":
        try:
            minimo = int(input("Popularidad mínima: "))
            maximo = int(input("Popularidad máxima: "))
        except ValueError:
            print("\nIngresa valores enteros válidos.")
            return

        if not (1 <= minimo <= 100 and 1 <= maximo <= 100):
            print("\nLos valores deben estar entre 1 y 100.")
            return
        if minimo > maximo:
            print("\nEl mínimo no puede ser mayor que el máximo.")
            return

        encontrado = False
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print("\nCanción:", nombres[i])
                print("Artista:", artistas[i])
                print("Duración:", duraciones[i], "minutos")
                print("Popularidad:", popularidades[i])
                encontrado = True

        if not encontrado:
            print("\nNo se encontraron canciones en ese rango.")

    else:
        print("\nOpción no válida.")

def playlist_recomendada():
    if not nombres:
        print("\nNo hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\n======= PLAYLIST RECOMENDADA =======")
    print("Promedio de popularidad:", round(promedio, 2))
    print("\nCanciones con popularidad superior al promedio:\n")

    encontrado = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print("Canción:", nombres[i])
            print("Artista:", artistas[i])
            print("Duración:", duraciones[i], "minutos")
            print("Popularidad:", popularidades[i])
            print("--------------------------")
            encontrado = True

    if not encontrado:
        print("No hay canciones que superen el promedio.")

def menu():
    while True:
        print("\n================================")
        print("       FESTIVAL PLAYLIST")
        print("================================")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")
        print("================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_canciones()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            playlist_recomendada()
        elif opcion == "5":
            print("\n¡Gracias por utilizar Festival Playlist!")
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
