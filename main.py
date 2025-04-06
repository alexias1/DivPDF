import tkinter as tk
from tkinter import filedialog, Label
import os 
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter

#Funções
def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(title="Selecione um pdf")
    entrada.delete(0, tk.END)
    entrada.insert(0, arquivo)

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    saida.delete(0, tk.END)
    saida.insert(0, pasta)

def selecionar_arquivo_txt():
    #Define o caminho padrão para o arquivo "ordem.txt" na mesma pasta do programa
    arquivo_excel = filedialog.askopenfilename(title="Selecione um arquivo excel", initialdir=os.getcwd(), filetypes=[("Arquivos Excel", "*.xls;*.xlsx")])
    entrada_excel.delete(0, tk.END)
    entrada_excel.insert(0, arquivo_excel)
    
def divPDF():
    reader = PdfReader(entrada.get())

    if entrada_excel.get() != "":
        # Carregar o arquivo Excel
        lista = pd.read_excel(entrada_excel.get(), engine="openpyxl")  # Para arquivos .xlsx
        num = 0
        for pdf in reader.pages:
            writer = PdfWriter()
            writer.add_page(pdf)
            nome = str(lista.iloc[num,0]) + "-" + lista.iloc[num,1] + "-" + lista.iloc[num,2] + '.PDF'
            caminho = saida.get() + "/" +lista.iloc[num,2] + '/'

            if not os.path.exists(caminho):
                os.makedirs(caminho)
            #Configurações de CAMINHO e NOME_DO_ARQUIVO para salvar também
            writer.write(caminho + nome )
            writer.close
            num += 1
            pass
    else:
        num = 1
        for pdf in reader.pages:
            writer = PdfWriter()
            writer.add_page(pdf)
            #Configurações de CAMINHO e NOME_DO_ARQUIVO para salvar também
            writer.write(saida.get() + "/arquivo" + str(num) +".pdf")
            writer.close
            num += 1
            pass
    pass

#Layout da Janela
janela = tk.Tk()
janela.title("DivPDF 2.0")
janela.configure(bg="#2C3E50")

#Centralizar janela
pos_x = (janela.winfo_screenwidth() - 800) // 2
pos_y = (janela.winfo_screenheight() - 200) // 2
janela.geometry(f"{800}x{200}+{pos_x}+{pos_y}")

#Estilos dos botões
estilo_botao = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 10, "bold"),"relief": "raised", "bd": 3, "width": 20, "height": 1}

#Campo de entrada (Arquivo)
label_entrada = tk.Label(janela, text="Selecione um Arquivo:", bg="#2C3E50", fg="white", font=("Arial", 10))
label_entrada.grid(row=0, column=0, padx=10, pady=5, sticky="e")  # "e" significa alinhamento à direita
entrada = tk.Entry(janela, width=60, font=("Arial", 10), bg="white", fg="black", bd=2, relief="sunken")
entrada.grid(row=0, column=1, padx=10, pady=5)
botao_entrada = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo, **estilo_botao)
botao_entrada.grid(row=0, column=2, padx=10, pady=5)

#Campo de entrada (Pasta)
label_saida = tk.Label(janela, text="Escolher Pasta:", bg="#2C3E50", fg="white", font=("Arial", 10))
label_saida.grid(row=1, column=0, padx=10, pady=5, sticky="e")
saida = tk.Entry(janela, width=60, font=("Arial", 10), bg="white", fg="black", bd=2, relief="sunken")
saida.grid(row=1, column=1, padx=10, pady=5)
botao_pasta = tk.Button(janela, text="Escolher Pasta", command=selecionar_pasta, **estilo_botao)
botao_pasta.grid(row=1, column=2, padx=10, pady=5)
saida.insert(0, os.getcwd()) #Preenche automaticamente com o diretório do programa

#Campo de entrada (Arquivo excel)
label_excel = tk.Label(janela, text="Selecionar Arquivo Excel:", bg="#2C3E50", fg="white", font=("Arial", 10))
label_excel.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada_excel = tk.Entry(janela, width=60, font=("Arial", 10), bg="white", fg="black", bd=2, relief="sunken")
entrada_excel.grid(row=2, column=1, padx=10, pady=5)
#Pré-seleciona o arquivo ordem.txt, se ele existir(Deus é fiel)
ordem_txt_path = os.path.join(os.getcwd(), "ordem.txt")
if os.path.exists(ordem_txt_path):
    entrada_excel.insert(0, ordem_txt_path)
botao_excel = tk.Button(janela, text="Selecionar Arquivo Excel", command=selecionar_arquivo_txt, **estilo_botao)
botao_excel.grid(row=2, column=2, padx=10, pady=5)

#Botão de Recortar
botao_cortar = tk.Button(janela, text="Recortar", **estilo_botao, command=divPDF)
botao_cortar.grid(row=3, column=1, padx=10, pady=10)

#Rodapé
rodape = Label(janela, text="Desenvolvido por Alexia Rodrigues e José Arthur - 2025", bg="#2C3E50", fg="white",font=("Arial", 9, "italic"))
rodape.grid(row=4, column=0, columnspan=3, pady=5)

janela.mainloop()