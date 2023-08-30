from sklearn.tree import DecisionTreeClassifier

x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

algoritmo = DecisionTreeClassifier()
# Criterion: aplicacion de la suma de los cuadrados 
# residuales usando MSE y MAE.

# Splitter: estrategia utilizada para la división de cada nodo
# puede ser best o random.

# max_depth: Trata sobre la profundidad del arbol, 
# ayuda a evitar el sobreajuste


algoritmo.fit(x_entrenamiento, y_entrenamiento)
algoritmo.predict(x_prueba)
