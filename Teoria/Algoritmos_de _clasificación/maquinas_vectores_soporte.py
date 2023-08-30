from sklearn.svm import SVC

x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

# Definir algoritmo
algoritmo = SVC()
#### configuracion #####
# kernel = transforma los datos de entrada del 
# conjunto de datos a la adecuada

# C = parametro de penalizacion, indica cuanto 
# error es soportable

# Entrenar modelo
algoritmo .fit(x_entrenamiento, y_entrenamiento)

#Predecir modelo
algoritmo.predict(x_prueba)
