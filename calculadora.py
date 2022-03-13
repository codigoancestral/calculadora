from tkinter import *
import locale
import math

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

janela = Tk()
janela.title('Calculadora Quântica')

visor = Entry(janela, width=40, borderwidth=5)
visor.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def botaoClique(numero):
  #visor.delete(0, END)
  valorAtual = visor.get()
  if numero == '.' and numero not in valorAtual:
    visor.delete(0, END)
    visor.insert(0, str(valorAtual) + str(numero))
  
  if numero != '.':
    visor.delete(0, END)
    visor.insert(0, str(valorAtual) + str(numero))

def limpaVisor():
  visor.delete(0, END)

def somar():
  global f_numero
  global operacao
  operacao = 'adicao'
  primeiroNumero = visor.get()
  f_numero = float(primeiroNumero)
  visor.delete(0, END)

def subtrair():
  global f_numero
  global operacao
  operacao = 'subtracao'
  primeiroNumero = visor.get()
  f_numero = float(primeiroNumero)
  visor.delete(0, END)

def multiplicar():
  global f_numero
  global operacao
  operacao = 'multiplicacao'
  primeiroNumero = visor.get()
  f_numero = float(primeiroNumero)
  visor.delete(0, END)

def dividir():
  global f_numero
  global operacao
  operacao = 'divisao'
  primeiroNumero = visor.get()
  f_numero = float(primeiroNumero)
  visor.delete(0, END)

def percentagem():
  global f_numero
  global operacao
  operacao = 'percentagem'
  primeiroNumero = visor.get()
  f_numero = float(primeiroNumero)
  visor.delete(0, END)

def raiz2():
  raiz = math.sqrt(float(visor.get()))
  visor.delete(0, END)
  visor.insert(0, raiz)

def modulo():
  modulo = float(visor.get()) * -1
  visor.delete(0, END)
  visor.insert(0, modulo)

def igual():
  segundoNumero = visor.get()
  visor.delete(0, END)
  if operacao == 'adicao':
    visor.insert(0, f_numero + float(segundoNumero))

  if operacao == 'subtracao':
    visor.insert(0, f_numero - float(segundoNumero))

  if operacao == 'multiplicacao':
    visor.insert(0, f_numero * float(segundoNumero))

  if operacao == 'divisao':
    visor.insert(0, f_numero / float(segundoNumero))

  if operacao == 'percentagem':
    visor.insert(0, f_numero * (float(segundoNumero)/100))

  if operacao == 'modulo':
    visor.insert(0, f_numero * -1)

botao1 = Button(janela, text="1", padx=40, pady=20, command=lambda: botaoClique(1))
botao2 = Button(janela, text="2", padx=40, pady=20, command=lambda: botaoClique(2))
botao3 = Button(janela, text="3", padx=40, pady=20, command=lambda: botaoClique(3))
botao4 = Button(janela, text="4", padx=40, pady=20, command=lambda: botaoClique(4))
botao5 = Button(janela, text="5", padx=40, pady=20, command=lambda: botaoClique(5))
botao6 = Button(janela, text="6", padx=40, pady=20, command=lambda: botaoClique(6))
botao7 = Button(janela, text="7", padx=40, pady=20, command=lambda: botaoClique(7))
botao8 = Button(janela, text="8", padx=40, pady=20, command=lambda: botaoClique(8))
botao9 = Button(janela, text="9", padx=40, pady=20, command=lambda: botaoClique(9))
botao0 = Button(janela, text="0", padx=40, pady=20, command=lambda: botaoClique(0))
botaoLimpar       = Button(janela, text="C", padx=39, pady=20, command=lambda: limpaVisor())
botaoSomar        = Button(janela, text="+", padx=41, pady=20, command=lambda: somar())
botaoSubtrair     = Button(janela, text="-", padx=41, pady=20, command=lambda: subtrair())
botaoMultiplicar  = Button(janela, text="*", padx=41, pady=20, command=lambda: multiplicar())
botaoDividir      = Button(janela, text="/", padx=40, pady=20, command=lambda: dividir())
botaoIgual        = Button(janela, text="=", padx=41, pady=20, command=lambda: igual())
botaoPercentagem  = Button(janela, text="%", padx=39, pady=20, command=lambda: percentagem())
botaoRaiz2        = Button(janela, text="√", padx=39, pady=20, command=lambda: raiz2())
botaoModulo       = Button(janela, text="+-", padx=36, pady=20, command=lambda: modulo())
botaoVirgula      = Button(janela, text=",", padx=41, pady=20, command=lambda: botaoClique('.'))

botao1.grid(row=4, column=0)
botao2.grid(row=4, column=1)
botao3.grid(row=4, column=2)

botao4.grid(row=3, column=0)
botao5.grid(row=3, column=1)
botao6.grid(row=3, column=2)

botao7.grid(row=2, column=0)
botao8.grid(row=2, column=1)
botao9.grid(row=2, column=2)

botao0.grid(row=5, column=1)

botaoLimpar.grid(row=1, column=0)
botaoRaiz2.grid(row=1, column=1)
botaoPercentagem.grid(row=1, column=2)
botaoDividir.grid(row=1, column=3)
botaoMultiplicar.grid(row=2, column=3)
botaoSubtrair.grid(row=3, column=3)
botaoSomar.grid(row=4, column=3)
botaoModulo.grid(row=5, column=0)
botaoVirgula.grid(row=5, column=2)
botaoIgual.grid(row=5, column=3)

janela.mainloop()

