"""Sou o Daniel Bernardes Cardoso
Esse é o meu primeiro jogo
É um jogo de super trunfo
Espero que goste (: """
# Importes do python
from tkinter import Tk
# Pip install PILLOW
from PIL import ImageTk, Image
# Importes dos meus arquivos
from blibiotecas import Tela, Button, Label
from blibiotecas.selecionaCartas import selecionaJogador, Arquivo

def jogar(maquina, confirmar):
    global v2
    global contador
    global selecionados
    x = v2.abilidade('não')
    if x != "":
        if contador >= 2:
            selecionados = []
        confirmar.place_forget()
        contador += 1
        v2.mostrarAbilidades(maquina, 'maquina')
        pontosMaquina = Label(v2, textvariable=v2.pontosMaquina, bg="#FFFFFF", font='Arial 12', fg='red')
        pontosMaquina.place(x=480, y=100)
        v2.listaLimpeza.append(pontosMaquina)
        mensagemFinal = Label(v2, text=v2.abilidade('sim'), bg='#000000', fg='#FFC600', font='Arial 14')
        mensagemFinal.place(x=300, y=20)
        v2.listaLimpeza.append(mensagemFinal)
        proximo = Button(v2, text="continuar")
        proximo.place(x=93, y=420)
        v2.listaLimpeza.append(proximo)
        if contador >= 3:
            proximo["command"] = lambda: v2.final(proximo)
            v2.listaLimpeza.append(proximo)
            contador = 0
        else:
            proximo["command"] = v2.rodada

# Função que cria a rodada
def rodadas():
    global v2
    global contador
    v2.aparecerRodada()
    jogador = selecionaJogador(selecionados)
    maquina = selecionaJogador(selecionados)
    confirmar = Button(v2, text="Confirmar", bg="Snow", command=lambda: jogar(maquina, confirmar))
    confirmar.place(x=93, y=420)
    v2.listaLimpeza.append(confirmar)
    aparecerContador = Label(v2, text=f'Rodada: {contador+1}/3', font='Arial 11')
    aparecerContador.place(x=400, y=420)
    v2.mostrarAbilidades(jogador, 'jogador')
    pontosJogador = Label(v2, textvariable=v2.pontosJogador, bg="#FFFFFF", font='Arial 12', fg='red')
    pontosJogador.place(x=230, y=100)
    v2.listaLimpeza.append(aparecerContador)
    v2.listaLimpeza.append(pontosJogador)

# Preparando as imagens
def verImagens():
    img = Image.open("imagens/telaInicial.png")
    imgInicial = ImageTk.PhotoImage(img)
    img = Image.open('imagens/fundo.gif')
    imgFundo = ImageTk.PhotoImage(img)
    img = Image.open('imagens/carta.png')
    imgCarta = ImageTk.PhotoImage(img)
    img = Image.open('imagens/setaDireita.gif')
    imgSetaDireita = ImageTk.PhotoImage(img)
    img = Image.open('imagens/setaEsquerda.gif')
    imgSetaEsquerda = ImageTk.PhotoImage(img)
    img = Image.open('imagens/setaDireitaDesativada.png')
    imgSeDiDes = ImageTk.PhotoImage(img)
    img = Image.open('imagens/setaEsquerdaDesativada.png')
    imgSeEsDes = ImageTk.PhotoImage(img)
    v2.novasImagens(imgInicial, imgFundo, imgCarta, imgSetaDireita, imgSetaEsquerda, imgSeEsDes, imgSeDiDes)


# Menu
contador = 0
v1 = Arquivo("Novascartas.txt")
selecionados = []
# Criando a tela
janela = Tk()
janela.title('super trunfo')
janela.geometry("500x500+400+200")
janela.resizable(False, False)
v2 = Tela(janela, rodada=rodadas, criarCarta=v1.novaCarta, verCartas=v1.exibir)
v1.passarTela(v2)
v1.lerArquivo()
verImagens()
v2.telaInicial()
v2.place(x=0, y=0)
janela.mainloop()
