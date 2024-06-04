from tkinter import *
import requests

class App:
    def __init__(self):

        self.janela = Tk()
        self.janela.title('Consulta Nome do Banco pelo Código')
        self.janela.geometry('665x290')
        self.janela.resizable(width=False, height=False)

        self.Label1 = Label(background='white', font='Arial 14 bold', text='Consulta Nome do Banco pelo Código ')
        self.Label1.place(x=7, y=13, height=49, width=649)
        self.Label2 = Label(font='Arial 14 bold', text='Informe o Código do Banco:')
        self.Label2.place(x=47, y=83, height=30, width=407)
        self.Entry1 = Entry(font='Arial 14 bold', foreground='red', takefocus=True)
        self.Entry1.place(x=384, y=79, height=37, width=100)
        self.Entry1.focus()
        self.Button1 = Button(background='green', font='Arial 16 bold', foreground='white', text='Consultar Banco', command=self.consultar_banco)
        self.Button1.place(x=11, y=128, height=43, width=643)
        self.Label3 = Label(font='Arial 14 bold', text='Resultado da Consulta:')
        self.Label3.place(x=34, y=193, height=30, width=214)
        self.Label4 = Label(background='silver', text='Resposta à consulta à API')
        self.Label4.place(x=253, y=193, height=30, width=387)
        self.Label5 = Label(background='yellow', font='Arial 14 bold', text='Nome do Banco')
        self.Label5.place(x=15, y=240, height=30, width=638)

        self.janela.mainloop()

    def consultar_banco(self):
        cod_banco = self.Entry1.get()
        url = f"https://brasilapi.com.br/api/banks/v1/{cod_banco}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            nome_banco = data.get("name", "Banco Desconhecido")
            self.Label4.config(text=f"Resultado da Consulta: Banco Cadastrado na Base")
            self.Label5.config(text=f"Nome do Banco: {nome_banco}")
        else:
            self.Label4.config(text="Resultado da Consulta: Banco Inválido")
            self.Label5.config(text="Nome do Banco:")

# Criando a aplicação
aplicacao = App()
