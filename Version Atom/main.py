import pandas as pd
import numpy as np
from numpy.random import shuffle
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
import tmdbsimple as tmdb
import pickle

from API import *
from EncoderClass import *

tmdb.API_KEY = 'abcd9827ce3fb2298891370ff0cd0e58'

credits = pd.read_csv("tmdb_5000_credits.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")

#Definição de banda de treino e teste baseado nos DataFrames acima
IDlist = list(movies["id"])
n = 4000
IDTrainList = IDlist[:n]
IDTestList = IDlist[n:]

#Inicialização dos Classificadores e do Encoder(Criado mais a cima)
Codex = Encoder(['M0',"M1","M2",'M3','M4','M5','M6','M7','M8','M9','M10'])
Naive = MultinomialNB()

print("Iniciando Treino")
print(". . .")
#Treino para SVM e Naive Bayes
n = 4000
i = 0
X = []
y = []
shuffle(IDTrainList)
for i in range(len(IDTrainList)):
    X.append(Codex.Feed(i)[0])
    y.append(Codex.Feed(i)[1])
    i += 1
    if i == n:break
Naive.fit(X,y)
print("Treino Finalizado")
print("Escrevendo Arquivo")

# Escrevendo Naive Treinado em arquivo Naive
with open('Naive.pkl', 'wb') as output:
    pickle.dump(Naive, output, pickle.HIGHEST_PROTOCOL)
with open('Codex.pkl', 'wb') as output:
    pickle.dump(Codex, output, pickle.HIGHEST_PROTOCOL)


print("Done")
