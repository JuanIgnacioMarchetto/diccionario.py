
diccionario = {
    "perro": "Mamífero carnívoro doméstico de la familia de los cánidos.",
    "gato": "Mamífero carnívoro doméstico de la familia de los félidos.",
    "casa": "Edificio para habitar.",
    "coche": "Vehículo automóvil de cuatro ruedas.",
    "libro": "Conjunto de hojas de papel u otro material encuadernadas que forman un volumen.",
}

def buscar_palabra(palabra):
    definicion = diccionario.get(palabra.lower())
    if definicion:
        return f"{palabra}: {definicion}"
    else:
        return f"La palabra '{palabra}' no se encuentra en el diccionario."

def main():
    while True:
        print("Diccionario Español")
        print("===================")
        palabra = input("Introduce una palabra para buscar su definición (o 'salir' para terminar): ")
        if palabra.lower() == 'salir':
            break
        print(buscar_palabra(palabra))
        print()

if __name__ == "__main__":
    main()
