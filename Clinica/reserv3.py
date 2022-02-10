import sqlite3
import tkinter

def reserva():
    rootR = tkinter.Tk()
    rootR.geometry('390x350')
    rootR.title("RESERVA")

    r_head = tkinter.Label(rootR,text="RESERVAR QUARTOS ",font="Times 10 bold",fg="black")
    r_head.place(x=50,y=20)

    id = tkinter.Label(rootR,text="ID PACIENTE: ",font="arial 8 bold",fg="black")
    id.place(x=30,y=60)

    P_id = tkinter.Entry(rootR)
    P_id.place(x=130,y=90)

    room = tkinter.Label(rootR,text="TIPO DE QUARTO: ",font="arial 8 bold",fg="black")
    room.place(x=30,y=90)

    rid = tkinter.Entry(rootR)
    rid.place(x=110,y=60)

    valoq = tkinter.Label(rootR,text="ACOMPANHANTE(S): ",font="arial 8 bold",fg="black")
    valoq.place(x=30,y=120)

    valom = tkinter.Entry(rootR)
    valom.place(x=150,y=120)

    datE = tkinter.Label(rootR,text="DATA ENTRADA: ",font="arial 8 bold",fg="black")
    datE.place(x=30,y=150)

    dat = tkinter.Entry(rootR)
    dat.place(x=130,y=150)
    
    datS = tkinter.Label(rootR,text="DETALHES QUARTO: ",font="arial 8 bold",fg="black")
    datS.place(x=30,y=185)

    daS = tkinter.Entry(rootR)
    daS.place(x=150,y=185)

    submit = tkinter.Button(rootR,text="Cadastrar ",font="arial 8 bold",fg="black")
    submit.place(x=150,y=230)

    button1 = tkinter.Button(rootR,text="SAIR " ,bg='light blue',fg='black')

    button1.pack(side=tkinter.TOP)
    button1.place(x=155,y=290)

    rootR.mainloop()
