y_test = "variable de real"
y_pred = "variable de predicha"

# matriz de confusion
from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(y_test, y_pred)
print(matriz)

# exactitud
from sklearn.metrics import accuracy_score

exactitud = accuracy_score(y_test, y_pred)
print(exactitud)

# presición 
from sklearn.metrics import precision_score

precisión = precision_score(y_test, y_pred)
print(precisión)

# sensibilidad 
from sklearn.metrics import recall_score

sensibilidad = recall_score(y_test, y_pred)
print(sensibilidad)

# puntaje F1
from sklearn.metrics import f1_score

puntaje = f1_score(y_test, y_pred)
print(puntaje)