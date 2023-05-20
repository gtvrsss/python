class Carro:
    def __init__(self, marca, cor, velocidade, qtdRodas, qtdPassageiros, tamanho):  # definindo um método
        self.marca = marca
        self.cor = cor
        self.velocidade = velocidade
        self. qtdRodas = qtdRodas
        self.qtdPassageiros = qtdPassageiros
        self.tamanho = tamanho

    def andar(self):  # agora nosso carro pode andar!
        print("Está começando a andar!")

    def buzinar(self): # agora nosso carro pode buzinar!
        print("Está buzinando!")

    def acenderLuz(self): # agora nosso carro pode acender a luz!
        print("Acendeu a luz!")


tesla = Carro("Tesla", "prata", 100.5, 4, 4, 3.5)
fusca = Carro("VW", "vermelho", 80, 4, 4, 3.0)
celta = Carro("Chevrolet", "preto", 90, 4, 2, 3.0)

print("Fusca")
print(fusca.marca)
print(fusca.cor)
print(fusca.qtdPassageiros)
print(fusca.qtdRodas)
print(fusca.tamanho)
print(fusca.velocidade)

print("Tesla")
print(tesla.marca)
print(tesla.cor)
print(tesla.qtdPassageiros)
print(tesla.qtdRodas)
print(tesla.tamanho)
print(tesla.velocidade)

print(f'O carro {fusca.marca} vai acender a luz!')