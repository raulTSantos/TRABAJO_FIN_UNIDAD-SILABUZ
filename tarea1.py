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


def buscar_libro_isbn_titulo():
    print("\n|--------------------------------------|")
    print("|---- BUSCAR LIBROS: ISBN O TITULO ----|")
    print("|--------------------------------------|")

    isbn_titulo = str(input("\nIngresar el ISBN o TÍTULO del libro: "))

    msj = "Resultado de la busqueda" 
    print("\n--------------------------------------")
    print(f"{msj:^38}")
    print("--------------------------------------")

    c = 0
    for element in data:
        if element.isbn == isbn_titulo:
            c += 1
            print()
            print(element)
        elif element.titulo == isbn_titulo:
            c += 1
            print()
            print(element)

    msj = f"Se ha encontrado {c} coincidencia(s)"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

def ordenar():
    print("\n|-------------------------------|")
    print("|---- ORDENAR LIBRO: TITULO ----|")
    print("|-------------------------------|")

    sorted_titles=[]

    for element in data:
        sorted_titles.append(element.titulo)

    sorted_titles.sort()

    msj = "Resultado del ordenamiento" 
    print("\n--------------------------------")
    print(f"{msj:^32}")
    print("--------------------------------")

    for tittle in sorted_titles:
        for element in data:
            if element.titulo == tittle:
                print()
                print(element)

    msj = f"Se ha ordenado correctamente los libros con respecto al TÍTULO"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

def buscar_libro_autor_editorial_genero():
    print("\n|--------------------------------------------------|")
    print("|---- BUSCAR LIBROS: AUTOR, EDITORIAL O GENERO ----|")
    print("|--------------------------------------------------|")

    autor_editorial_genero = str(input("\nIngresar el AUTOR, EDITORIAL O GENERO: "))
    
    msj = "Resultado de la busqueda" 
    print("\n--------------------------------------")
    print(f"{msj:^38}")
    print("--------------------------------------")

    c = 0
    for element in data:
        if autor_editorial_genero in element.autor_es:
            c += 1
            print()
            print(element)
        if element.editorial == autor_editorial_genero:
            c += 1
            print()
            print(element)
        if element.genero == autor_editorial_genero:
            c += 1
            print()
            print(element)
        
    msj = f"Se ha encontrado {c} coincidencia(s)"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

def actualizar():
    print("\n|--------------------------------------|")
    print("|---- ACTUALIZAR DATOS DE UN LIBRO ----|")
    print("|--------------------------------------|")

    id_libro = str(input("\nIngresar el ID del libro para actualizar sus datos (1,2,...,n): "))
    
    for element in data:
        if element.id == id_libro:
            element.titulo      = input("Ingrese el TÍTULO del libro: ")
            element.genero      = input("Ingrese el GÉNERO del libro: ")
            element.isbn        = input("Ingrese el ISBN del libro: ")
            element.editorial   = input("Ingrese la EDITORIAL del libro: ")
            element.autor_es    = input("Ingrese autor(Si son varios,separar por comas sin espacio): ").split(",")

            msj = f"Se ha actualizado correctamente los datos del libro con el ID {id_libro}"
            print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
            print(f"{msj:^107}")
            print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
            
            return

    msj = f"No existe ningun libro con el ID {id_libro}"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

def buscar_libro_autores():
    print("\n|------------------------------------------|")
    print("|---- BUSCAR LIBROS: NUMERO DE AUTORES ----|")
    print("|------------------------------------------|")

    nro_autores = int(input("\nIngresar el número de autores del libro (1,2,...,n): "))

    msj = "Resultado de la busqueda" 
    print("\n--------------------------------------")
    print(f"{msj:^38}")
    print("--------------------------------------")

    c = 0
    for element in data:
        n = len(element.autor_es)
        if n == int(nro_autores):
            c += 1
            print()
            print(element)

    msj = f"Se ha encontrado {c} coincidencia(s)"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    
def save_file():
    print("\n|-------------------------------------|")
    print("|---- GUARDAR ARCHIVO (CSV) EN DD ----|")
    print("|-------------------------------------|")

    with open('books.csv', 'a', newline="") as file:
        writer_object = csv.writer(file)
        #si el archivo esta vacio,escribe cabecera
        if os.stat('books.csv').st_size == 0:
            writer_object.writerow(["id","titulo","genero","isbn","editorial","autor(es)"])
        for x in data:
            writer_object.writerow([x.id,x.titulo,x.genero, x.isbn,x.editorial,",".join(x.autor_es)])
        
        file.close()
    
    msj = "Archivo (CSV) guardado correctamente"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

def read_file():
    print("\n|-----------------------------|")
    print("|---- LEER UN ARCHIVO CSV ----|")
    print("|-----------------------------|")
    
    msj = "Resultado de la lectura" 
    print("\n--------------------------------------")
    print(f"{msj:^38}")
    print("--------------------------------------")

    print()

    with open('books.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)

    msj = "Archivo (CSV) leido correctament"
    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"{msj:^107}")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")


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
        read_file()
    elif opcion == 2:
        listar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        buscar_libro_isbn_titulo()
    elif opcion == 6:
        ordenar()
    elif opcion == 7:
        buscar_libro_autor_editorial_genero()
    elif opcion == 8:
        buscar_libro_autores()
    elif opcion == 9:
        actualizar()
    elif opcion == 10:
        save_file()
    else:
        print()
        exit()