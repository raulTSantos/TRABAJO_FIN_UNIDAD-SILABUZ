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
        print(f"Cantida de pokemones encontrados: 0")
    else:
        for index,element in enumerate(lista, start=1):
            print(f"POKEMON {index}")
            getPokemon(element)

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
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass

def presentacion():
    clear_console()
    print("---------------------------------------------------------------------------")
    print("------------ BIENVENIDO A LA APLICACIÓN DE POKEMON-API -------------")
    print("---------------------------------------------------------------------------")
    show_operations()
