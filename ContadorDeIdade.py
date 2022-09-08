from cProfile import label
from tkinter import *
from tkinter import ttk
from turtle import width
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# cores ----------

cor1 = "#3b3b3b"
cor2 = "#36154a"
cor3 = "#ffffff"
cor4 = "#e9963f"

#-----------------

janela = Tk()
janela.title('Calculadora de Idade')
janela.geometry('310x400')

# separacao da tela --------------------------

parte_cima = Frame(janela,
                   width=310,
                   height=140,
                   pady=0,
                   padx=0,
                   relief=FLAT,
                   bg=cor2)

parte_cima.grid(row=0, column=0)

parte_baixo = Frame(janela,
                    width=310,
                    height=400,
                    pady=0,
                    padx=0,
                    relief=FLAT,
                    bg=cor1)

parte_baixo.grid(row=1, column=0)

#-----------------------------------------------
# Label das telas ------------------------------

# label tela de cima ----------

label_calculadora = Label(parte_cima,
                          text="Calculadora",
                          width=25,
                          height=1,
                          padx=3,
                          relief=FLAT,
                          anchor=CENTER,
                          font=('Ivy 15 bold'),
                          bg=cor2,
                          fg=cor3)

label_calculadora.place(x=0, y=25)

label_De_Idade = Label(parte_cima,
                       text="DE IDADE",
                       width=25,
                       height=1,
                       padx=3,
                       relief=FLAT,
                       anchor=CENTER,
                       font=('Ivy 30 bold'),
                       bg=cor2,
                       fg=cor4)

label_De_Idade.place(x=-150, y=50)

#--- Função de calcular idade----------------------


def calcular():

    inicial = cal_1.get()
    terminal = cal_2.get()

    dia, mes, ano = [int(f) for f in inicial.split('/')]

    #----------convertento em formato date time -------

    data_inicial = date(ano, mes, dia)

    dia_2, mes_2, ano_2 = [int(f) for f in terminal.split('/')]

    #----------convertento em formato date time -------

    data_nascimento = date(ano_2, mes_2, dia_2)

    ano = relativedelta(data_inicial, data_nascimento).years
    mes = relativedelta(data_inicial, data_nascimento).months
    dia = relativedelta(data_inicial, data_nascimento).days

    Numero_ano['text'] = ano
    Numero_mes['text'] = mes
    Numero_dia['text'] = dia


#--------------------------------------------------------------------

#------------------------------------
# label tela de baixo --------------------------------------------------

data_inicial = Label(parte_baixo,
                     text="Data inicial",
                     height=1,
                     padx=0,
                     pady=0,
                     relief=FLAT,
                     anchor=NW,
                     font=('Ivy 10 bold'),
                     bg=cor1,
                     fg=cor3)

data_inicial.place(x=20, y=25)

data_nascimento = Label(parte_baixo,
                        text="Data de Nascimento",
                        height=1,
                        padx=0,
                        pady=0,
                        relief=FLAT,
                        anchor=NW,
                        font=('Ivy 10 bold'),
                        bg=cor1,
                        fg=cor3)

data_nascimento.place(x=20, y=55)

cal_1 = DateEntry(parte_baixo,
                  width=13,
                  bg='darkblue',
                  fg=cor3,
                  borderwidth=5,
                  date_patter='dd/mm/y',
                  y=2022)

cal_1.place(x=170, y=25)

cal_2 = DateEntry(parte_baixo,
                  width=13,
                  bg='darkblue',
                  fg=cor3,
                  borderwidth=5,
                  date_patter='dd/mm/y',
                  y=2000)

cal_2.place(x=170, y=55)

#------------ Botao de calcular ---------

BotaoC = Button(parte_baixo,
                command=calcular,
                text="Calcular",
                width=12,
                height=-10,
                padx=3,
                relief=RAISED,
                overrelief=RIDGE,
                anchor=CENTER,
                font=('Ivy 15 bold'),
                bg=cor3,
                fg=cor2)

BotaoC.place(x=70, y=110)

#------------------------------------------------

ano = Label(parte_baixo,
            text="Anos",
            height=1,
            padx=0,
            pady=0,
            relief=FLAT,
            anchor=NW,
            font=('Ivy 20 bold'),
            bg=cor1,
            fg=cor4)

ano.place(x=20, y=205)

mes = Label(parte_baixo,
            text="Mêses",
            height=1,
            padx=0,
            pady=0,
            relief=FLAT,
            anchor=NW,
            font=('Ivy 20 bold'),
            bg=cor1,
            fg=cor4)

mes.place(x=115, y=205)

dia = Label(parte_baixo,
            text="Dias",
            height=1,
            padx=0,
            pady=0,
            relief=FLAT,
            anchor=NW,
            font=('Ivy 20 bold'),
            bg=cor1,
            fg=cor4)

dia.place(x=220, y=205)

Numero_ano = Label(parte_baixo,
                   text="--",
                   height=1,
                   padx=0,
                   pady=0,
                   relief=FLAT,
                   anchor=NW,
                   font=('Ivy 20 bold'),
                   bg=cor1,
                   fg=cor3)

Numero_ano.place(x=20, y=165)

Numero_mes = Label(parte_baixo,
                   text="--",
                   height=1,
                   padx=0,
                   pady=0,
                   relief=FLAT,
                   anchor=NW,
                   font=('Ivy 20 bold'),
                   bg=cor1,
                   fg=cor3)

Numero_mes.place(x=130, y=165)

Numero_dia = Label(parte_baixo,
                   text="--",
                   height=1,
                   padx=0,
                   pady=0,
                   relief=FLAT,
                   anchor=NW,
                   font=('Ivy 20 bold'),
                   bg=cor1,
                   fg=cor3)

Numero_dia.place(x=220, y=165)

#------------------------------------

janela.mainloop()
