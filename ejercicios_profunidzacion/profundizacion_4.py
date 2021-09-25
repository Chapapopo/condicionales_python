# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
pal_1 = str(input("Ingresar una palabra:\n"))
pal_2 = str(input("Ingresar una palabra:\n"))
pal_3 = str(input("Ingresar una palabra:\n"))
res=int(input("Si quiere ordenar las palabras por orden alfabetico ingrese 1\nSi quiere ordenarlo por cantidad de letras ingrese 2\n"))
if res == 1:
    if (pal_1 > pal_2) and (pal_1 > pal_3):
        print (pal_1)
        if pal_2 > pal_3:
            print (pal_2)
            print (pal_3)
        else:
            print (pal_3)
            print (pal_2)
    elif (pal_2 > pal_3):
        print (pal_2)
        if pal_1 > pal_3:
            print (pal_1)
            print (pal_3)
        else:
            print (pal_3)
            print (pal_1)
    else:
        print (pal_3)
        if pal_1 > pal_2:
            print (pal_1)
            print (pal_2)
        else:
            print (pal_2)
            print (pal_1)
elif res == 2:
    can_1 = len(pal_1)
    can_2 = len(pal_2)
    can_3 = len(pal_3)
    if (can_1 > can_2) and (can_1 > can_3):
        print (pal_1)
        if can_2 > can_3:
            print (pal_2)
            print (pal_3)
        else:
            print (pal_3)
            print (pal_2)
    elif (can_2 > can_3):
        print (pal_2)
        if can_1 > can_3:
            print (pal_1)
            print (pal_3)
        else:
            print (pal_3)
            print (pal_1)
    else:
        print (pal_3)
        if can_1 > can_2:
            print (pal_1)
            print (pal_2)
        else:
            print (pal_2)
            print (pal_1)