class Individual:
    def __init__(self) -> None:
        pass
    
    def __init__(self, chromossomes):
        self.chromossomes = chromossomes
    
    def get_chromossomes(self):
        return self.chromossomes
    
    def set_chromossomes(self, chromossomes):
        self.chromossomes = chromossomes