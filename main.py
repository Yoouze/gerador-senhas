# modules
import random as rd
import tkinter as tk


# funções
def gerar_senha():
    cMax = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cMin = 'abcdefghijklmnopqrstuvwxyz'
    num = '1234567890'
    especial = '!@#$%&*'
    
    composition = f'{cMax+cMin}{especial}{especial}{num}'
    size = 16
    txt = ''.join(rd.sample(composition, size))
    senha = tk.Label(text='')
    senha['text'] = txt
    senha.place(x=200.0, y=400.0)

# variaveis

#label = tk.Label()


# interface




# janela
janela = tk.Tk()
    #configs
janela.title('Gerador de senhas')
janela.geometry('600x600')
janela.configure(bg='#207985')

canvas = tk.Canvas(
    janela, 
    bg='#207985', 
    height=600,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)


img0 = tk.PhotoImage(file="lock.png")
b0 = tk.Button(
    borderwidth=0,
    highlightthickness=0,
    bg='#207985',
    fg='white',
    text='Gerar uma senha',
    bd=5,
    command=gerar_senha,
    relief="flat")

b0.place(
    x=200.0, y=300.0,
    width=200,
    height=50)


background_img = tk.PhotoImage(file='background.png')
background = canvas.create_image(
    287.5, 187.0, image=background_img)


janela.resizable(False, False)
janela.mainloop()
