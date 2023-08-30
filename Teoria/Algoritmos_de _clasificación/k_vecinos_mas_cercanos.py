from sklearn.neighbors import KNeighborsClassifier

x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

algoritmo = KNeighborsClassifier()
# n_neighbors: numero de vecinos o k por defecto es 5
# para definir la distancia hay dos valores que deben
# ser configurados P y metric

algoritmo.fit(x_entrenamiento, y_entrenamiento)
algoritmo.predict(x_prueba)



