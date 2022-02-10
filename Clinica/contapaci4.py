import tkinter
import sqlite3


def conta():
    rootC=tkinter.Tk()
    rootC.title("CONTA PACIENTE")
    rootC.geometry('400x390')
    
    var=tkinter.StringVar(master = rootC)

    H = tkinter.Label(rootC,text="CONTA ",fg="black",font="arial 10 bold")
    H.place(x=50,y=20)

    id = tkinter.Label(rootC,text="ID PACIENTE: ",fg="black",font="arial 8 bold")
    id.place(x=20,y=60)

    P_id = tkinter.Entry(rootC)
    P_id.place(x=100,y=60)

    dd_l = tkinter.Label(rootC,text="DATA: ",fg="black",font="arial 8 bold")
    dd_l.place(x=20,y=100)

    dd = tkinter.Entry(rootC)
    dd.place(x=60,y=100)

    ddp=tkinter.Button(rootC,text="ATUALIZAR DATA",fg="black",font="arial 8 bold")
    ddp.place(x=200,y=100)

    treat = tkinter.Label(rootC,text="TIPO DE TRATAMENTO: ",fg="black",font="arial 8 bold")
    treat.place(x=20,y=140)

    cost = tkinter.Label(rootC,width=9)
    cost.place(x=140,y=200)

    
    #list box
    
    costl = tkinter.Label(rootC,text="CUSTO: ",fg="black",font="arial 8 bold")
    costl.place(x=20,y=175)

    cost_t = tkinter.Label(rootC,width=6)
    cost_t.place(x=70,y=175)

    med_l = tkinter.Label(rootC,text="SELECIONAR MEDICINA: ",fg="black",font="arial 8 bold")
    med_l.place(x=20,y=210)

    medl = tkinter.Entry(rootC,width=4)
    medl.place(x=160,y=210)

    med_ql = tkinter.Label(rootC,text="QUANTIDADE: ",fg="black",font="arial 8 bold")
    med_ql.place(x=20,y=250)

    med = tkinter.Entry(rootC,width=4)
    med.place(x=100,y=250)

    pricel = tkinter.Label(rootC,text="PREÇO: ",fg="black",font="arial 8 bold")
    pricel.place(x=200,y=250)

    price = tkinter.Entry(rootC,width=5)
    price.place(x=250,y=250)

    
    button1 = tkinter.Button(rootC,text="SALVAR",bg='light blue',fg='black')
    button2 = tkinter.Button(rootC,text="SAIR",bg='light blue',fg='black')
    button3 = tkinter.Button(rootC,text="IMPRIMIR",bg='light blue',fg='black')

    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=320)

    button2.pack(side=tkinter.TOP)
    button2.place(x=300,y=320)

    button3.pack(side=tkinter.TOP)
    button3.place(x=180,y=320)
    rootC.mainloop()

