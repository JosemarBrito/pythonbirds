class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Mundo{id(self)}'


if __name__ == '__main__':
    josemar = Pessoa(nome= 'Josemar')
    guilherme = Pessoa(josemar, nome='Guilherme')
    print(Pessoa.cumprimentar(guilherme))
    print(id(guilherme))
    print(guilherme.nome)
    print(guilherme.idade)
    for filho in guilherme.filhos:
        print(filho.nome)

