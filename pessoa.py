


class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True, trabalhando=False, salario=0):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = salario

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Data de nascimento: {self.data_nascimento}')
        print( f'Codigo: {self.codigo}')
        print(f'Estudando: {self.estudando}')
        print(f'Trabalhando: {self.trabalhando}')
        if self.trabalhando:
            print(f'Salario: {self.salario}')


    def estudar(self):
        if not self.estudando:
            self.estudando = True
            print(f"{self.nome} começou a estudar!")
        elif self.trabalhando and self.estudando:

            self.salario = self.salario + 300
            print(
                f"começou a estudar e aumentou o seu salario para"
                f"R${self.salario:.2f}"
            )
        else:
            print(f"{self.nome} ja esta estudando")

    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario = 1000
            print(f"{self.nome} começou a trabalhar")
        else:
            print(f"{self.nome} ja esta trabalhando")

class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento,codigo):
        super().__init__(nome,data_nascimento,codigo)
        self.fome =True
        self.chorando = True
        self.dormindo = False
    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Data de nascimento: {self.data_nascimento}')
        print( f'Codigo: {self.codigo}')
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
p1.estudar()
p1.trabalhar()
p1.apresentar()
p1.estudar()

print("-"* 20)

p2 = Pessoa("Yasmin","31/01/2008","ljah")
p2.estudar()
p2.apresentar()
print("-"* 20)

p3 = Pessoa("Sandra","22/11/1975","kais")
p3.estudar()
p3.trabalhar()
p3.apresentar()
p3.estudar()

print("-"* 20)

p4 = Pessoa("Carlos","11/09/1978","oash")
p4.trabalhar()
p4.apresentar()
print("-"* 20)

p5 = Pessoa("Isabelly","28/09/2009","paos")
p5.estudar()
p5.apresentar()
print("-"* 20)

b1 = Bebe("x","04/5/2024","jhef")
b1.apresentar()
b1.chorar()
b1.mamar()
b1.dormir()
b1.trabalhar()

