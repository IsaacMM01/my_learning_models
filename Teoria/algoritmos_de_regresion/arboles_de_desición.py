from sklearn.tree import DecisionTreeRegressor

x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

# Definir algoritmo
algoritmo = DecisionTreeRegressor()
#### configuracion #####

# Criterion: aplicacion de la suma de los cuadrados 
# residuales usando MSE y MAE.

# Splitter: estrategia utilizada para la división de cada nodo
# puede ser best o random.

# max_depth: Trata sobre la profundidad del arbol, 
# ayuda a evitar el sobreajuste

# 

# Entrenar modelo
algoritmo .fit(x_entrenamiento, y_entrenamiento)

#Predecir modelo
algoritmo.predict(x_prueba)

#Precisión del modelo
precision = algoritmo.score(x_prueba, y_prueba) 