class Veiculo:
    def __init__(self, marca, modelo, cor, tipo,forca = True):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__tipo = tipo
        self._forca = forca

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_cor(self):
        return self.__cor

    def get_tipo(self):
        return self.__tipo

    def is_forca(self):
        return self._forca

    def apresentar(self):
        print(f'Marca:{self.get_marca()}')
        print(f'Tipo de veiculo:{self.get_tipo()}')
        print(f'Modelo:{self.get_modelo()}')
        print(f'Cor:{self.get_cor()}')
        print(f"A força é: {self.is_forca()}")

    def set_forca(self,status):
        if self._forca and status:
            print("ele é potente")
        elif not self._forca and not status:
            print("ele não é potente")
        elif not self._forca and status:
            self._forca = status
            print("ele ficou forte")
        else:
            self._forca = status
            print("ele ficou Fraco")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, potente=True, fraco=False):
        super().__init__(marca,modelo,cor,potente,fraco)
        self.acelerar = False
        self.frear = True
        self.mudar_direcao = False
        self.velocidade_normal = True

    def apresentar(self):
        print("Carro")
        print(f'Marca:{self.get_marca()}')
        print(f'Modelo:{self.get_modelo()}')
        print(f'Cor:{self.get_cor()}')
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




v1 = Veiculo( "carro",  "Aston Martin", "One-77 ", "cinza ")
v1._forca = True
v1.set_forca(True)
v1.apresentar()
print("-"* 20)

v2 = Veiculo( "caminhão", "Volvo", "Volvo VM", "preto")
v2.set_forca  (False)
v2.apresentar()
print("-"* 20)

v3 = Veiculo( "moto", "Shineray", "Shineray 250F", "branco")
v3._forca = True
v3.set_forca(True)
v3.apresentar()
print("-"* 20)

c1 = Carro("Hatch", "Fiat", "branco")
c1.apresentar()
c1.normal()
c1.acelerando()
c1.brecar()
c1.direcao()

print("-"* 20)
