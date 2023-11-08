import numpy as np


categorias = ["Electrónica", "Ropa", "Hogar", "Deportes", "Alimentos", "Juguetes"]


ventas = [
    ["Ropa", "Hogar"],
    ["Electrónica", "Juguetes"],
    ["Alimentos", "Hogar"],
    ["Deportes", "Ropa"],
    ["Juguetes", "Hogar"]
]


codificacion_one_hot = np.zeros((len(ventas), len(categorias)))


for i, transaccion in enumerate(ventas):
    for categoria in transaccion:
        indice_categoria = categorias.index(categoria)
        codificacion_one_hot[i, indice_categoria] = 1


print("Matriz de Codificación One-Hot:")
print(codificacion_one_hot)