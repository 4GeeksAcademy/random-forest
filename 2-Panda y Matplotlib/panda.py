import pandas as pd

#imprime el rago de fechas

date = pd.date_range(start='05-01-2021', end='05-12-2021')

print(date)

#divide todos los valores:

serie = pd.Series([2,4,6,8,10])

print(serie.apply(lambda n : n/2))

#ordena las tablas con los valores introducidos

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]

tabla_creada = pd.DataFrame(data, columns=['Marca','Modelo','Color'])

print(tabla_creada)

#Añadir una lista y ordenarla

data = [
    { 
        "brand": "Toyota", 
        "make": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "make": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porche", 
        "make": "Cayenne",
        "color": "White"
    }
]

data.append({
        "brand": "Tesla", 
        "make": "Model S",
        "color": "Red"
    })

print(pd.DataFrame(data))

#borra la primera columna con .iloc:

import pandas as pd

data_frame = pd.read_csv('./us_baby_names_right.csv')

data_frame = data_frame.iloc[:,1:] #selecciona todas las filas y las columnas menos la primera y lo imprime en un nuevo diccionario

print(data_frame)

#contar los valores de una columna, en este caso vamos a contar el genero:

data_frame1 = data_frame.value_counts('Gender')

print(data_frame1)

#seleccionar todos los valores de una columna, sumarlos y contarlos

data_frame2 = data_frame.groupby('Name').sum()

print(len(data_frame2))