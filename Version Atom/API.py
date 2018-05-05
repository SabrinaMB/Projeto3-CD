import pandas as pd
import tmdbsimple as tmdb

credits = pd.read_csv("tmdb_5000_credits.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")

tmdb.API_KEY = 'abcd9827ce3fb2298891370ff0cd0e58'

def takeInfos(id):
    atores = []
    crews = []
    keywords = []

    movie = tmdb.Movies(id)

    response = movie.info()
    popularity = round(movie.popularity)
    media = round(movie.vote_average)
    title = movie.title
    for ator in movie.credits()['cast']: atores.append(ator['name'])
    for crew in movie.credits()['crew']: crews.append(crew['name'])
    for keyword in movie.keywords()['keywords']: keywords.append(keyword['name'])
    # for similar in movie.similar_movies()['results']:
    #     sTitles.append(similar['title'])
    #     sPopularity.append(round(similar["popularity"]))
    #     sMedia.append(round(similar["vote_average"]))

    return title,popularity,media,atores,crews,keywords

def takeOffInfos(line):
    atores = []
    crews = []
    keywords = []

    popularity = round(movies.iloc[line].popularity)
    media = round(movies.iloc[line].vote_average)
    title = movies.iloc[line].title

    i = 0
    x = credits.iloc[0].cast[i:].find('"name": ')
    y = credits.iloc[0].cast[x:].find(",")+x
    name=[credits.iloc[0].cast[x+9:y-1]]
    for i in range(2):
        i = y+16
        x = credits.iloc[0].cast[i:].find('"name": ')
        y = credits.iloc[0].cast[i+x:].find('",')+x+i
        name.append(credits.iloc[0].cast[i+x+9:y])
    atores = name

    x = credits.iloc[0].crew.find('"name": ')
    y = credits.iloc[0].crew[x:].find(",")+x
    crew =[credits.iloc[0].crew[x+9:y-2]]

    x = movies.iloc[0].keywords.find('"name": ')
    y = movies.iloc[0].keywords[x:].find(",")+x
    name=[movies.iloc[0].keywords[x+9:y-1]]
    for i in range(2):
        i = y+4
        x = movies.iloc[0].keywords[i:].find('"name": ')
        y = movies.iloc[0].keywords[i+x:].find('"},')+x+i
        name.append(movies.iloc[0].keywords[i+x+9:y])
    keywords = name

    return title,popularity,media,atores,crews,keywords

def NormalizeCat(X): #Não esta sendo usado
    global perda
    i = 0
    n = len(X)
    limit = 300
    if len(X)>limit:perda+=1
    while(len(X)<limit):
        if i == n: i = 0
        X.append(X[i])
        i+=1
    while(len(X)>limit):
        X.pop()
    return X
