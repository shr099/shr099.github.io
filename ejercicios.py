def parono():
    num = int(input("Ingresa un num: "))
    if num % 2 == 0:
        print("Es par")
    else:
        print("No es par")
# parono()

def calculadora():
    n1 = float(input('Ingresa el primer numero: '))
    n2 = float(input('Ingresa el segundo numero: '))
    signo = input('Ingresa la operacion que quieres hacer (+ - * /): ')

    if signo == '+' or signo == 'suma':
        n_operacion = n1 + n2
        print(f'{n1} + {n2} = {n_operacion}')

    elif signo == '-' or signo == 'resta':
        n_operacion = n1 - n2
        print(f'{n1} - {n2} = {n_operacion}')

    elif signo == '*' or signo == 'multiplicacion':
        n_operacion = n1 * n2
        print(f'{n1} * {n2} = {n_operacion}')

    elif signo == '/' or signo == 'division':
        if n2 != 0:
            n_operacion = n1 / n2
            print(f'{n1} / {n2} = {n_operacion}')

    else:
        print('Ingresa un valor valido. (puedes esribir la operacion)')
# calculadora()

def tabla_mult():
    n = int(input('Ingresa un numero: '))
    for i in range(1,11):
        multiplicacion = n * i
        print(f'{n} x {i} = {multiplicacion}')
        i =+ 1
# tabla_mult()

def lista():
    n = input('Ingresa una lista de numeros separados por comas (,): ')
    lista = [int(numero) for numero in n.split(',')]
    lista.sort()

    print(f'Lista orddenada de menor a mayor {lista}')
# lista()

import random

def adivinar_numero():
    n_adivinar = random.randint(1,100)
    intentos = 0

    while True:
        n_usuario = int(input('ingresa un numero del 1 al 100: '))

        if n_usuario < n_adivinar:
            print('El numero que tratas de adivinar es MAYOR que el que ingresaste')
            intentos += 1
            print(n_adivinar)
        if n_usuario > n_adivinar:
            print('El numero que tratas de adivinar es MENOR que el que ingresaste')
            intentos += 1
            print(n_adivinar)

        if n_usuario == n_adivinar:
            print(f'Correcto! El numero era {n_adivinar}')
            break
# adivinar_numero()

def contar_vocales():
    frase = input('Ingresa una frase: ')
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0,}
    for letra in frase.lower():
        if letra in vocales:
            vocales[letra] += 1

    total_vocales = sum(vocales.values())
    print(f'La frase tiene {total_vocales} vocales')
    print(f'Aqui esta el detalle: {vocales}')
# contar_vocales()

def palindromo():
    frase = input('Ingresa una frase: ')
    frase_sin_espacios = ''.join(frase.lower().split())
    lista = []
    for letra in frase_sin_espacios:
        lista.append(letra)
    if lista == lista[::-1]:
        print('Si es un palindromo')
    else:
        print('No es un palindromo')
    print(lista)
    print(lista[::-1]) # voltear la lista

# palindromo()

def juego_ahorcado():
    vidas = 10
    palabra = 'mano'
    letras_intentadas = []
    print('\nSi no adivinas una letra te resta una vida, pero si no adivinas la palabra te restan dos vidas')
    # for letra in letras_intentadas:
    #     if letra in letras_intentadas:
    #        
    #     print('_', end= ' ')
    # print()
    while True:
        mostrar_palabra = ''.join([letra if letra in letras_intentadas else '_' for letra in palabra])
        print('\nLa palabra es la siguiente:')
        print(' '.join(mostrar_palabra))

        print('\nOPCIONES')
        print('1. Ingresar una letra')
        print('2. Adivinar la palabra')
        respuesta = input('Ingresa el # de la opcion que desees: ')

        if respuesta == '1':
            letra = input('\nIngresa una letra: ')
            if len(letra) != 1:
                print('Ingresa solo UNA letra')
                continue

            if letra in letras_intentadas:
                print('Ya intentaste con esa letra')
                continue

            letras_intentadas.append(letra)
            if letra in palabra:
                print('Correcto. Adivinaste una letra')
            else: 
                vidas -= 1
                print('Esa letra no esta en la palabra')
                print(f'Te quedan {vidas} vidas')
        elif respuesta == '2':
            palabra_usuario = input('\nIngresa la palabra: ')
            if palabra_usuario == palabra:
                print(f'Correcto! Adivinaste la palabra "{palabra}"')
                print(f'Te quedaban {vidas} vidas')
                break
            else:
                print('Incorreto. Esa no era la palabra')
                vidas -= 2
                print(f'Te quedan {vidas} vidas')
                
        else:
            print('Esta opcion no es valida')
        
        if vidas == 0:
            print(f'Perdiste. La palabra era "{palabra}"')
            break
# juego_ahorcado()

nombres_edades = {
    "Juan": 25,
    "Ana": 22,
    "Luis": 30,
    "María": 20,
    "Pedro": 28
}

def ordenar_edades(nombres_edades):
    edades_ordenadas = sorted(nombres_edades.values())
    print(edades_ordenadas)

    nombres_edades_ordenados = dict(sorted(nombres_edades.items()))

    print(nombres_edades_ordenados)

# ordenar_edades(nombres_edades)
    
    
import random
import string

def generar_contrasena(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_especiales):
    caracteres = ''
    
    if usar_mayusculas:
        caracteres += string.ascii_uppercase  # Letras mayúsculas
    if usar_minusculas:
        caracteres += string.ascii_lowercase  # Letras minúsculas
    if usar_numeros:
        caracteres += string.digits  # Números
    if usar_especiales:
        caracteres += string.punctuation  # Caracteres especiales

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    usar_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    try:
        contrasena = generar_contrasena(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_especiales)
        print(f"Contraseña generada: {contrasena}")
    except ValueError as e:
        print(e)

# if __name__ == "__main__":
#     main()

def juego_ppt():
    import random
    opciones = ["Piedra", "Papel", "Tijera"]
    vidas_usu = 3
    vidas_comp = 3
    while True:
        print('\nBienvenido a piedra, papel o tijera')
        print(f'Tienes {vidas_usu} vidas')
        print('\n¿Qué quieres escoger?')
        print('1. Piedra')
        print('2. Papel')
        print('3. Tijera')
        respuesta = int(input('Ingresa el número de la opción que desees: '))
        res_comp = random.choice(opciones)
        print(f'La computadora eligió: {res_comp}')

        if respuesta not in [1,2,3]:
            print('Opción no válida. Por favor, elige 1, 2 o 3.')
            continue

        eleccion_usuario = opciones[respuesta - 1]  # Mapeo de la elección del usuario, relacionar res usuario y res computadora

        if eleccion_usuario == res_comp:
            print(f'{eleccion_usuario} vs {res_comp}')
            print('Fue empate')
        elif (eleccion_usuario == 'Piedra' and res_comp == 'Tijera') or \
             (eleccion_usuario == 'Papel' and res_comp == 'Piedra') or \
             (eleccion_usuario == 'Tijera' and res_comp == 'Papel'):
            print(f'\n{eleccion_usuario} vs {res_comp}')
            print('Ganaste :)')
            vidas_comp -= 1
        else:
            print(f'{eleccion_usuario} vs {res_comp}')
            print('Perdiste :(')
            vidas_usu -= 1

        print(f'\nTus vidas: {vidas_usu}')
        print(f'Vidas de la maquina: {vidas_comp}')

        if vidas_usu == 0:
            print('\nPERDISTE. No te quedan mas vidas')
            break
        elif vidas_comp == 0:
            print('\nGANASTE. Dejaste a la maquina sin vidas')
            break
# juego_ppt()

def tareas():
    try:
        # Abrimos el archivo y obtenemos el número de la última tarea
        with open('tareas.txt', 'r') as archivo:
            lineas = archivo.readlines()
            if lineas:
                # Obtenemos el número de la última tarea
                i = int(lineas[-1].split('.')[0]) # Agarra las lineas de tareas.txt [-1] agarra la ultima lienea, con el split es busa el punto y separa como dos caracteres diferentes y hace una lista con esos dos, y el 0 lo que hace es tomar el primer valor de la lista, recordando que en una lista se inicia 0, 1 , 2, etc
            else:
                i = 0
    except FileNotFoundError:
        # Si el archivo no existe, inicializamos i en 0
        i = 0

    while True:
        print('\nMENU')
        print('1. Agregar una tarea')
        print('2. Eliminar una tarea')
        print('3. Ver tareas')
        print('4. Salir')
        res = input('Ingresa el # de la opción que desees: ')
        
        if res == '1':
            tarea = input('\nIngresa la tarea que quieres agregar: ')
            i += 1
            with open('tareas.txt', 'a') as archivo:
                archivo.write(f'{i}. {tarea}\n')
            print(f'Tarea "{tarea}" agregada con el número {i}.')

        elif res == '2':
            t_eliminar = input('\nIngresa el # de la tarea que deseas eliminar: ')
            try:
                t_eliminar = int(t_eliminar)  # Convertimos la entrada a un entero
                with open('tareas.txt', 'r') as archivo:
                    lineas = archivo.readlines()

                with open('tareas.txt', 'w') as archivo:
                    nueva_lista = []
                    for linea in lineas:
                        numero, tarea = linea.split('.', 1)
                        if int(numero) != t_eliminar:
                            nueva_lista.append(linea)
                    
                    # Reescribimos las tareas con la numeración corregida
                    for index, linea in enumerate(nueva_lista, start=1):
                        _, tarea = linea.split('.', 1)
                        archivo.write(f'{index}.{tarea}')
                print(f'Tarea #{t_eliminar} eliminada.')
            except ValueError:
                print('Por favor, ingresa un número válido.')
            except Exception as e:
                print(f'Error al eliminar la tarea: {e}')

        elif res == '3':
            try:
                with open('tareas.txt', 'r') as archivo:
                    lineas = archivo.readlines()
                    if lineas:
                        print('\nTareas:')
                        for linea in lineas:
                            print(linea.strip())
                    else:
                        print('\nNo hay tareas.')
            except FileNotFoundError:
                print('\nNo hay tareas.')

        elif res == '4':
            print('Saliendo del programa.')
            break

        else:
            print('Por favor, selecciona una opción válida.')

tareas()
