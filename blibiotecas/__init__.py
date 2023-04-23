from tkinter import Frame, Button, Label, Entry, Radiobutton, StringVar, IntVar, DISABLED
from sys import exit

# Classe que cria a tela
class Tela(Frame):
    # Ajeitando a tela
    def __init__(self, tela, rodada, criarCarta, verCartas):
        super().__init__()
        self['height'] = 500
        self['width'] = 500
        self['bg'] = 'black'
        self.soma = 0
        self.rodada = rodada
        self.criarCarta = criarCarta
        self.verCartas = verCartas
        self.listaLimpeza = []

    # Preparando as imagens
    def novasImagens(self, imgInicial, imgFundo, imgCarta, imgSetaDireita, imgSetaEsquerda, imgSeEsDes, imgSeDiDes):
        self.imgInicial = imgInicial
        self.imgFundo = imgFundo
        self.imgCarta = imgCarta
        self.imgSetaDireita = imgSetaDireita
        self.imgSetaEsquerda = imgSetaEsquerda
        # Seta direita e esquerda desativadas
        self.imgSeEsDes = imgSeEsDes
        self.imgSeDiDes = imgSeDiDes

    # Função que limpa a tela
    def limparTela(self):
        for x in self.listaLimpeza:
            x.destroy()
        self.listaLimpeza = []
        self.soma = 0

    # Função que faz a tela inicial
    def telaInicial(self):
        self.limparTela()
        self.pontosJogador = IntVar()
        self.pontosMaquina = IntVar()
        self.aparecer = Label(self, image=self.imgInicial)
        self.aparecer.place(x=0, y=0)
        # Fazendo os butões
        butao1 = Button(self, text="Jogar", width="12", bg='snow', command=self.rodada,
                        font="TimesNewRoman 12", bd=1, relief="solid")
        butao2 = Button(self, text="Criar carta", width="12", bg='snow', command=self.criarCarta,
                        font="TimesNewRoman 12", bd=1, relief="solid")
        butao3 = Button(self, text="Ver suas cartas", width="12", bg='snow', command=self.verCartas,
                        font="TimesNewRoman 12", bd=1, relief="solid")
        butao4 = Button(self, text="Sair", width="12", bg='snow', command=exit,
                        font="TimesNewRoman 12", bd=1, relief="solid")
        # Posicionando os butões
        butao1.place(x=5, y=110)
        butao2.place(x=130, y=110)
        butao3.place(x=255, y=110)
        butao4.place(x=380, y=110)
        self.listaLimpeza = [butao1, butao2, butao3, butao4, self.aparecer]

    # Função que verifica as abilidades
    def abilidade(self, estado):
        atributo = self.atributoJogador.get()
        if atributo == "":
            escolha = Label(self, text="!!! Escolha uma opção", bg="#000000", fg="Red", font='Arial 14')
            escolha.place(x=270, y=230)
            self.listaLimpeza.append(escolha)
            return ""
        elif estado == "sim":
            if self.cartaJogador[atributo] > self.cartaMaquina[atributo]:
                self.pontosJogador.set(self.pontosJogador.get() + 1)
                return 'O jogador venceu'
            elif self.cartaJogador[atributo] < self.cartaMaquina[atributo]:
                self.pontosMaquina.set(self.pontosMaquina.get() + 1)
                return 'A máquina venceu'
            else:
                self.pontosJogador.set(self.pontosJogador.get() + 1)
                self.pontosMaquina.set(self.pontosMaquina.get() + 1)
                return 'Houve um empate'
        else:
            return " "

    # Função que mostra o resultado final
    def final(self, butao):
        if self.pontosJogador.get() > self.pontosMaquina.get():
            resultado = 'Vencedor: Jogador'
        elif self.pontosJogador.get() < self.pontosMaquina.get():
            resultado = 'Vencedor: Máquina'
        else:
            resultado = 'Empate'
        vencedor = Label(self, text=f'Resultado Final\n{resultado}', font='Arial 20', fg='red', bg='black')
        vencedor.place(x=135, y=250)
        butao['command'] = self.telaInicial

    def mostrarAbilidades(self, jogador, quem):
        # Vendo se é pra mostrar a carta da máquina ou do jogador
        if quem == 'maquina':
            self.cartaMaquina = jogador
            imgCartaMaquina = Label(self, image=self.imgCarta)
            imgCartaMaquina.place(x=257, y=95)
            nomeCarta = Label(self, text="Carta da máquina", bg="#000000", fg="#FFFFFF", font="Arial 13")
            nomeCarta.place(x=310, y=70)
            nomeMaquina = Label(self, text=jogador['nome'], bg="#FFFFFF", font='Arial 12')
            nomeMaquina.place(x=260, y=100)
            forcaMaquina = Label(self, text=jogador['força'], bg="#FFC600", font='Arial 15')
            forcaMaquina.place(x=420, y=234)
            defesaMaquina = Label(self, text=jogador['defesa'], bg="#FFC600", font='Arial 15')
            defesaMaquina.place(x=420, y=298)
            magiaMaquina = Label(self, text=jogador['magia'], bg="#FFC600", font='Arial 15')
            magiaMaquina.place(x=420, y=360)
            limpeza = [imgCartaMaquina, nomeCarta, nomeMaquina, forcaMaquina, defesaMaquina, magiaMaquina]
            for x in limpeza:
                self.listaLimpeza.append(x)
        else:
            self.cartaJogador = jogador
            imgCartaJogador = Label(self, image=self.imgCarta)
            imgCartaJogador.place(x=7, y=95)
            nomeCarta = Label(self, text="Sua carta", bg="#000000", fg="#FFFFFF", font="Arial 13")
            nomeCarta.place(x=90, y=70)
            nomeJogador = Label(self, text=jogador['nome'], bg="#FFFFFF", font='Arial 12')
            nomeJogador.place(x=10, y=100)
            forcaJogador = Label(self, text=jogador['força'], bg="#FFC600", font='Arial 15')
            forcaJogador.place(x=174, y=234)
            defesaJogador = Label(self, text=jogador['defesa'], bg="#FFC600", font='Arial 15')
            defesaJogador.place(x=174, y=298)
            magiaJogador = Label(self, text=jogador['magia'], bg="#FFC600", font='Arial 15')
            magiaJogador.place(x=174, y=360)
            self.atributoJogador = StringVar()
            butaoForca = Radiobutton(self, value="força", variable=self.atributoJogador, bg="#FFC600")
            butaoForca.place(x=10, y=234)
            butaoDefesa = Radiobutton(self, value="defesa", variable=self.atributoJogador, bg="#FFC600")
            butaoDefesa.place(x=10, y=298)
            butaoMagia = Radiobutton(self, value="magia", variable=self.atributoJogador, bg="#FFC600")
            butaoMagia.place(x=10, y=360)
            limpeza = [imgCartaJogador, nomeCarta, nomeJogador, forcaJogador, defesaJogador, magiaJogador, butaoForca,
                       butaoDefesa, butaoMagia]
            for x in limpeza:
                self.listaLimpeza.append(x)

    def aparecerRodada(self):
        self.limparTela()
        fundo = Label(self, image=self.imgFundo)
        fundo.place(x=0, y=0)
        self.listaLimpeza.append(fundo)

    def checagem(self, nome, forca, defesa, magia, nomeArquivo):
        x = 0
        # Verificando o nome
        nome = nome.strip()
        if nome == "":
            self.erroNome['text'] = "!!! O preenchimento desse campo é obrigatório"
            x = 1
        elif len(nome) > 9:
            self.erroNome['text'] = "!!! O nome NÃO pode ultrapassar 9 caracteres"
            x = 1
        else:
            self.erroNome['text'] = ""
        # Verificando a força
        try:
            forca = int(forca)
        except ValueError:
            self.erroForca['text'] = "!!! A força TEM que ser um número inteiro"
            x = 1
        else:
            if forca < 0 or forca > 100:
                self.erroForca['text'] = "!!! Esse campo DEVE estar entre 0 e 100"
                x = 1
            else:
                self.erroForca['text'] = ""
        # Verificando a defesa
        try:
            defesa = int(defesa)
        except ValueError:
            self.erroDefesa['text'] = "!!! A defesa TEM que ser um número inteiro"
            x = 1
        else:
            if defesa < 0 or defesa > 100:
                self.erroDefesa['text'] = "!!! Esse campo DEVE estar entre 0 e 100"
                x = 1
            else:
                self.erroDefesa['text'] = ""
        # Verificando a magia
        try:
            magia = int(magia)
        except ValueError:
            self.erroMagia['text'] = "!!! A magia TEM que ser um número inteiro"
            x = 1
        else:
            if magia < 0 or magia > 100:
                self.erroMagia['text'] = "!!! Esse campo DEVE estar entre 0 e 100"
                x = 1
            else:
                self.erroMagia['text'] = ""
        # Se não haver erro criar a carta
        if x == 0:
            with open(nomeArquivo, 'a') as novaCarta:
                novaCarta.write(f'{nome}\n{forca}\n{defesa}\n{magia}\n')
            self.telaInicial()

    def aparecerCriacaoCartas(self, nomeArquivo):
        self.limparTela()
        # Colocando a imagem de fundo
        imagemFundo = Label(self, image=self.imgFundo)
        imagemFundo.place(x=0, y=0)
        # Criando as menagens de erro
        self.erroNome = Label(self, bg="#000000", fg="Red", font='Arial 11')
        self.erroNome.place(x=110, y=120)
        self.erroForca = Label(self, bg="#000000", fg="Red", font='Arial 11')
        self.erroForca.place(x=110, y=170)
        self.erroDefesa = Label(self, bg="#000000", fg="Red", font='Arial 11')
        self.erroDefesa.place(x=110, y=220)
        self.erroMagia = Label(self, bg="#000000", fg="Red", font='Arial 11')
        self.erroMagia.place(x=110, y=270)
        concluir = Button(self, text='concluir', width="12", bg='snow', fg='red', command=lambda:
                        self.checagem(nome.get(), forca.get(), defesa.get(), magia.get(), nomeArquivo))
        concluir.place(x=200, y=470)
        # Colocando os entrys
        nome = Entry(self, font='Arial 12', width="12")
        forca = Entry(self, font='Arial 12', width="12")
        defesa = Entry(self, font='Arial 12', width="12")
        magia = Entry(self, font='Arial 12', width="12")
        nome.place(x=200, y=150)
        forca.place(x=200, y=200)
        defesa.place(x=200, y=250)
        magia.place(x=200, y=300)
        # Fazendo as frases
        fraseNome = Label(self, text="Nome:", bg="#000000", fg="Snow", font='Arial 11')
        fraseForca = Label(self, text="Força:", bg="#000000", fg="Snow", font='Arial 11')
        fraseDefesa = Label(self, text="Defesa:", bg="#000000", fg="Snow", font='Arial 11')
        fraseMagia = Label(self, text="Magia:", bg="#000000", fg="Snow", font='Arial 11')
        fraseNome.place(x=130, y=150)
        fraseForca.place(x=130, y=200)
        fraseDefesa.place(x=130, y=250)
        fraseMagia.place(x=130, y=300)
        self.listaLimpeza = [nome, forca, defesa, magia, imagemFundo, fraseNome, fraseForca, fraseDefesa, fraseMagia,
                             concluir, self.erroNome, self.erroForca, self.erroDefesa, self.erroMagia]

    # Fazendo as setas da função de ver carta funcionar
    def passarCarta(self, onde):
        # Checando se é para passar ou voltar a carta
        if onde == "direita":
            self.soma += 1
        else:
            self.soma -= 1
        self.qualCarta['text'] = f'Carta {self.soma + 1}/{len(self.listaCarta)}'
        # Se chegar no limite desabilitar o butão
        if self.soma + 1 >= len(self.listaCarta):
            self.butaoAvancar['command'] = desabilitarBotao
            self.butaoAvancar['image'] = self.imgSeDiDes
        else:
            self.butaoAvancar['command'] = lambda: self.passarCarta('direita')
            self.butaoAvancar['image'] = self.imgSetaDireita
        # Se chegar no minimo desativar
        if self.soma - 1 < 0:
            self.butaoVoltar['command'] = desabilitarBotao
            self.butaoVoltar['image'] = self.imgSeEsDes
        else:
            self.butaoVoltar['command'] = lambda: self.passarCarta('esquerda')
            self.butaoVoltar['image'] = self.imgSetaEsquerda
        # Tirando a carta antiga e colocando a outra
        self.nome['text'] = self.listaCarta[self.soma]["nome"]
        self.forca['text'] = self.listaCarta[self.soma]["força"]
        self.defesa['text'] = self.listaCarta[self.soma]["defesa"]
        self.magia['text'] = self.listaCarta[self.soma]["magia"]

    # Função que faz as cartas criadas aparecerem
    def aparecerCartas(self, quantCarta, listaCarta, funcaoExcluir, funcaoRefazer, cartaAntiga):
        self.listaCarta = listaCarta
        # colocando uma imagem de fundo
        imagemFundo = Label(self, image=self.imgFundo)
        imagemFundo.place(x=0, y=0)
        # Se não há cartas, mostre uma mensagem dizendo que não há
        if quantCarta == 0:
            mensagem = Label(self, text='NÃO HÁ CARTAS NO MOMENTO', fg='red', bg='#000000', font='Arial 12')
            mensagem.place(x=130, y=220)
            self.listaLimpeza = [mensagem]
        # Caso há, mostre elas
        else:
            # Mostrar a carta
            carta = Label(self, image=self.imgCarta)
            carta.place(x=132, y=100)
            self.qualCarta = Label(self, text=f'Carta {self.soma + 1}/{len(self.listaCarta)}', bg='#000000', fg='Snow',
                                   font='Arial 14')
            self.qualCarta.place(x=210, y=70)
            self.butaoAvancar = Button(self, command=lambda: self.passarCarta('direita'), image=self.imgSetaDireita,
                                       highlightthickness=0, bd=0)
            self.butaoAvancar.place(x=420, y=220)
            # Se só haver 1 carta desativar o butão de passar
            if quantCarta == 1:
                self.butaoAvancar['command'] = desabilitarBotao
                self.butaoAvancar['image'] = self.imgSeDiDes

            self.butaoVoltar = Button(self, command=desabilitarBotao, image=self.imgSeEsDes, highlightthickness=0, bd=0)
            self.butaoVoltar.place(x=50, y=218)
            butaoRefazer = Button(self, command=funcaoRefazer, bg='#FFC600', text="Refazer", width="5")
            butaoRefazer.place(x=132, y=72)
            if cartaAntiga == {}:
                butaoRefazer['state'] = DISABLED

            butaoExcluir = Button(self, command=lambda: funcaoExcluir(self.listaCarta[self.soma]['nome']), bg='#FFC600',
                                  text="Excluir", width="5")
            butaoExcluir.place(x=328, y=72)
            self.nome = Label(self, text=self.listaCarta[self.soma]["nome"], bg="#FFFFFF", font='Arial 12')
            self.forca = Label(self, text=self.listaCarta[self.soma]["força"], bg="#FFC600", font='Arial 15')
            self.defesa = Label(self, text=self.listaCarta[self.soma]["defesa"], bg="#FFC600", font='Arial 15')
            self.magia = Label(self, text=self.listaCarta[self.soma]["magia"], bg="#FFC600", font='Arial 15')
            self.nome.place(x=136, y=110)
            self.forca.place(x=300, y=240)
            self.defesa.place(x=300, y=307)
            self.magia.place(x=300, y=365)
            self.listaLimpeza = [carta, self.qualCarta, self.butaoVoltar, self.butaoAvancar, self.nome, self.forca,
                                 self.defesa, self.magia, butaoExcluir]
        # Criando o butão de voltar
        voltar = Button(self, text='Voltar', command=self.telaInicial, width="12", bg='snow', fg='red')
        voltar.place(x=200, y=470)
        # Preparando a limpeza
        self.listaLimpeza.append(voltar)
        self.listaLimpeza.append(imagemFundo)

def desabilitarBotao():
    pass
