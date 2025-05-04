import tkinter as tk
from tkinter import Label
import os
from .file_func import selecionar_arquivo, selecionar_pasta, selecionar_arquivo_excel
from .pdf_func import divPDF

#Layout da Janela
janela = tk.Tk()
janela.title("DivPDF 3.0")
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
botao_entrada = tk.Button(janela, text="Selecionar Arquivo", command=lambda: selecionar_arquivo(entrada), **estilo_botao)
botao_entrada.grid(row=0, column=2, padx=10, pady=5)

#Campo de entrada (Pasta)
label_saida = tk.Label(janela, text="Escolher Pasta:", bg="#2C3E50", fg="white", font=("Arial", 10))
label_saida.grid(row=1, column=0, padx=10, pady=5, sticky="e")
saida = tk.Entry(janela, width=60, font=("Arial", 10), bg="white", fg="black", bd=2, relief="sunken")
saida.grid(row=1, column=1, padx=10, pady=5)
botao_pasta = tk.Button(janela, text="Escolher Pasta", command=lambda: selecionar_pasta(saida), **estilo_botao)
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
botao_excel = tk.Button(janela, text="Selecionar Arquivo Excel", command=lambda: selecionar_arquivo_excel(entrada_excel), **estilo_botao)
botao_excel.grid(row=2, column=2, padx=10, pady=5)

#Botão de Recortar
botao_cortar = tk.Button(janela, text="Recortar", **estilo_botao, command=lambda: divPDF(False, entrada_excel, entrada, saida))
botao_cortar.grid(row=3, column=1, padx=10, pady=10)

#Botão de Enviar
botao_enviar = tk.Button(janela, text="Enviar", **estilo_botao, command=lambda: divPDF(True, entrada_excel, entrada, saida))
botao_enviar.grid(row=3, column=2, padx=10, pady=5)

#Rodapé
rodape = Label(janela, text="Desenvolvido por Alexia Rodrigues e José Arthur - 2025", bg="#2C3E50", fg="white",font=("Arial", 9, "italic"))
rodape.grid(row=4, column=0, columnspan=3, pady=5)
janela.mainloop()