# Importamos la libreria 
from sklearn import datasets

# Importamos la datos de la misma libreria
datasets = datasets.load_breast_cancer()
print (datasets)

### Entendimiento de data ###

# verificar la informacion contenida en el dataset
print ("Información del dataset: ")
print (datasets.keys())
print()

# Verifico las caracteriticas del dataset 
print ("Caracteristicas del dataset:")
print (datasets.DESCR)

# Seleccionamos todas las columnas 
x = datasets.data

# Defino los datos correspondientes a las etiquetas
y = datasets.target

### Implementación del modelo ###

from sklearn.model_selection import train_test_split

# Separación de los datos de 'train' en entrenamiento y prueba para probar los algoritmos
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# Defino del algoritmo a utilizar
from sklearn.naive_bayes import GaussianNB 
algoritmo =GaussianNB()

# Entrenamos el modelo
algoritmo.fit (x_train, y_train)

# Realizo una predicción 
y_pred = algoritmo.predict(x_test)

# verifico la matriz de confusión 
from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(matriz)

# Calculo la precisión del modelo
from sklearn.metrics import precision_score
precision = precision_score (y_test, y_pred)
print ("Precision del modelo:")
print(precision)

# calculo la exactitid del modelo
from sklearn.metrics import accuracy_score
exactitud = accuracy_score (y_test, y_pred)
print ("Exactitud del modelo:")
print(exactitud)

# Calculon la sensibilidad del modelo
from sklearn.metrics import recall_score
sensibilidad = recall_score (y_test, y_pred)
print("Sensibilidad del modelo:")
print(sensibilidad)

# Calculo del puntaje del modelo 
from sklearn.metrics import f1_score
puntaje_f1 = f1_score(y_test, y_pred)
print("Puntaje del modelo:")
print (puntaje_f1)
 
#Calculo la curva ROC-AUC del modelo
from sklearn.metrics import roc_auc_score

roc_auc = roc_auc_score(y_test, y_pred)
print("Curva ROC-AUC del modelo:")
print(roc_auc)

print("Precision del modelo: {0:.5f}".format(precision))
print("Exactitud del modelo: {0:.5f}".format(exactitud))
print("Sensibilidad del modelo: {0:.5f}".format(sensibilidad))
print("Puntaje del modelo: {0:.5f}".format(puntaje_f1))
print("Curva ROC-AUC del modelo: {0:.5f}".format(roc_auc))
