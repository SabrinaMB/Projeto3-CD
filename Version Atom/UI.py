import tmdbsimple as tmdb
import pickle

tmdb.API_KEY = 'abcd9827ce3fb2298891370ff0cd0e58'
#Função para Interface de Usuario
def UI():

    Entrada = str(input("Qual filme você deseja saber a nota?\n"))
    search = tmdb.Search()
    response = search.movie(query=Entrada)
    if len(search.results) == 0: print("Desculpe não encontrei nenhum filme com este nome...")
    if len(search.results) > 1:
        print("Encontrei os seguintes filmes com este nome, qual deles você deseja?")
        for i in range(len(search.results)): print(str(search.results[i]['title']) + "  [{}]".format(i))
        Escolido = int(input("\n"))
    else: Escolido = 0
    print(chr(27) + "[2J")
    print("Calculando. . .")

    X,y = Codex.Feed(search.results[Escolido]['id'])

    saida = Naive.predict([X])
    # print("A nota desse filme provavelmente será {0}".format(saida[0]))
    # DEVS
    nota = search.results[Escolido]['vote_average']
    print(chr(27) + "[2J")
    print("A nota desse filme provavelmente será de {0} / 5.0 estrelas".format(round(nota)/2))

if __name__ =="__main__":
    with open('Naive.pkl', 'rb') as fileout:
        Naive = pickle.load(fileout)
    with open('Codex.pkl', 'rb') as fileout2:
        Codex = pickle.load(fileout2)

    UI()
