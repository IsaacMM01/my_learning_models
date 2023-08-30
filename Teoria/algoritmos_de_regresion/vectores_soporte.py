from sklearn.svm import SVR

x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

# Definir algoritmo
algoritmo = SVR()

# Entrenar modelo
algoritmo .fit(x_entrenamiento, y_entrenamiento)

#Predecir modelo
algoritmo.predict(x_prueba)

#Precisión del modelo
precision = algoritmo.score(x_prueba, y_prueba) 