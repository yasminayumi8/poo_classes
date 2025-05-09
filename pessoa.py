class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True, trabalhando=False, salario=0):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def get_nome(self):
        return self.__nome

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_codigo(self):
        return self.__codigo

    def is_estudando(self):
        return self._estudando

    def is_trabalhando(self):
        return self._trabalhando

    def get_salario(self):
        return self._salario

    def set_salario(self, valor):
        if valor > 0:
            self._salario = valor
        else:
            print("salario invalido")

    def apresentar(self):
        print(f'Nome: {self.get_nome()}\n')
        print(f'Data de nascimento: {self.__data_nascimento}')
        print( f'Codigo: {self.__codigo}')
        print(f'Estudando: {self._estudando}')
        print(f'Trabalhando: {self._trabalhando}')
        if self._trabalhando:
            print(f'Salario: {self._salario}')


    # def estudar(self):
    #     if not self._estudando:
    #         self._estudando = True
    #         print(f"{self.__nome} começou a estudar!")
    #     elif self._trabalhando and self._estudando:
    #
    #         self._salario = self._salario + 300
    #         print(
    #             f"começou a estudar e aumentou o seu salario para"
    #             f"R${self._salario:.2f}"
    #         )
    #     else:
    #         print(f"{self.__nome} ja esta estudandot")

    def set_trabalhar(self, status):
        if self._trabalhando and status:
            print("Ja esta trabalhando")
        elif not self._trabalhando and not status:
            print("Que vida boa")
        elif not self._trabalhando and status:
            self._trabalhando = status
            self.set_salario(1000)
        else:
            self._trabalhando = status
            self.set_salario(0)

    def set_estudar(self, status):
        self._estudando = status
        if status:
            self.set_salario(self.get_salario() +300)



    # def trabalhar(self):
    #     if not self._trabalhando:
    #         self._trabalhando = True
    #         self._salario = 1000
    #         print(f"{self.__nome} começou a trabalhar")
    #     else:
    #         print(f"{self.__nome} ja esta trabalhando")

class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento,codigo):
        super().__init__(nome,data_nascimento,codigo)
        self.fome =True
        self.chorando = True
        self.dormindo = False
    def apresentar(self):
        print(f'Nome: {self.__nome}')
        print(f'Data de nascimento: {self.__data_nascimento}')
        print( f'Codigo: {self.__codigo}')
        if self.fome:
            print(f'Esta com fome')
        else:
            print(f'Nao esta com fome')
        if self.chorando:
            print(f'Esta chorando')
        else:
            print(f'Nao esta chorando')
        if self.dormindo:
            print(f'Esta dormindo')
        else:
            print(f'Nao esta dormindo')
    def mamar(self):
        if self.chorando:
            print(f'o bebezinho esta mamando')
            self.chorando = False
            self.fome = False
        else:
            print(f'o bebezinho nao esta mamando')
    def chorar(self):
        if self.chorando:
            print(f'o bebezinho esta chorando pois esta com fome')
            self.dormindo = False
            self.fome = True
        else:
            print(f'o bebezinho nao esta chorando')
            self.fome = False
    def dormir(self):
        if self.fome:
            print(f'o bebezinho esta com fome e nao esta conseguindo dormir')
            self.chorando = True
            self.fome = True
        else:
            print(f'o bebezinho esta dormindo')
    def acordar(self):
        if self.dormindo:
            print(f'o bebezinho esta acordado')
            self.fome = True
        else:
            print(f'o bebezinho nao esta acordado')
    def trabalhar(self):
        print(f'o bebezinho nao  trabalha')


p1 = Pessoa("lucas","23/09/1990","aghs")
p1.is_estudando()
p1.is_trabalhando()
p1.apresentar()
p1.is_estudando()

print("-"* 20)

p2 = Pessoa("Yasmin","31/01/2008","ljah")
p2.is_estudando()
p2.apresentar()
print("-"* 20)

p3 = Pessoa("Sandra","22/11/1975","kais")
p3.is_estudando()
p3.is_trabalhando()
p3.apresentar()
p3.is_estudando()

print("-"* 20)

p4 = Pessoa("Carlos","11/09/1978","oash")
p4.is_trabalhando()
p4.apresentar()
print("-"* 20)

p5 = Pessoa("Isabelly","28/09/2009","paos")
p5.is_estudando()
p5.apresentar()
print("-"* 20)

b1 = Bebe("x","04/5/2024","jhef")
b1.apresentar()
b1.chorar()
b1.mamar()
b1.dormir()
b1.trabalhar()

