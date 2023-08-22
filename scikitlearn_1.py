import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, classification_report, confusion_matrix

#Input(x) -> Comentarios(review)
#Output(y) -> Sentimientos

# Lectura y analisis la data
df_review = pd.read_csv("Ejercicio1/Data/IMDB Dataset.csv")
#print(df_review)
df_positivo = df_review[df_review["sentiment"]=="positive"][:9000]
df_negativo = df_review[df_review["sentiment"]=="negative"][:1000]
df_review_des = pd.concat([df_positivo, df_negativo])
#print(df_review_des.value_counts("sentiment"))

# Balanceo de data
rus = RandomUnderSampler()
df_review_bal, df_review_bal["sentiment"] = rus.fit_resample(df_review_des[["review"]], 
                                                             df_review_des["sentiment"])
#print(df_review_bal.value_counts("sentiment"))

#Separado de data
train, test= train_test_split(df_review_bal, test_size=0.33, random_state=42)
# print(train.count(), test.count())
train_x, train_y = train["review"], train["sentiment"]
test_x, test_y = test["review"], test["sentiment"]

# Transformación de data (bag of words) -> (CountVectorizer|Tfidf)
tfidf = TfidfVectorizer(stop_words="english")
train_x_vector = tfidf.fit_transform(train_x)
test_x_vector = tfidf.transform(test_x)

# Implementación de modelos

#SVC
svc = SVC(kernel = "linear")
svc.fit(train_x_vector, train_y)

#Decision Tree
dec_tree = DecisionTreeClassifier()
dec_tree.fit(train_x_vector, train_y)

# Naive Bayes
gnb = GaussianNB()
gnb.fit(train_x_vector.toarray(), train_y)

#Logic Regression
lr = LogisticRegression()
lr.fit(train_x_vector, train_y)

#Evaluación 

#score (precisión)
#print(svc.score(test_x_vector, test_y))             #0.841
#print(dec_tree.score(test_x_vector, test_y))        #0.662
#print(gnb.score(test_x_vector.toarray(), test_y))   #0.630
#print(lr.score(test_x_vector, test_y))              #0.829

#F1 score (Recall)
#print(f1_score(test_y, 
#               svc.predict(test_x_vector), 
#               labels= ["positive", "negative"], 
#               average = None))

# Reporte de clasificación 
#print(classification_report(test_y, 
#                            svc.predict(test_x_vector), 
#                            labels= ["positive", "negative"]))

# Confusion matrix
#print(confusion_matrix( test_y, 
#                        svc.predict(test_x_vector), 
#                        labels= ["positive", "negative"]))

# GridSearchCV
parametros = {"C": [1,4,8,16,32], "kernel": ["linear", "rbf"]}
svc_grid = GridSearchCV(svc, parametros, cv = 5)
svc_grid.fit(train_x_vector, train_y)
print(svc_grid.best_estimator_)
print(svc_grid.best_params_)
print(svc_grid.best_score_)