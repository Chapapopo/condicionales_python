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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
tem_1 = int(input("Ingresar la primer temperatura:\n"))
tem_2 = int(input("Ingresar la segunda temperatura:\n"))
tem_3 = int(input("Ingresar le tercer temperatura:\n"))

if tem_1 == tem_2 == tem_3:
    print("las tres temperaturas son iguales y", tem_3,"es su promedio")
else:
    if (tem_1 > tem_2) and (tem_1 > tem_3):
        print(tem_1,"es la mayor temperatura")
    elif tem_2 > tem_3:
        print(tem_2,"es la mayor temperatura")
    else:
        print(tem_3,"es la mayor temperatura")
    if (tem_1 < tem_2) and (tem_1 < tem_3):
        print(tem_1,"es la menor temperatura")
    elif tem_2 < tem_3:
        print(tem_2,"es la menor temperatura")
    else:
        print(tem_3,"es la menor temperatura")
    pro = (tem_2 + tem_1 + tem_3) / 3
    print(pro,"es el promedio de las tres temperaturas")