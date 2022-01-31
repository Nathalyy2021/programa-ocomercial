import tkinter

     
def funcionarios():
    rootE=tkinter.Tk()
    rootE.title("FORMULARIO CADASTRO EQUIPE/DOUTOR")
    rootE.geometry('400x400')

    var=tkinter.StringVar(master = rootE)

    H = tkinter.Label(rootE,text="FUNCIONARIOS ",fg="black",font="arial 10 bold")
    H.place(x=50,y=20)

    l1 = tkinter.Label(rootE,text="FUNCIONARIO ID",fg="black",font="arial 8 bold")
    l1.place(x=50,y=50)

    t1 = tkinter.Entry(rootE)
    t1.place(x=170,y=50)

    l2 = tkinter.Label(rootE,text="NOME FUNCIONARIO",fg="black",font="arial 8 bold")
    l2.place(x=50,y=80)

    t2 = tkinter.Entry(rootE)
    t2.place(x=170,y=80)

    l3 = tkinter.Label(rootE,text="SEXO",fg="black",font="arial 8 bold")    
    l3.place(x=50,y=110)
        #criar variavel
    r1 = tkinter.Radiobutton(rootE,text="Feminino",value="Female")
    r1.place(x=80,y=110)
        #criar variavel
    r2 = tkinter.Radiobutton(rootE,text="Masculino",value="Male")
    r2.place(x=150,y=110)

    l4 = tkinter.Label(rootE,text="IDADE",fg="black",font="arial 8 bold")    
    l4.place(x=50,y=140)

    t3 = tkinter.Entry(rootE)
    t3.place(x=80,y=140)

    l5 = tkinter.Label(rootE,text="TIPO FUNCIONARIO",fg="black",font="arial 8 bold")    
    l5.place(x=50,y=170)

    scrollbar = tkinter.Scrollbar(rootE,width=2)
    scrollbar.place(x=260,y=140)

    lb = tkinter.Listbox(rootE,selectmode="SINGLE",exportselection=0,height=1,width=15)
    lb.insert(tkinter.END,"DOUTOR")
    lb.insert(tkinter.END,"ENFERMEIRO")
    lb.insert(tkinter.END,"RECEPCIONISTA")
    lb.place(x=150,y=170)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)

    l6 = tkinter.Label(rootE,text="SALARIO :")
    l6.place(x=50,y=200)

    t4 = tkinter.Entry(rootE)
    t4.place(x=110,y=200)

    l7 = tkinter.Label(rootE,text="EXPERIENCIA :")
    l7.place(x=50,y=230)

    t5 = tkinter.Entry(rootE)
    t5.place(x=140,y=230)

    l8 = tkinter.Label(rootE,text="TELEFONE :")
    l8.place(x=50,y=260)

    t6 = tkinter.Entry(rootE)
    t6.place(x=140,y=200)

    l9 = tkinter.Label(rootE,text="EMAIL :")
    l9.place(x=50,y=290)

    t7 = tkinter.Entry(rootE)
    t7.place(x=90,y=290)
    rootE.mainloop()
