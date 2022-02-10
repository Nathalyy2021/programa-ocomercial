import tkinter
import sqlite3

     
def funcionarios():
    rootE=tkinter.Tk()
    rootE.title("FORMULARIO CADASTRO EQUIPE/DOUTOR")
    rootE.geometry('400x400')

    var=tkinter.StringVar(master = rootE)

    H = tkinter.Label(rootE,text="FUNCIONARIOS ",fg="black",font="arial 10 bold")
    H.place(x=50,y=20)

    l1 = tkinter.Label(rootE,text="FUNCIONARIO ID: ",fg="black",font="arial 8 bold")
    l1.place(x=50,y=50)

    t1 = tkinter.Entry(rootE)
    t1.place(x=170,y=50)

    l2 = tkinter.Label(rootE,text="NOME FUNCIONARIO: ",fg="black",font="arial 8 bold")
    l2.place(x=50,y=80)

    t2 = tkinter.Entry(rootE)
    t2.place(x=170,y=80)

    l3 = tkinter.Label(rootE,text="SEXO: ",fg="black",font="arial 8 bold")    
    l3.place(x=50,y=110)
        #criar variavel
    r1 = tkinter.Radiobutton(rootE,text="Feminino",value="Female")
    r1.place(x=80,y=110)
        #criar variavel
    r2 = tkinter.Radiobutton(rootE,text="Masculino",value="Male")
    r2.place(x=150,y=110)

    l4 = tkinter.Label(rootE,text="IDADE: ",fg="black",font="arial 8 bold")    
    l4.place(x=50,y=140)

    t3 = tkinter.Entry(rootE)
    t3.place(x=90,y=140)

    l5 = tkinter.Label(rootE,text="TIPO FUNCIONARIO: ",fg="black",font="arial 8 bold")    
    l5.place(x=50,y=170)

    scrollbar = tkinter.Scrollbar(rootE,width=2)
    scrollbar.place(x=260,y=140)

    lb = tkinter.Listbox(rootE,selectmode="SINGLE",exportselection=0,height=1,width=15)
    lb.insert(tkinter.END,"DOUTOR")
    lb.insert(tkinter.END,"ENFERMEIRO")
    lb.insert(tkinter.END,"RECEPCIONISTA")
    lb.place(x=160,y=170)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)

    l6 = tkinter.Label(rootE,text="SALARIO :",fg="black",font="arial 8 bold")
    l6.place(x=50,y=200)

    t4 = tkinter.Entry(rootE)
    t4.place(x=120,y=200)

    l7 = tkinter.Label(rootE,text="EXPERIENCIA :",fg="black",font="arial 8 bold")
    l7.place(x=50,y=230)

    t5 = tkinter.Entry(rootE)
    t5.place(x=140,y=230)

    l8 = tkinter.Label(rootE,text="TELEFONE :",fg="black",font="arial 8 bold")
    l8.place(x=50,y=260)

    t6 = tkinter.Entry(rootE)
    t6.place(x=120,y=260)

    l9 = tkinter.Label(rootE,text="EMAIL :",fg="black",font="arial 8 bold")
    l9.place(x=50,y=290)

    t7 = tkinter.Entry(rootE)
    t7.place(x=100,y=290)

    button1 = tkinter.Button(rootE,text="SALVAR " ,bg='light blue',fg='black')
    button2 = tkinter.Button(rootE,text="SAIR " ,bg='light blue',fg='black')

    button1.pack(side=tkinter.TOP)
    button1.place(x=130,y=320)

    button2.pack(side=tkinter.TOP)
    button2.place(x=230,y=320)
    rootE.mainloop()

