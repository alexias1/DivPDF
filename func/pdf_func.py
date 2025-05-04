import os
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from func import sendWhatsapp

def recortarPDF(reader, entrada_excel, saida):
    nome = 'arquivo_'

    if entrada_excel.get() != '':
        lista = pd.read_excel(entrada_excel.get(), engine="openpyxl")

    num = 0
    for pdf in reader.pages:
        writer = PdfWriter()
        writer.add_page(pdf)
        #Configurações de CAMINHO e NOME_DO_ARQUIVO para salvar também

        if entrada_excel.get() != '':
            #print(str(lista.loc[num, 'Descrição']))
            nome =  str(lista.loc[num, 'Descrição']) + '.pdf'

            if not os.path.exists(saida.get() + "/"+ str(lista.loc[num, 'Vencimento'])):
                os.makedirs(saida.get() + "/"+ str(lista.loc[num, 'Vencimento']))
            
            writer.write(saida.get() + "/"+ str(lista.loc[num, 'Vencimento']) + '/' + nome)
        else:
            writer.write(saida.get() + "/"+ nome + str(num) + '.pdf')

        writer.close
        num += 1
        pass
    pass


def renomearPDF(reader, entrada_excel, saida):
#Carregar o arquivo Excel
    lista = pd.read_excel(entrada_excel.get(), engine="openpyxl")  # Para arquivos .xlsx
    num = 0
    for pdf in reader.pages:
        writer = PdfWriter()
        writer.add_page(pdf)

        #FUTURAMENTE ADICIONAR A PROCURA POR NOME DE COLUNAS DATA VALIDE, DESCRICAO, ENVIO E NÚMERO_ENVIO

        nome = str(lista.iloc[num,0]) + "-" + lista.iloc[num,1] + "-" + lista.iloc[num,2] + '.PDF'
        caminho = saida.get() + "/" +lista.iloc[num,2] + '/'

        if not os.path.exists(caminho):
            os.makedirs(caminho)

        #Configurações de CAMINHO e NOME_DO_ARQUIVO para salvar também
        writer.write(caminho + nome )
        writer.close

        if lista.iloc[num,5] == 'Sim':
            sendWhatsapp.EnviarPDF('', '+' + str(lista.iloc[num,4]), lista.iloc[num,6], lista.iloc[num,1])
        pass


        num += 1
pass

def divPDF(envio, entrada_excel, entrada, saida):
    reader = PdfReader(entrada.get())

    if envio:
        renomearPDF(reader, entrada_excel, saida)
    else:
        recortarPDF(reader, entrada_excel, saida)
    pass