# DivPDF

**DivPDF** é uma pequena aplicação desenvolvida para facilitar o processo de **separar** e **renomear arquivos PDF**.

## 🎯 Funcionalidade

A aplicação permite:

- Fazer o **upload de um arquivo PDF** que será dividido página por página.
- Escolher uma **pasta de destino** para salvar os arquivos recortados.
- **Renomear os arquivos automaticamente**, com base em um arquivo Excel opcional.

## 📋 Como funciona

1. O usuário **envia um arquivo PDF**.
2. Escolhe uma **pasta local para salvar** os arquivos PDF recortados.
3. Pode, **opcionalmente**, enviar um **arquivo Excel (.xlsx)** que contenha:
   - Uma coluna chamada `descrição` → usada para o nome do arquivo.
   - Uma coluna chamada `vencimento` → atualmente obrigatória, mas futuramente será opcional.
4. O sistema então:
   - **Divide o PDF em páginas individuais**.
   - Renomeia os arquivos:
     - Se o Excel foi fornecido: usa os valores da coluna `descrição`, de forma sequencial.
     - Caso contrário: usa nomes genéricos como `arquivo_1.pdf`, `arquivo_2.pdf`, etc.

## 💻 Tecnologias utilizadas

- Python
- PyPDF2 
- pandas (para leitura do Excel)
- tkinter (interface gráfica)

---

**Desenvolvido por [Alexia Rodrigues](https://github.com/alexias1) e [José Arthur](https://github.com/WellPertter)**
