from sklearn.naive_bayes import GaussianNB

x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

algoritmo = GaussianNB()

algoritmo.fit(x_entrenamiento, y_entrenamiento)
algoritmo.predict(x_prueba)
