class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Mundo{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 50

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass


if __name__ == '__main__':
    josemar = Pessoa(nome='Josemar')
    guilherme = Pessoa(josemar, nome='Guilherme')
    print(Pessoa.cumprimentar(guilherme))
    print(id(guilherme))
    print(guilherme.nome)
    print(guilherme.idade)
    for filho in guilherme.filhos:
        print(filho.nome)
    # Atributos dinamicos
    guilherme.sobrenome = 'Brito'
    print(guilherme.sobrenome)
    del guilherme.filhos
    guilherme.olhos = 1
    del guilherme.olhos
    print(guilherme.__dict__)
    print(josemar.__dict__)
    print(Pessoa.olhos)
    print(guilherme.olhos)
    print(josemar.olhos)
    print(id(Pessoa.olhos), id(guilherme.olhos), id(josemar.olhos))
    print(Pessoa.metodo_estatico(), guilherme.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), guilherme.nome_e_atributos_de_classe())

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(josemar, Pessoa))
    print(isinstance(josemar, Homem))
    print(josemar.olhos)
