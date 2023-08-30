import numpy as np 

# Matrices vacias

# Crear matrices de unos - 3 filas 4 columnas
unos = np.ones((3,4))
print(unos)

# Crear una matriz de ceros - 3 filas 4 columnas
ceros = np.zeros((3,4))
print(ceros)

# Crear una matriz con valores aleatorios
aleatorios = np.random.random((2,2))
print(aleatorios)

# Crear matriz vacia 
vacia = np.empty((3,2))
print(vacia)

# Crear una matriz con un solo valor 
full = np.full((2,2),8)
print(full)

# Crear matrices con valores espaciados uniformemente
espacio_1 = np.arange(0,30,5)
print(espacio_1)

espacio_2 = np.linspace(0,2,5)
print(espacio_2)

# Crear una matriz identidad
identidad_1 = np.eye(4,4)
print(identidad_1)

identidad_2 = np.identity(4)
print(identidad_2)

# Conocer las dimensiones de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#Conocer el tipo de los datos
a = np.array([(1,2,3)])
print(a.dtype)

# Conocer el tamaño y la forma de la matriz
a = np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)

# Cambio de forma de una matriz
a = np.array([(8,9,10), (11,12,13)])
print(a)
a = a.reshape(3,2)
print(a)

# Extraer un solo valor de la matriz 
# el valor ubicado en la fila 0 columna 2
a = np.array([(1,2,3,4), (13,4,5,6)])
print(a[0,2])

# Extraer los valores de todas las filas 
# ubicados en la columna 3
a = np.array([(1,2,3,4), (3,4,5,6)])
print(a[0:,2])

#Operaciones matematicas

#Encontrar el valor mínimo, máximo y la suma
a = np.array([(2,4,8)])
print(a.min())
print(a.max())
print(a.sum())

# Calcular la raíz cuadrada y la desviación estándar 
a = np.array([(1,2,3), (3,4,5,)])
print(np.sqrt(a))
print(np.std(a))

# Calcular la suma, resta, multiplicación y 
# división de dos matrices
x = np.array([(1,2,3), (3,4,5,)])
y = np.array([(1,2,3), (3,4,5,)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)


