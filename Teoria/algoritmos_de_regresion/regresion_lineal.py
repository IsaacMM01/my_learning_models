from sklearn import linear_model

#Regresion lineal simple (y = ax + b)
x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

# Definir el algoritmo que se va a usar, en este caso se decidio usar regresión lineal por su simplicidad
algoritmo = linear_model.LinearRegression()

# Entrenar el modelo
algoritmo.fit(x_entrenamiento, y_entrenamiento)

# Predecir el modelo
algoritmo.predict(x_prueba)

# Para conocer el valor de la pendiente
a = algoritmo.coef_

# Para conocer el valor de la intersección o constante 
b = algoritmo.intercept_

# Para conocer la precision R^2 
precision = algoritmo.score(x_prueba, y_prueba)