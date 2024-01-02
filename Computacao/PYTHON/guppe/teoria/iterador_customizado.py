"""
Escrevendo um iterador customizado

class Contador():
    def __init__(self,menor,maior):
        self.menor = menor
        self.maior = maior


    def __next__(self):
        return self

    def __iter__(self):
        if self.maior> self.menor:
            numero = self.menor
            self.menor = self.menor +1
            return numero
        raise StopIteration
"""