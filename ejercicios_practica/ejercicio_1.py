# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if (numero_1>numero_2):
    print("{} es el mayor".format(numero_1))
elif (numero_2>numero_1):
    print("{} es el mayor".format(numero_2))
else:
    print("son el mismo numero")
# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if (numero_1>0):
    print("el primer numero es positivo")
elif(numero_1<0):
    print("el primer numero es negativo")
else:
    print("el primer numero es cero")
# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if (numero_1>0) and (numero_1<100):
    print("el primer numero es mayor a 0 y menor a 100")
# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if (numero_1<10) and (numero_2>-2):
    print("el primer numeo es menor a 10 y el sugundo es mayor a -2")
elif (numero_2>-2):
    print("el segundo numero es mayor a -2")
elif (numero_1<10):
    print("el primer numero es menor a 10")
else:
    print("el primer numeroes mayor o igual a 10 y el segundo es menor o igual a -2")