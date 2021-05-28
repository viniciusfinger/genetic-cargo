from Item import *

def instanciaItens() -> list:
    itens = []
    
    itens.append(Item(nome="iPhone 11", peso=500, valor=6000))
    itens.append(Item(nome="Televisão 50 pol", peso=15000, valor=3400))
    itens.append(Item(nome="Geladeira", peso=100000, valor=2600))
    itens.append(Item(nome="Livro", peso=100, valor=37))
    itens.append(Item(nome="Livro", peso=250, valor=300))
    itens.append(Item(nome="Box livros", peso=500, valor=90))
    itens.append(Item(nome="Mesa com cadeiras", peso=80000, valor=3000))
    itens.append(Item(nome="Escultura", peso=1000, valor=12000))
    itens.append(Item(nome="Sofá", peso=60000, valor=6000))
    itens.append(Item(nome="Freezer", peso=100000, valor=3000))
    itens.append(Item(nome="Microondas", peso=10000, valor=700))

    return itens