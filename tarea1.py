import csv
import os

print("\n***********************************************************************************************************")
print("***************************** BIENVENIDO A LA APLICACIÓN DE REGISTRO DE LIBROS ****************************")
print("***********************************************************************************************************")

data = []

class Libro():
    def __init__(self):
        self.id         = ()
        self.titulo     = ()
        self.genero     = ()
        self.isbn       = ()
        self.editorial  = ()
        self.autor_es   = ()

    def __str__(self) -> str:
        return f"Id: {self.id}, Título: {self.titulo}, Género: {self.genero}, ISBN: {self.isbn}, Editorial: {self.editorial}, Autor(es): {self.autor_es}"

def create():  
    # INSTANCIAR UN NUEVO OBJETO
    libro = Libro()

    libro.id        = input("\nIngrese el ID del libro: ")
    libro.titulo    = input("Ingrese el TÍTULO del libro: ")
    libro.genero    = input("Ingrese el GÉNERO del libro: ")
    libro.isbn      = input("Ingrese el ISBN del libro: ")
    libro.editorial = input("Ingrese la EDITORIAL del libro: ")
    libro.autor_es  = input("Ingrese AUTOR (Si son varios, separar por comas y sin espacio): ").split(",")

    # AGREGAR EL NUEVO OBJETO
    data.append(libro)

def agregar():
    print("\n***********************************************************************************************************")

    agregar_libros = int(input("\n¿Cuántos libros deseas agregar?: "))

    print("\n|------------------------|")
    print("|---- AGREGAR LIBROS ----|")
    print("|------------------------|")

    for i in range(agregar_libros):
        # INSTANCIAR UN NUEVO OBJETO
        libro = Libro()

        libro.id        = input("\nIngrese el ID del libro: ")
        libro.titulo    = input("Ingrese el TÍTULO del libro: ")
        libro.genero    = input("Ingrese el GÉNERO del libro: ")
        libro.isbn      = input("Ingrese el ISBN del libro: ")
        libro.editorial = input("Ingrese la EDITORIAL del libro: ")
        libro.autor_es  = input("Ingrese autor (Si son varios, separar por comas y sin espacio): ").split(",")

        # AGREGAR EL NUEVO OBJETO
        data.append(libro)

    msj = f"Se ha agregado correctamente los {agregar_libros} libros"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

    print("\n***********************************************************************************************************")

def listar():
    print("\n***********************************************************************************************************")

    print("\n|-------------------------|")
    print("|---- LISTA DE LIBROS ----|")
    print("|-------------------------|")

    for index,x in enumerate(data,1):
        msj = f"Libro N° {index}"
        print("\n-------------------------")
        print(f"{msj:^25}")
        print("-------------------------")

        print("\nId: ",x.id)
        print("Título: ",x.titulo)
        print("Género: ",x.genero)
        print("ISBN: ",x.isbn)
        print("Editorial: ",x.editorial)
        print("Autor(es): ",x.autor_es)

    msj = f"Se ha listado correctamente los {index} libros"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

    print("\n***********************************************************************************************************")

def eliminar():
    print("\n***********************************************************************************************************")

    print("\n|---------------------------|")
    print("|---- LIBROS A ELIMINAR ----|")
    print("|---------------------------|")

    libro_eliminar = int(input("\nIngresar el número del libro que desea eliminar (1,2,...,n): "))-1

    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("Se ha eliminado correctamente el libro: ")
    print(f"{data[libro_eliminar]}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

    data.pop(libro_eliminar)

    print("\n***********************************************************************************************************")

# ----------------------------
# INTERACTUANDO CON LA CONSOLA
# ----------------------------

numero_de_libros = int(input("\n¿Cuántos libros deseas registrar?: "))

print("\n|--------------------------|")
print("|---- REGISTRAR LIBROS ----|")
print("|--------------------------|")
for i in range(numero_de_libros):
    create()

opcion = 0 
while opcion != 11:
    
    print("\n------------------------------------------------------------------")
    print("------------------------ MENÚ DE OPCIONES ------------------------")
    print("------------------------------------------------------------------")
    
    print("\n(1) Leer archivo de disco duro (.txt o csv)")
    print("(2) Listar libros")
    print("(3) Agregar libro")
    print("(4) Eliminar libro")
    print("(5) Buscar libro por ISBN o por título")
    print("(6) Ordenar libros por título")
    print("(7) Buscar libros por autor, editorial o género")
    print("(8) Buscar libros por número de autores")
    print("(9) Editar o actualizar datos de un libro")
    print("(10) Guardar libros en archivo de disco duro (.txt o csv)")
    print("(11) Salir")
    print("\n------------------------------------------------------------------")


    opcion = int(input("\n¿Que opción elegiste?: "))

    # ---------------------------------------
    # VALIDACION SIMPLE DE LA VARIABLE opcion
    # ---------------------------------------
    while opcion == 0 or opcion >= 12:
        opcion = int(input(f"\nIngrese un número valido por favor: "))
        print("--------------------------------------")
    # ---------------------------------------

    if opcion == 1:
        pass
    elif opcion == 2:
        listar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    elif opcion == 7:
        pass
    elif opcion == 8:
        pass
    elif opcion == 9:
        pass
    elif opcion == 10:
        pass
    else:
        print()
        exit()