import tkinter as tk

funcionarios = []

def cadastrar_funcionario():
    matricula = entry_matricula.get()
    rg = entry_rg.get()
    cpf = entry_cpf.get()
    
  
    funcionarios.append({"Matrícula": matricula, "RG": rg, "CPF": cpf})
    
    
    entry_matricula.delete(0, tk.END)
    entry_rg.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    
    
    atualizar_lista_funcionarios()

def atualizar_lista_funcionarios():
    texto_funcionarios.delete(1.0, tk.END)  # Limpa o texto atual
    
    
    for funcionario in funcionarios:
        texto_funcionarios.insert(tk.END, f"Nome: {funcionario['Matrícula']}\n")
        texto_funcionarios.insert(tk.END, f"RG: {funcionario['RG']}\n")
        texto_funcionarios.insert(tk.END, f"CPF: {funcionario['CPF']}\n\n")


root = tk.Tk()
root.title("Cadastro de Funcionário")

label_matricula = tk.Label(root, text="Nome:")
label_matricula.grid(row=0, column=0, padx=10, pady=5)
entry_matricula = tk.Entry(root)
entry_matricula.grid(row=0, column=1, padx=10, pady=5)

label_rg = tk.Label(root, text="RG:")
label_rg.grid(row=1, column=0, padx=10, pady=5)
entry_rg = tk.Entry(root)
entry_rg.grid(row=1, column=1, padx=10, pady=5)

label_cpf = tk.Label(root, text="CPF:")
label_cpf.grid(row=2, column=0, padx=10, pady=5)
entry_cpf = tk.Entry(root)
entry_cpf.grid(row=2, column=1, padx=10, pady=5)

botao_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_funcionario)
botao_cadastrar.grid(row=3, columnspan=2, padx=10, pady=10)

label_lista_funcionarios = tk.Label(root, text="Funcionários cadastrados:")
label_lista_funcionarios.grid(row=4, column=0, padx=10, pady=5, columnspan=2)
texto_funcionarios = tk.Text(root, width=40, height=10)
texto_funcionarios.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Rodando a aplicação
root.mainloop()
