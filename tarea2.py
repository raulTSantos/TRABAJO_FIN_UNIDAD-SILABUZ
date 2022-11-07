import requests
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

URL_PRINCIPAL="https://pokeapi.co/api/v2"

URL_GENERATION=f"{URL_PRINCIPAL}/generation"
URL_ABILITY=f"{URL_PRINCIPAL}/ability"
URL_POKEMON_SHAPE=f"{URL_PRINCIPAL}/pokemon-shape"
URL_HABITAT=f"{URL_PRINCIPAL}/pokemon-habitat"
URL_TYPE=f"{URL_PRINCIPAL}/type"

def getResponse(path: str) -> str:
    try:
        rsp= requests.get(path)
        data= rsp.json()
        return data
    except Exception as err:
        return rsp.raise_for_status()

def getPokemon(name: str) -> None:
     rsp= requests.get("https://pokeapi.co/api/v2/pokemon/"+name)
     data = rsp.json()
     abilities = [ability['ability']['name'] for ability in data['abilities']]

     print(f"Nombre: {data['name']}")
     print(f"Habilidad: {','.join(abilities)}")
     print(f"URL: {data['sprites']['front_default']}")
     print("-------------------------------------------------------------------------------------------")

def validate_input(lista: list[str]) -> str:
    value= input("Ingrese una opcion(Ejem: 1): ").strip()
    options=[str(element) for element in range(1,len(lista)+1)]
    print("")
    while value not in options:
        print("La respuesta ingresada no es valida ")
        value= input(f"Ingrese valores del 1 al {len(lista)}: ").strip()
        print("")
    return value

def show_elements(lista):
    for index,x in enumerate(lista,start=1):
        print(f"{index}. {x} ")
    print(f"Total de {len(lista)} resultados\n")

def show_pokemons(lista: list[str]) -> None:
    if len(lista) ==0:
        print(f"Cantidad de pokemones encontrados: 0")
    else:
        for index,element in enumerate(lista, start=1):
            print(f"POKEMON {index}")
            getPokemon(element)

#Pinta nuevos encabezados
def print_title(strn):
    print("*"*len(strn))
    print(strn)
    print("*"*len(strn))

#retorna una lista anidada a partir de los elemento de la lista original en fragmentos de 5
def pagination(lista):
    temp=[]
    initial=0
    while initial <len(lista):
        temp.append(lista[initial:initial+5])
        initial +=5
    return temp


#Permite pintar en consola los pokemones usando paginacion con un tamaño de 5 elementos
def show_paginated(lista):
    pages = pagination(lista)
    total_page=len(pages)
    current_page=1
    if total_page >0:
        while True:
            if total_page != current_page:
                if current_page <total_page:
                    clear_console()
                    print("********************************************************************************")
                    show_pokemons(pages[current_page-1])
                    print("********************************************************************************")     
                    rpt=input(" Ingrese 'S' (Siguiente) o 'X' (Escapar): ").strip()
                    if rpt.upper() == 'S':
                        current_page +=1           
                    else:
                        break
                    
                if current_page <total_page and current_page >1:
                    clear_console()
                    print("********************************************************************************")
                    show_pokemons(pages[current_page-1])
                    print("********************************************************************************")       
                    rpt=input("Ingrese 'A' (Anteriror),'S' (Siguiente) o 'X' (Escapar): ").strip()
                    
                    if rpt.upper() == 'A':
                        current_page -=1
                    if rpt.upper() == 'S':
                        current_page +=1           
                    else:
                        print("Escapando de los resultados ....")
                        break

            elif total_page == current_page  and current_page >1:
                clear_console()
                print("********************************************************************************")
                show_pokemons(pages[current_page-1])
                print("********************************************************************************") 
                rpt=input("Ingrese 'A' (Anterior) o 'X' (Escapar): ").strip()      
                if rpt.upper() == 'A':
                    current_page -=1
                else:
                    print("Escapando de los resultados ....")
                    break
            else:
                clear_console()
                print("********************************************************************************")
                show_pokemons(pages[current_page-1])
                print("********************************************************************************") 
                break

#retorna true o false si el ususario quiere continuar
def execute_app():  
    response = input("¿Quieres regresar al menu de opciones? (si o no): ")
    response = response.upper()
    if response == "SI":
        clear_console()
        return True
    else: 
        clear_console()
        return False

#Funcion que ejecuta el desarrollo del programa
def run_app():
    clear_console()
    presentacion()
    while execute_app():     
        show_operations()
    else :
        print("Hasta pronto")


def operation_1():
    try:
        generation_json = getResponse(URL_GENERATION)
        names_list=[x["name"] for x in generation_json['results']]
        show_elements(names_list)
        print("Escriba una las opciones para ver pokemones disponibles y presione ENTER\n")
        value=validate_input(names_list)
        data_json = getResponse(f"{URL_GENERATION}/{value}")
        pokemon_species_list=[x["name"] for x in data_json['pokemon_species']]
        show_pokemons(pokemon_species_list)
    except Exception :
        print("Surgio un errror")

def operation_2():
    clear_console()
    try:
        shape_json= getResponse(URL_POKEMON_SHAPE)
        names_list=[x["name"] for x in shape_json['results']]

        print_title("LISTADO DE FORMAS DE POKEMONES")
        show_elements(names_list)
        
        print("Escriba una las opciones para ver pokemones disponibles y presione ENTER\n")
        value=validate_input(names_list)
        data_json = getResponse(f"{URL_POKEMON_SHAPE}/{value}")

        clear_console()
        print_title(f"LISTADO DE POKEMONES SEGUN FORMA: {names_list[int(value)-1]}")
        pokemon_species_list=[x["name"] for x in data_json['pokemon_species']]
        show_paginated(pokemon_species_list)

    except Exception :
        print("Surgio un error en el sistema.")
    

def operation_3():
    clear_console()
    try:
        ability_json= getResponse(URL_ABILITY)
        names_list=[x["name"] for x in ability_json['results']]

        print_title("LISTADO DE HABILIDADES DE POKEMONES")
        show_elements(names_list)

        print("Escriba una las opciones para ver pokemones disponibles y presione ENTER\n")
        value=validate_input(names_list)
        data_json = getResponse(f"{URL_ABILITY}/{value}")

        clear_console()
        print_title(f"LISTADO DE POKEMONES SEGUN HABILIDAD: {names_list[int(value)-1]}")
        pk_list=[x["pokemon"]["name"] for x in data_json['pokemon']]
        show_paginated(pk_list)

    except Exception :
        print("Surgio un error en el sistema.")

def operation_4():
    clear_console()
    try:
        habitat_json= getResponse(URL_HABITAT)
        names_list=[x["name"] for x in habitat_json['results']]

        print_title("LISTADO DE HABITAT DE POKEMONES")
        show_elements(names_list)

        print("Escriba una las opciones para ver pokemones disponibles y presione ENTER\n")
        value=validate_input(names_list)
        data_json = getResponse(f"{URL_HABITAT}/{value}")

        clear_console()
        print_title(f"LISTADO DE POKEMONES SEGUN HABITAT: {names_list[int(value)-1]}")
        pokemon_species_list=[x["name"] for x in data_json['pokemon_species']]
    
        show_paginated(pokemon_species_list)
    except Exception :
        print("Error de sistema.")

def operation_5():
    try:
        clear_console()
        pokemon_type_json= getResponse(URL_TYPE)
        names_list=[x["name"] for x in pokemon_type_json['results']]

        print_title("LISTADO DE TIPOS DE POKEMONES")
        show_elements(names_list)

        print("Escriba una las opciones para ver pokemones disponibles y presione ENTER\n")
        value=validate_input(names_list)
        data_json = getResponse(f"{URL_TYPE}/{names_list[value]}")

        clear_console()
        print_title(f"LISTADO DE POKEMONES SEGUN TIPO: {names_list[int(value)-1]}")
        pk_list=[x["pokemon"]["name"] for x in data_json['pokemon']]
        
        show_paginated(pk_list)
    except Exception :
        print("Error de sistema.")

def show_operations():
    print("\n------------ MENU DE OPCIONES ------------")
    print("\n(1) Listar pokemons por generacion")
    print("(2) Listar pokemons por forma")
    print("(3) Listar pokemons por habilidad")
    print("(4) Listar pokemons por habitat")
    print("(5) Listar pokemons por tipo")

    opcion= input("Ingrese una de las opciones mostradas: ").strip()
    
    while opcion not in ["1","2","3","4","5"]:
        print("Respuesta ingresada no valida. Ingrese valores del 1 al 5 ")
        opcion= input("Ingrese nuevamente la opcion (Ejem: 1) : ").strip()

    if opcion == "1":
        operation_1()
    elif opcion == "2":
        operation_2()
    elif opcion == "3":
        operation_3()
    elif opcion == "4":
        operation_4()
    elif opcion == "5":
        operation_5()

def presentacion():
    clear_console()
    print("---------------------------------------------------------------------------")
    print("------------ BIENVENIDO A LA APLICACIÓN DE POKEMON-API -------------")
    print("---------------------------------------------------------------------------")
    show_operations()


run_app()
