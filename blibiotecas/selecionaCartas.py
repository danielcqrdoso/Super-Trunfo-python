from random import randint

# Classe que mexe com o arquivo
class Arquivo:
    def __init__(self, nomeArquivo):
        # Declarando variaveis
        self.nomeArquivo = nomeArquivo
        self.elementos = 0
        self.listaCarta = []
        self.cartaAntiga = {}

    def passarTela(self, tela):
        self.tela = tela

    def lerArquivo(self):
        # Vendo a quantidade de elementos que há no arquivo
        try:
            with open(self.nomeArquivo, "r") as novaCarta:
                for x in novaCarta:
                    self.elementos += 1
        except FileNotFoundError:
            with open(self.nomeArquivo, "w") as novaCarta:
                novaCarta.write("")
        self.quantCartas = round(self.elementos/4)
        # Lendo as cartas
        with open(self.nomeArquivo, "r") as novaCarta:
            for x in range(0, self.quantCartas):
                # lendo as novas cartas e consertando-as

                nome = novaCarta.readline().replace('\n', '')
                forca = novaCarta.readline().replace('\n', '')
                defesa = novaCarta.readline().replace('\n', '')
                magia = novaCarta.readline().replace('\n', '')
                # Trasformando os números em inteiros
                forca = int(forca)
                defesa = int(defesa)
                magia = int(magia)
                # Salvando as cartas
                carta = {
                    'nome': nome,
                    'força': forca,
                    'defesa': defesa,
                    'magia': magia
                }
                self.listaCarta.append(carta)
        return self.listaCarta

    def refazer(self):
        carta = self.cartaAntiga
        with open(self.nomeArquivo, "a") as refator:
            refator.write(f'{carta["nome"]}\n{carta["força"]}\n{carta["defesa"]}\n{carta["magia"]}\n')
        self.cartaAntiga = {}
        self.exibir()

    # Função de excluir carta criada
    def excluir(self, nomeCarta):
        # Separando o arquivo em listas
        with open(self.nomeArquivo, "r") as excluido:
            arquivo = excluido.readlines()
        # Excluindo da lista a carta
        for x in range(0, self.elementos-3, 4):
            if nomeCarta == arquivo[x].replace('\n', ''):
                self.cartaAntiga['nome'] = arquivo[x].replace('\n', '')
                arquivo.pop(x)
                self.cartaAntiga['força'] = int(arquivo[x])
                arquivo.pop(x)
                self.cartaAntiga['defesa'] = int(arquivo[x])
                arquivo.pop(x)
                self.cartaAntiga['magia'] = int(arquivo[x])
                arquivo.pop(x)
                break
        # Rescrevendo sem a carta excluida
        with open(self.nomeArquivo, 'w') as novoArquivo:
            for x in arquivo:
                novoArquivo.write(x)

        # Recaregando a tela
        self.exibir()

    def novaCarta(self):
        self.tela.aparecerCriacaoCartas(self.nomeArquivo)

    def exibir(self):
        # Função que mostra as cartas
        self.tela.limparTela()
        self.listaCarta = []
        self.elementos = 0
        self.lerArquivo()
        self.tela.aparecerCartas(self.quantCartas, self.listaCarta, self.excluir, self.refazer, self.cartaAntiga)

# Função que seleciona a carta
def selecionaJogador(sel):
    # criando cartas
    player1 = {
        'nome': 'Player 1',
        'força': 80,
        'defesa': 60,
        'magia': 0,
    }
    player2 = {
        'nome': 'Player 2',
        'força': 80,
        'defesa': 40,
        'magia': 50,
    }
    player3 = {
        'nome': 'Player 3',
        'força': 90,
        'defesa': 70,
        'magia': 10,
    }
    player4 = {
        'nome': 'Player 4',
        'força': 90,
        'defesa': 50,
        'magia': 0,
    }
    player5 = {
        'nome': 'Player 5',
        'força': 70,
        'defesa': 70,
        'magia': 10,
    }
    player6 = {
        'nome': 'Player 6',
        'força': 50,
        'defesa': 90,
        'magia': 20,
    }
    # Juntando as cartas em uma unica variavel
    players = [player1, player2, player3, player4, player5, player6]
    v1 = Arquivo('Novascartas.txt')
    v = v1.lerArquivo()
    for x in v:
        players.append(x)
    # Sorteando uma carta
    player = len(players)
    a = randint(0, player-1)
    while a in sel:
        a = randint(0, player-1)
    sel.append(a)
    return players[a]

