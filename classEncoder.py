class Encoder:
    def __init__(self):
        self.Codex = []
        self.atualIndex = 0
        
    def fit(self,lista):
        for item in lista:
            onList = False
            for code in self.Codex:
                if item == code[0]: onList = True
            if not onList:
                Codex.append([item,self.atualIndex])
                self.atualIndex+=1
    
    def transform(self,lista):
        resposta = []
        for item in lista:
            for code in self.Codex:
                if item == code[0]: resposta.append(code[1])
        if len(lista)==1: return resposta[0]
        return resposta
    
    def fit_transform(self,lista):
        self.fit(lista)
        return self.transform(lista)
    
    def inverse_transform(self,lista):
        resposta = []
        for item in lista:
            for code in self.Codex:
                if item == code[1]: resposta.append(code[0])
        if len(lista)==1: return resposta[0]
        return resposta