from sklearn.ensemble import RandomForestClassifier

x_entrenamiento = "variablesIndependientes_entrenamiento"
y_entrenamiento = "variablesIndependientes_entrenamiento"
x_prueba = "variablesIndependientes_prueba"
y_prueba = "variablesIndependientes_prueba"

# Definir algoritmo
algoritmo = RandomForestClassifier()
#### configuracion #####

# n_estimators: numero de arboles que contendra (a mayor numero de arboles, mejor rendimiento pero sera mas lento)

# Criterion: aplicacion de la suma de los cuadrados residuales usando MSE
# y MAE para implementar la separacion de los datos para los arboles de decision a construir 

# max_depth: Trata sobre la profundidad del arbol, 
# ayuda a evitar el sobreajuste

# max_features: define el número máximo de características que se probaran en un arbol individual


# Entrenar modelo
algoritmo .fit(x_entrenamiento, y_entrenamiento)

#Predecir modelo
algoritmo.predict(x_prueba)

#Precisión del modelo
precision = algoritmo.score(x_prueba, y_prueba) 