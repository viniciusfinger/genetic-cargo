class Item:
    def __init__(self) -> None:
        pass

    def __init__(self, name, weight, price):
        self.name = name
        self.peso = weight
        self.price = price

    def getName(self):
        return self.name
    
    def getWeight(self):
        return self.peso
    
    def getPrice(self):
        return self.price