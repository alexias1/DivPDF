import tkinter as tk
from tkinter import filedialog, Label
import os 
from PyPDF2 import PdfReader, PdfWriter

#Funções
def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(title="Selecione um arquivo")
    entrada.delete(0, tk.END)
    entrada.insert(0, arquivo)

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    saida.delete(0, tk.END)
    saida.insert(0, pasta)
    
def divPDF():
    print(entrada.get())
    reader = PdfReader(entrada.get())
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
janela.title("DivPDF 1.0")
janela.configure(bg="#2C3E50")

#Centralizar janela
pos_x = (janela.winfo_screenwidth() - 500) // 2
pos_y = (janela.winfo_screenheight() - 250) // 2
janela.geometry(f"{500}x{250}+{pos_x}+{pos_y}")

#Estilos dos botões
estilo_botao = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 10, "bold"),"relief": "raised", "bd": 3, "width": 20, "height": 1}

#Campo de entrada (Arquivo)
entrada = tk.Entry(janela, width=60, font=("Arial", 10), bg="white", fg="black", bd=2, relief="sunken")
entrada.pack(pady=10)
botao_entrada = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo, **estilo_botao)
botao_entrada.pack(pady=5)

#Campo de entrada (Pasta)
saida = tk.Entry(janela, width=60, font=("Arial", 10), bg="white", fg="black", bd=2, relief="sunken")
saida.pack(pady=10)
botao_pasta = tk.Button(janela, text="Escolher Pasta", command=selecionar_pasta, **estilo_botao)
botao_pasta.pack(pady=5)
saida.insert(0, os.getcwd()) #Preenche automaticamente com o diretório do programa

#Botão de Recortar
botao_cortar = tk.Button(janela, text="Recortar", **estilo_botao, command=divPDF)
botao_cortar.pack(pady=10)

#Rodapé
rodape = Label(janela, text="Desenvolvido por José Arthur e Alexia Rodrigues - 2025", bg="#2C3E50", fg="white",font=("Arial", 9, "italic"))
rodape.pack(side="bottom", pady=5)

janela.mainloop()