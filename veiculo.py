class Veiculo:
    def __init__(self, marca, modelo, cor, tipo,potente=True, fraco=False):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.tipo = tipo
        self.potente = potente
        self.fraco = fraco

    def apresentar(self):
        print(f'Marca:{self.marca}')
        print(f'Tipo de veiculo:{self.tipo}')
        print(f'Modelo:{self.modelo}')
        print(f'Cor:{self.cor}')
        print(f'É Potente:{self.potente}')
        print(f'É Fraco:{self.fraco}')
    def potencia(self):
        if self.potente:
            self.potente = True
            print(f"O veiculo {self.modelo} é potente")
        else:
           print(f'O veiculo {self.modelo} é fraco')
    def fraqueza(self):
        if not self.fraco:
            self.fraco = True
            print(f"O veiculo {self.modelo} é fraco")
        else:
            print(f"O veiculo {self.modelo} é potente")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, potente=True, fraco=False):
        super().__init__(marca,modelo,cor,potente,fraco)
        self.acelerar = False
        self.frear = True
        self.mudar_direcao = False
        self.velocidade_normal = True

    def apresentar(self):
        print("Carro")
        print(f'Marca:{self.marca}')
        print(f'Modelo:{self.modelo}')
        print(f'Cor:{self.cor}')
        if self.acelerar:
            print(f'está acelerando')
        elif self.frear:
            print(f'esta freando')
        elif self.mudar_direcao:
            print(f'o carro esta mudando de direcao')
        elif self.velocidade_normal:
            print(f'o carro esta velocidade normal')

    def acelerando(self):
        if not self.acelerar:
            print(f'o carro esta acelerando')
            self.acelerar = True
            self.velocidade_normal = False
            self.frear = False
            self.mudar_direcao = False

    def brecar(self):
        if not self.frear:
            print(f'o carro esta freando')
            self.frear = True
            self.velocidade_normal = False
            self.acelerar = False

    def direcao(self):
        if not self.mudar_direcao:
            self.mudar_direcao = True
            print(f'o carro esta mudando de direcao')

    def normal(self):
        if not self.velocidade_normal:
            print(f'o carro esta velocidade normal')
            self.velocidade_normal = True
            self.frear = False
            self.mudar_direcao = True
            self.acelerar = False

    def potencia(self):
        print(f'o carro é potente')




v1 = Veiculo( "carro",  "Aston Martin", "One-77 ", "cinza ")
v1.apresentar()
v1.potencia()
print("-"* 20)

v2 = Veiculo( "caminhão", "Volvo", "Volvo VM", "preto")
v2.apresentar()
v2.potencia()
print("-"* 20)

v3 = Veiculo( "moto", "Shineray", "Shineray 250F", "branco")
v3.apresentar()
v3.fraqueza()

print("-"* 20)

c1 = Carro("Hatch", "Fiat", "branco")
c1.apresentar()
c1.normal()
c1.acelerando()
c1.normal()
c1.brecar()
c1.direcao()
c1.potencia()
print("-"* 20)
