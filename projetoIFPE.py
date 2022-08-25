from tkinter import *
from random import randint

janela = Tk()
janela.title('Jokenpô')

def jogo():
    jogador = int(jogada.get())
    if jogador == 0:
        lb6['text'] = 'Player: PEDRA'
    elif jogador == 1:
        lb6['text'] = 'Player: PAPEL'
    elif jogador == 2:
        lb6['text'] = 'Player: TESOURA'
    else:
        lb6['text'] = 'Jogada Inválida'
    itens = ('pedra', 'papel', 'tesoura')
    pc = randint(0, 2)
    if pc == 0: #PC JOGOU PEDRA
        lb7['text'] == 'PC: PEDRA'
        if jogador == 0:
            lb8['text'] = 'EMPATE'
        elif jogador == 1:
            lb8['text'] = 'PLAYER WINS'
        elif jogador == 2:
            lb8['text'] = 'PC WINS'
        else:
            lb8['text'] = 'Jogada Inválida'
    elif pc == 1: #PC JOGOU PAPEL
        lb7['text'] = 'PC: PAPEL'
        if jogador == 0:
            lb8['text'] = 'PC WINS'
        elif jogador == 1:
            lb8['text'] = 'EMPATE'
        elif jogador == 2:
            lb8['text'] = 'PLAYER WINS'
        else:
            lb8['text'] = 'Jogada Inválida'            
    elif pc == 2: #PC JOGOU TESOURA
        lb7['text'] = 'PC: TESOURA'
        if jogador == 0:
            lb8['text'] = 'PLAYER WINS'
        elif jogador == 1:
            lb8['text'] = 'PC WINS'
        elif jogador == 2:
            lb8['text'] = 'EMPATE'
        else:
            lb8['text'] = 'Jogada Inválida'  

#AJUSTES DA TELA INICIAL:

#LABEL DO TÍTULO:
tit = Label(janela, text='JOKENPÔ', width=20, font='arial 20', relief='sunken')
tit.grid(row=0, column=0)

#LABEL DAS OPÇÕES:
lb1 = Label(janela, text='0 - Pedra', font='arial 15', width=20)
lb2 = Label(janela, text='1 - Papel', font='arial 15', width=20)
lb3 = Label(janela, text='2 - Tesoura', font='arial 15', width=20)
lb4 = Label(janela, text='', width=20)

lb1.grid(row=1, column=0, sticky=N)
lb2.grid(row=2, column=0, sticky=N)
lb3.grid(row=3, column=0, sticky=N)
lb4.grid(row=4, column=0)

#LABEL DA ENTRADA DE USUÁRIO:
lb5 = Label(janela, text='Digite a opção: ')
lb5.grid(row=5, column=0, sticky=W)

#ENTRY DA OPÇÃO:
jogada = Entry(janela)
jogada.grid(row=5, column=0, sticky=N)

#BOTÃO:
bt = Button(janela, width=10, text='OK', command=jogo)
bt.grid(row=5, column=0, sticky=E)

#LABEL DO PLACAR E JOGADAS:
lb6 = Label(janela, text='Player: -----')
lb6.grid(row=6, column=0)

lb7 = Label(janela, text='PC: -----')
lb7.grid(row=7, column=0)

lb8 = Label(janela, text='-----')
lb8.grid(row=8, column=0)

janela.geometry('335x350+300+200')
janela.mainloop()
