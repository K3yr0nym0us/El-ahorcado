from secrets import choice
from os import system

lista_palabras = ['mascota','maquina','tecnologia','programa','maletin']

#esta funcion selecciona y lee una palabra y la convierte en guiones para mostrarla al usuario
def convertir_palabra():
    palabra = choice(lista_palabras)
    len(palabra)
    guiones = ''
    for letra in palabra:
        guiones += '_'
    return [palabra,guiones]

#esta funcion solicita una letra y la verifica
def pedir_letra():
    verificar = 1
    numeros = '0123456789'
    abcdario = 'abcdefghijklmnopqrstuvwxyz'
    while verificar >= 1:
        ingreso = input('Ingresa una letra: ')
        system('cls')
        if len(ingreso) >= 2:
            print('Ingresa solo un caracter')
            continue
        elif ingreso in numeros:
            print("Ingresa una letra, no un numero!")
            continue
        elif ingreso in abcdario:
            verificar = verificar - 1
            return ingreso
        else:
            print('Ingresa un numero, no un simbolo')
            continue

#funcion final, reemplaza cada '_' de la palabra segun corresponda
#al acierto del jugador y lo muestra en pantalla verificando si esta repetida o no
def revelar_letra():
    palabra_oculta = convertir_palabra()
    palabra = palabra_oculta.pop(0)
    guiones = palabra_oculta.pop()
    print('Frase: ', guiones)
    vidas = 6
    letras_repetidas = []
    while vidas > 0: 
        letra = pedir_letra()
        if letra in palabra:
            if letra in letras_repetidas:
                print('Esta letra ya fue descubierta, escoge otra!')
                system('cls')
                continue
            else:
                letras_repetidas.append(letra)
                for index in range(0, len(guiones)):
                    if (guiones[index] == '_'):
                        if (palabra[index] == letra):
                            temp = list(guiones)
                            temp[index] = letra
                            guiones = "".join(temp)
                print(f'Letra correcta\n{guiones}\n')
                if '_' in guiones:
                    continue
                else:
                    print('Ganaste!!!')
                    system("timeout /t 5 >nul")
                    return            
        else:
            print(f'Letra incorrecta\n{guiones}\n')
            vidas = vidas - 1
            print(f'Te quedan {vidas} vidas')
            system("timeout /t 1 >nul")
            continue
    print('Te quedaste sin vidas!\nFin del juego :c')
    system("timeout /t 5 >nul")

#esta funcion indica el inicio del programa
def inicio():
    print('Bienvenido al juego el ahorcado\nComienzas con 6 vidas\n')
    print('Puedes adivinar la frase antes de quedarte sin vidas?\n')
    revelar_letra()

inicio()