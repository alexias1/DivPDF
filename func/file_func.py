#Funções
import tkinter as tk
from tkinter import filedialog
import os

def selecionar_arquivo(entrada_widget):
    arquivo = filedialog.askopenfilename(title="Selecione um pdf")
    entrada_widget.delete(0, tk.END)
    entrada_widget.insert(0, arquivo)

def selecionar_pasta(saida_widget):
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    saida_widget.delete(0, tk.END)
    saida_widget.insert(0, pasta)

def selecionar_arquivo_excel(entrada_excel_widget):
    #Define o caminho padrão para o arquivo "ordem.txt" na mesma pasta do programa
    arquivo_excel = filedialog.askopenfilename(title="Selecione um arquivo excel", initialdir=os.getcwd(), filetypes=[("Arquivos Excel", "*.xls;*.xlsx")])
    entrada_excel_widget.delete(0, tk.END)
    entrada_excel_widget.insert(0, arquivo_excel)
