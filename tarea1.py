import time

class Acciones:
    def leer(self):
        pass
    
    def listar(self,tamaño_lista_libros,lista_libros):
        print("\n|-------------------------|")
        print("|---- LISTA DE LIBROS ----|")
        print("|-------------------------|")

        libro = {}
        libros = []

        for index,i in enumerate(range(tamaño_lista_libros),1):
            libro["Id"]        = lista_libros[i][0]
            libro["Título"]    = lista_libros[i][1]
            libro["Género"]    = lista_libros[i][2]
            libro["ISBN"]      = lista_libros[i][3]
            libro["Editorial"] = lista_libros[i][4]
            libro["Autor(es)"] = lista_libros[i][5]
            
            msj = f"Libro N° {index}"
            print("\n-------------------------")
            print(f"{msj:^25}")
            print("-------------------------")

            elementos = libro.items()
            
            for clave,valor in elementos:
                print(f"{clave} = {valor}")
            
            libros.append(libro)
 
    def agregar(self,tamaño_lista_libros,lista_libros):
        print("\n|-------------------------|")
        print("|---- AGREGAR LIBROS -----|")
        print("|-------------------------|")

        lista_antigua_libros = lista_libros

        lista_numero_autores = []

        lista_nueva_libros = []
        tamaño_lista_libros = len(lista_libros) # DIRECTAMENTE RECOGE LA LONGITUD DE LA lista_libros ANTIGUA
        numero_de_libros = int(input("\n¿Cuántos libros deseas registrar?: "))

        for i in range(numero_de_libros):
            print("\n|----------------------------------|")
            print(f"|----- REGISTRO DE LIBRO N° {i+1} -----|")
            print("|----------------------------------|")

            self.id = str(input("\nIngrese el ID del libro: "))
            self.titulo = str(input("Ingrese el TÍTULO del libro: "))
            self.genero = str(input("Ingrese el GÉNERO del libro: "))
            self.isbn = str(input("Ingrese el ISBN del libro: "))
            self.editorial = str(input("Ingrese la EDITORIAL del libro: "))

# ---------------------------------------------------------------------
# ------------------------------ AUTORES ------------------------------
# ---------------------------------------------------------------------
            lista_autores = []
            tamaño_lista_autores = len(lista_autores)
            numero_de_autores = int(input(f'\n¿Cuántos autores tiene el libro "{self.titulo}"?: '))
            print("---------------------------------------")
           
            # ---------------------------------------
            # VALIDACION SIMPLE DE LA VARIABLE numero_de_autores
            # ---------------------------------------
            if numero_de_autores != 0:
                lista_numero_autores.append(numero_de_autores)
            while numero_de_autores == 0:
                numero_de_autores = int(input(f"\nIngrese un número valido por favor: "))
                print("---------------------------------------")
            # --------------------------------------

            for i in range(numero_de_autores):
                lista_autores.append(str(input(f'Ingrese el AUTOR N° {i+1} del libro "{self.titulo}": ')))
                tamaño_lista_autores += 1 
            print("---------------------------------------")

            lista_nueva_libros.append([self.id,self.titulo,self.genero,self.isbn,self.editorial,self.autor_es])
            
            tamaño_lista_libros += 1

        lista_libros = lista_antigua_libros + lista_nueva_libros

        rpta = str(input("\n¿Desea visualizar todos los libros? (S/N): "))

        if rpta.upper() == "S":
            Acciones.listar(self,tamaño_lista_libros,lista_libros)

    def eliminar(self):
        pass

    def buscar_libro_isbn_titulo(self):
        pass

    def ordenar(self):
        pass

    def buscar_libro_autor_editorial_genero(self):
        pass

    def buscar_libro_numpaginas(self):
        pass

    def actualizar(self):
        pass

    def guardar(self):
        pass

    def salir(self):
        print("\n---------------------------------------------------------------------------")
        print("-------------------------- OK. HASTA PRONTO... ----------------------------")
        print("---------------------------------------------------------------------------\n")
        exit()

class Libros(Acciones):
    def __init__(self):
        self.id = ()
        self.titulo = ()
        self.genero = ()
        self.isbn = ()
        self.editorial = ()
        self.autor_es = ()

    def registrar_libros(self):
        print("\n---------------------------------------------------------------------------")
        print("------------ BIENVENIDO A LA APLICACIÓN DE REGISTRO DE LIBROS -------------")
        print("---------------------------------------------------------------------------")

        lista_numero_autores = [] # LISTA DE TODOS LOS NÍMEROS DE AUTORES 

        lista_libros = []
        tamaño_lista_libros = len(lista_libros)
        numero_de_libros = int(input("\n¿Cuántos libros deseas registrar?: "))

        for i in range(numero_de_libros):
            print("\n|----------------------------------|")
            print(f"|----- REGISTRO DE LIBRO N° {i+1} -----|")
            print("|----------------------------------|")

            self.id = str(input("\nIngrese el ID del libro: "))
            self.titulo = str(input("Ingrese el TÍTULO del libro: "))
            self.genero = str(input("Ingrese el GÉNERO del libro: "))
            self.isbn = str(input("Ingrese el ISBN del libro: "))
            self.editorial = str(input("Ingrese la EDITORIAL del libro: "))

# ---------------------------------------------------------------------
# ------------------------------ AUTORES ------------------------------
# ---------------------------------------------------------------------
            lista_autores = []
            tamaño_lista_autores = len(lista_autores)
            numero_de_autores = int(input(f'\n¿Cuántos autores tiene el libro "{self.titulo}"?: '))
            print("---------------------------------------")
           
            # ---------------------------------------
            # VALIDACION SIMPLE DE LA VARIABLE numero_de_autores
            # ---------------------------------------
            if numero_de_autores != 0:
                lista_numero_autores.append(numero_de_autores)
            while numero_de_autores == 0:
                numero_de_autores = int(input(f"\nIngrese un número valido por favor: "))
                print("---------------------------------------")
            # --------------------------------------

            for i in range(numero_de_autores):
                lista_autores.append(str(input(f'Ingrese el AUTOR N° {i+1} del libro "{self.titulo}": ')))
                tamaño_lista_autores += 1 
            print("---------------------------------------")

            self.autor_es = lista_autores

            lista_libros.append([self.id,self.titulo,self.genero,self.isbn,self.editorial,self.autor_es])

            tamaño_lista_libros += 1  
# ---------------------------------------------------------------------

        input('\nPresiona "Enter" para continuar...')
        print("Loading...")
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        
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
                time.sleep(1)
                self.leer()
            elif opcion == 2:
                time.sleep(1)
                self.listar(tamaño_lista_libros,lista_libros)
            elif opcion == 3:
                time.sleep(1)
                self.agregar(tamaño_lista_libros,lista_libros) # AUMENTE ESTO tamaño_lista_libros,lista_libros
            elif opcion == 4:
                time.sleep(1)
                self.eliminar()
            elif opcion == 5:
                time.sleep(1)
                self.buscar_libro_isbn_titulo()
            elif opcion == 6:
                time.sleep(1)
                self.ordenar()
            elif opcion == 7:
                time.sleep(1)
                self.buscar_libro_autor_editorial_genero()
            elif opcion == 8:
                time.sleep(1)
                self.buscar_libro_numpaginas()
            elif opcion == 9:
                time.sleep(1)
                self.actualizar()
            elif opcion == 10:
                time.sleep(1)
                self.guardar()
            else:
                time.sleep(1)
                self.salir()

# ---------------------------- INSTANCIAS ----------------------------
libros = Libros()
print(libros.registrar_libros())

