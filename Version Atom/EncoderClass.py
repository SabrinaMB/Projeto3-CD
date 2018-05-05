import pandas as pd
from API import *

credits = pd.read_csv("tmdb_5000_credits.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")

class Encoder:
    def __init__(self,lista):
        self.Codex = []
        self.atualIndex = 1
        self.fit(lista)

    def fit(self,lista):
        for item in lista:
            onList = False
            for code in self.Codex:
                if item == code[0]: onList = True
            if not onList:
                self.Codex.append([item,self.atualIndex])
                self.atualIndex+=1

    def transform(self,lista):
        resposta = []
        for item in lista:
            for code in self.Codex:
                if item == code[0]: resposta.append(code[1])
        return resposta

    def fit_transform(self,lista):
        self.fit(lista)
        return self.transform(lista)

    def inverse_transform(self,lista):
        resposta = []
        for item in lista:
            for code in self.Codex:
                if item == code[1]: resposta.append(code[0])
        return resposta

    def show(self):
        print(self.Codex)

    def Feed(self,line):
        title,popularity,media,atores,crews,keywords = takeInfos(line)  # Prever
        # title,popularity,media,atores,crews,keywords = takeOffInfos(line)  # Treino
        self.fit([title])
        self.fit(atores)
        self.fit(crews)
        self.fit(keywords)

        Atores = self.transform(atores)
        Crews = self.transform(crews)
        Keywords = self.transform(keywords)
        X = self.fit_transform  (["P"+str(popularity/10)])
        if len(Crews)>0:X.append(Crews[0])
        else: X.append(X[-1])
        for i in range(3):
            if len(Atores)>(i): X.append(Atores[i])
            else: X.append(X[-1])

            if len(Keywords)>(i): X.append(Keywords[i])
            else: X.append(X[-1])
        y = round(media/2)
        return X,y
