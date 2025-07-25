# Definimos la función agregar libros
# Creamos la lista llamado inventario
inventario = []

def agregar_libros(*titulos):
    for titulo in titulos:
        inventario.append({titulo: {}})

def asignar_detalles(titulo, autor, genero, año):
    for libro in inventario:
        if titulo in libro:
            libro[titulo]["autor"] = autor
            libro[titulo]["genero"] = genero
            libro[titulo]["año"] = año

def mostrar_biblioteca():
    for libro in inventario:
        for titulo, detalles in libro.items():
            print(f"\nTítulo: {titulo}: ")
            print(f"\nDetalles:\n")
            for clave, valor in detalles.items():
                print(f"{clave}: {valor}")

def buscar_libros(**filtros):
    for libro in inventario:
        for titulo, detalles in libro.items():
            c = c2 = 0
            for clave, valor in detalles.items():
                if "año_max" in filtros:
                    if clave != "año":
                        if clave in filtros and valor == filtros[clave]:
                            c += 1
                    else:
                        if valor <= filtros["año_max"]:
                            c += 1
                else:
                    if clave in filtros and valor == filtros[clave]:
                        c2 += 1
            if c2 == len(filtros) or c == len(filtros):
                print(f"\nTítulo: {titulo}")
                print("Detalles:")
                for clave, valor in detalles.items():
                    print(f"{clave}: {valor}")

# Pruebas
agregar_libros("Cien años de soledad", "El principito", "Don Quijote")
asignar_detalles("El principito", "Antoine de Saint-Exupéry", "Ficción", 1943)
asignar_detalles("Cien años de soledad", "Gabriel García Marquez", "Ficción", 2010)
mostrar_biblioteca()
buscar_libros(genero="Ficción", autor="Gabriel García Marquez")     
buscar_libros(genero="Ficción", año_max=2000)
