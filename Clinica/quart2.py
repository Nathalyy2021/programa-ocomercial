import sqlite3
import tkinter


def quarto():
    rootQ = tkinter.Tk()
    rootQ.title("Nº QUARTO")
    rootQ.geometry('390x400')

    r_head = tkinter.Label(rootQ,text="PESQUISAR QUARTOS ",font="Times 10 bold",fg="black")
    r_head.place(x=50,y=20)

    id = tkinter.Label(rootQ,text="ID PACIENTE: ",font="arial 8 bold",fg="black")
    id.place(x=30,y=60)

    P_id = tkinter.Entry(rootQ)
    P_id.place(x=130,y=90)

    room = tkinter.Label(rootQ,text="TIPO DE QUARTO: ",font="arial 8 bold",fg="black")
    room.place(x=30,y=90)

    rid = tkinter.Entry(rootQ)
    rid.place(x=110,y=60)

    valoq = tkinter.Label(rootQ,text="VALOR QUARTO: ",font="arial 8 bold",fg="black")
    valoq.place(x=30,y=120)

    valom = tkinter.Entry(rootQ)
    valom.place(x=130,y=120)

    datE = tkinter.Label(rootQ,text="DATA ENTRADA: ",font="arial 8 bold",fg="black")
    datE.place(x=30,y=150)

    dat = tkinter.Entry(rootQ)
    dat.place(x=130,y=150)
    
    datS = tkinter.Label(rootQ,text="DATA SAIDA: ",font="arial 8 bold",fg="black")
    datS.place(x=30,y=180)

    daS = tkinter.Entry(rootQ)
    daS.place(x=110,y=180)

    cr = tkinter.Label(rootQ,text="DETALHES QUARTO: ",font="arial 8 bold",fg="black")
    cr.place(x=30,y=220)

    crs = tkinter.Entry(rootQ)
    crs.place(x=150,y=220)

    submit = tkinter.Button(rootQ,text="Cadastrar ",font="arial 8 bold",fg="black")
    submit.place(x=100,y=270)

    update = tkinter.Button(rootQ,text="Atualizar ",font="arial 8 bold",fg="black")
    update.place(x=230,y=270)

    button1 = tkinter.Button(rootQ,text="SALVAR " ,bg='light blue',fg='black')
    button2 = tkinter.Button(rootQ,text="SAIR " ,bg='light blue',fg='black')

    button1.pack(side=tkinter.TOP)
    button1.place(x=120,y=330)

    button2.pack(side=tkinter.TOP)
    button2.place(x=230,y=330)
    rootQ.mainloop()
