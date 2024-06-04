import sqlite3

def create_database():
    connection = sqlite3.connect('alunos.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                        matricula TEXT PRIMARY KEY,
                        nome TEXT NOT NULL)''')
    connection.commit()
    connection.close()

create_database()




import sqlite3
from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Inclusão de Alunos')
        self.janela.geometry("540x230")
        self.janela.resizable(width=False, height=False)

        self.Label1 = Label(self.janela, font='Arial 16 bold', text='Matrícula:')
        self.Label1.place(x=13, y=22, height=30, width=130)
        self.Entry1 = Entry(self.janela, font='Arial 16 bold', foreground='Red')
        self.Entry1.place(x=137, y=21, height=32, width=198)
        self.Label2 = Label(self.janela, font='Arial 16 bold', text='Nome do Aluno:')
        self.Label2.place(x=13, y=68, height=30, width=194)
        self.Entry2 = Entry(self.janela, font='Arial 16 bold', foreground='Blue')
        self.Entry2.place(x=199, y=69, height=30, width=311)
        self.Button1 = Button(self.janela, font='Arial 12 bold', text='Incluir Aluno no Banco de Dados', command=self.incluir_aluno)
        self.Button1.place(x=22, y=116, height=36, width=488)
        self.Label3 = Label(self.janela, background='Gray', text='')
        self.Label3.place(x=22, y=168, height=35, width=488)

        self.create_database()

        self.janela.mainloop()

    def create_database(self):
        connection = sqlite3.connect('alunos.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                            matricula TEXT PRIMARY KEY,
                            nome TEXT NOT NULL)''')
        connection.commit()
        connection.close()

    def incluir_aluno(self):
        matricula = self.Entry1.get()
        nome = self.Entry2.get()
        
        if matricula and nome:
            connection = sqlite3.connect('alunos.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM registros WHERE matricula = ?", (matricula,))
            record = cursor.fetchone()
            
            if record:
                self.Label3.config(text='Matrícula já Cadastrada', fg='red')
            else:
                cursor.execute("INSERT INTO registros (matricula, nome) VALUES (?, ?)", (matricula, nome))
                connection.commit()
                self.Label3.config(text='Aluno Cadastrado com Sucesso!!!', fg='green')
                
                cursor.execute("SELECT * FROM registros")
                all_records = cursor.fetchall()
                print("Alunos cadastrados:")
                for rec in all_records:
                    print(f"Matrícula: {rec[0]}, Nome: {rec[1]}")
                
            connection.close()
        else:
            self.Label3.config(text='Preencha todos os campos', fg='red')

aplicacao = App()
