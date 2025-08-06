import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def contar_paginas_pdfs(pasta):
    total_paginas = 0
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.lower().endswith(".pdf"):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            try:
                with open(caminho_arquivo, "rb") as f:
                    leitor = PyPDF2.PdfReader(f)
                    total_paginas += len(leitor.pages)
            except Exception as e:
                print(f"Erro ao ler {nome_arquivo}: {e}")
    return total_paginas

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        total = contar_paginas_pdfs(pasta)
        messagebox.showinfo("Resultado", f"Total de páginas em todos os PDFs: {total}")

# Interface gráfica simples com Tkinter
root = tk.Tk()
root.title("Contador de Páginas em PDFs")

tk.Label(root, text="Clique no botão abaixo para escolher a pasta com PDFs").pack(pady=10)
tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta).pack(pady=10)

root.mainloop()
