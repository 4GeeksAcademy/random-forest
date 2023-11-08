import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

colores = ['Rojo','Negro','Verde']
probabilidades = [18/37,18/37,1/37]

tiradas = np.random.choice(colores, size=100, p=probabilidades)

print(tiradas)

#imprimir los booleanos de las tiradas que sean de color rojo

print(tiradas == 'Rojo')

#creamos otro diccionario con los valores que han salido en las tiradas

salidas = {
    'Rojo': np.count_nonzero(tiradas == 'Rojo'),
    'Negro': np.count_nonzero(tiradas == 'Negro'),
    'Verde': np.count_nonzero(tiradas == 'Verde')
}

print(salidas)

for color, veces in salidas.items():
    print(f'El color {color} ha salido: {veces} veces')

#vamos a crear una tabla con los valores de cada uno

select, values = np.unique(tiradas, return_counts=True)

print(select, values)
ind = np.argmax(values)
print(ind)
print(select[ind])

alumnos = { 'Nombre': ['Juan', 'Maria', 'Pedro'],
            'Apellidos': ['Perez Perez', 'Cagigao Vazquez', 'Ruiz Guines']}
            
df = pd.DataFrame(alumnos)
print(df)

notas = np.random.uniform(0,10,3)
print(np.round(notas,2))
print(np.mean(notas))
print(np.sum(notas>2))

print(np.count_nonzero(notas>5)/len(notas)*100)

df['Notas'] = notas

dni = ['12345N','12346K','12987P']

df['DNI'] = dni

df.set_index('DNI', drop=True, inplace=True)

df['Grupos'] = pd.Series(df.index).apply(lambda x: 1 if int(x[:-1])%2 == 0 else 2).values

print(df)

print(df[(df.Notas > 3) & (df.Grupos == 2)])

print(df.loc['12345N'])

#derivada

def f(x): return x + 1
def g(x): return x**2 + 1
x = np.linspace(-2,2,100)

plt.plot(x, f(x), label='f')
plt.plot(x, g(x), label='g')
plt.plot(0, f(0), 'ro')
plt.plot(1, f(1), 'ro')
plt.legend()
plt.show()


