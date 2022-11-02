import time

class Acciones:
    def leer(self):
        pass
    
    def listar(self):
        pass
    
    def agregar(self):
        pass

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
        print("---------------------------------------------------------------------------")
        print("------------ BIENVENIDO A LA APLICACIÓN DE REGISTRO DE LIBROS -------------")
        print("---------------------------------------------------------------------------")
        lista_libros=[]
        tamaño_lista_libros = len(lista_libros)
        numero_de_libros = int(input("\n¿Cuántos libros deseas registrar?: "))

        for i in range(numero_de_libros):
            self.id = str(input("\nIngrese el ID del libro: "))
            self.titulo = str(input("Ingrese el TÍTULO del libro: "))
            self.genero = str(input("Ingrese el GÉNERO del libro: "))
            self.isbn = str(input("Ingrese el ISBN del libro: "))
            self.editorial = str(input("Ingrese la EDITORIAL del libro: "))
            self.autor_es = str(input("Ingrese el AUTOR(ES) del libro: "))

            lista_libros.append([self.id,self.titulo,self.genero,self.isbn,self.editorial,self.autor_es])
            tamaño_lista_libros += 1  

        input('\nPresiona "Enter" para continuar...')
        print("Loading...")
        time.sleep(1)
        print("Loading...")
        time.sleep(1)

        print("\n------------ MENÚ DE OPCIONES ------------")
        opcion = 0 
        while opcion != 11:
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
            opcion = int(input("\n¿Que opciónn elegiste?: "))
            if opcion == 1:
                time.sleep(1)
                self.leer()
            elif opcion == 2:
                time.sleep(1)
                self.listar()
            elif opcion == 3:
                time.sleep(1)
                self.agregar()
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

