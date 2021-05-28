class Item:
    def __init__(self) -> None:
        pass

    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso #em quilos
        self.valor = valor #em Reais

    def getNome(self):
        return self.nome
    
    def getPeso(self):
        return self.peso
    
    def getValor(self):
        return self.valor