import numpy as np

print(np.__version__)

array = np.zeros(10)

print(array)

arr = array.itemsize

print(arr)

tamaño = array.size

print(tamaño)

total = arr * tamaño

print(total)

print(np.info(np.zeros))

vector = np.zeros(10)

vector[4] = 1

print(vector)

rango = np.arange(10,50)

print(rango)

invertido = np.arange(0,10)

print(invertido[::-1])

matriz = np.arange(0,9).reshape(3,3)

print(matriz)

#encuentra los indices que no valen zero de un array:

conzeros = [1,2,0,0,4,0]

print(np.nonzero(conzeros))

#crea un array de identidad, donde seran todos zeros menos 1 en la diagonal

identico = np.eye(3)

print(identico)

#crea 3 numeros aleatorios en un array

aleatorios = np.random.random(3)

print(aleatorios)

#devuelve el valor maximo de un array creado al azar

maximo = np.random.random(10)

print(np.max(maximo))

#devuelve el valor medio de un array creado al azar

media = np.random.random(10)

print(np.mean(media))

#cambia todos los valores menos los bordes de un array

unos = np.ones((5,5)) # recordar que tiene que ser un valor individual para poner lineas y columnas, otra seria valor = (5,5) np.ones(valor)

unos[1:-1,1:-1] = 0

print(unos)

#añadir valores a los bordes del array con np.pad:

bordespad = np.ones((5,5))

bordespad = np.pad(bordespad, pad_width=1, constant_values=0) #crea 1 borde con el calor 0

print(bordespad)

#sacar la diafonal de una matriz:

matrix = np.arange(0,9).reshape(3,3)

print(np.diag(matrix))

#hacer tablero de damas:

damas = np.ones((8,8))

damas[::2,::2] = 0
damas[1::2,1::2] = 0

print(damas)