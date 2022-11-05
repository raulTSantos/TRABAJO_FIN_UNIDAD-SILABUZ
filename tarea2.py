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
        pass
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

