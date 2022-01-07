import tkinter
from window2 import menu


def GET():
    global userbox,passbox,error
    U1 = userbox.get()
    U2 = passbox.get()
    if (U1=='nat' and U2=='123'):
        menu()

    if (U1=='rob' and U2=='123'):
        menu()

    else:
        
        error=tkinter.Label(bottomframe,text="USUARIO E SENHA INCORRETOS",fg="red",font="bold")
        error.pack()
    
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    
    root = tkinter.Tk()
    root.geometry("500x400")
    topframe = tkinter.Frame(root)
    topframe.pack()

    bottomframe = tkinter.Frame(root)
    bottomframe.pack()

    heading = tkinter.Label(topframe,text="CLINICA ESTRELA GUIA", bg='white',fg='navy blue', font='Times 16 bold')

    username = tkinter.Label(topframe,text="Usuario: ")
    userbox = tkinter.Entry(topframe)

    password = tkinter.Label(bottomframe,text="Senha: ")
    passbox = tkinter.Entry(bottomframe)

    login = tkinter.Button(bottomframe,text="LOGIN",font='arial 8 bold',command=GET)
    
    root.wm_iconbitmap(r'c:\\Users\\OEM\\Desktop\\Hospital_python\\icones\\senha.ico')

    image= tkinter.PhotoImage(file="c:\\Users\\OEM\\Desktop\\Hospital_python\\img\\login.png")
    image=image.subsample(1,1)
    labelimg=tkinter.Label(image=image,height="200",width="200")
    labelimg.pack()

    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("Sistema Clinica Estrela Guia: LOGIN")
    root.mainloop()
Entry()