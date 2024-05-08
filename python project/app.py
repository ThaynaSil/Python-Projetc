from tkinter import * #Importando biblioteca para a criação do formulario.

def submit_form():
    # Função para coletar os dados dos campos e fazer algo com eles
    name = entry_Nome.get()
    age = entry_Idade.get()
    email = entry_Mat.get()
    phone = entry_Status.get()

janela = Tk()

janela.title("Formulário")

# Ajustar o tamanho da janela
janela.geometry("400x300")  # Largura x Altura

# Criação dos Textos e campos de entrada de dados
Texto_Nome = Label(janela, text="Nome:", font=("Arial", 10))
Texto_Nome.grid(column=0, row=0, sticky="w", pady= 10) #Posição Do Texto
entry_Nome = Entry(janela, font=(10)) 
entry_Nome.grid(column=1, row=0, sticky="w", pady= 10) #Posicao Da Entrada

Texto_Idade = Label(janela, text="Idade:", font=("Arial", 10))
Texto_Idade.grid(column=0, row=1, sticky="w", pady= 10)
entry_Idade = Entry(janela, font=(10))
entry_Idade.grid(column=1, row=1, sticky="w", pady= 10)

Texto_Mat = Label(janela, text="Matrícula:", font=("Arial", 10))
Texto_Mat.grid(column=0, row=2, sticky="w", pady= 10)
entry_Mat = Entry(janela, font=(10))
entry_Mat.grid(column=1, row=2, sticky="w", pady= 10)

Texto_Status = Label(janela, text="Status: Ativo / Inativo", font=("Arial", 10))
Texto_Status.grid(column=0, row=3, sticky="w", pady= 10)
entry_Status = Entry(janela, font=(10))
entry_Status.grid(column=1, row=3, sticky="w", pady= 10)

# Botão para enviar o formulário
submit_button = Button(janela, text=" Enviar ", font=("Arial", 11), command=submit_form) #Criação do botao - Quando clicado chama a função
submit_button.grid(columnspan=3, row=6, column= 1) # Posição na janela

janela.mainloop()


