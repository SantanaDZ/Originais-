import tkinter as tk
from tkinter import ttk, messagebox
import json
import csv
import os

ARQUIVO_JSON = 'produtos.json'

# ---------------- UTILITÁRIOS -------------------

def carregar_produtos():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def salvar_produtos():
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def exportar_para_csv():
    if not produtos:
        messagebox.showinfo("Exportação", "Nenhum produto para exportar.")
        return
    with open("produtos.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "preco", "quantidade"])
        writer.writeheader()
        writer.writerows(produtos)
    messagebox.showinfo("Exportação", "Exportado com sucesso para produtos.csv!")

# ---------------- INTERFACE -------------------

def atualizar_tabela():
    for item in tree.get_children():
        tree.delete(item)
    for i, p in enumerate(produtos, start=1):
        tree.insert("", "end", values=(i, p["nome"], f"R${p['preco']:.2f}", p["quantidade"]))

def adicionar_produto():
    def salvar():
        nome = entry_nome.get()
        try:
            preco = float(entry_preco.get())
            quantidade = int(entry_qtd.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço ou quantidade inválidos.")
            return
        produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        salvar_produtos()
        atualizar_tabela()
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Cadastrar Produto")

    tk.Label(janela, text="Nome:").grid(row=0, column=0)
    tk.Label(janela, text="Preço:").grid(row=1, column=0)
    tk.Label(janela, text="Quantidade:").grid(row=2, column=0)

    entry_nome = tk.Entry(janela)
    entry_preco = tk.Entry(janela)
    entry_qtd = tk.Entry(janela)

    entry_nome.grid(row=0, column=1)
    entry_preco.grid(row=1, column=1)
    entry_qtd.grid(row=2, column=1)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, columnspan=2)

def editar_produto():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um produto.")
        return

    index = int(tree.item(selecionado)['values'][0]) - 1
    produto = produtos[index]

    def salvar():
        nome = entry_nome.get()
        try:
            preco = float(entry_preco.get())
            quantidade = int(entry_qtd.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço ou quantidade inválidos.")
            return
        produto['nome'] = nome
        produto['preco'] = preco
        produto['quantidade'] = quantidade
        salvar_produtos()
        atualizar_tabela()
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Editar Produto")

    tk.Label(janela, text="Nome:").grid(row=0, column=0)
    tk.Label(janela, text="Preço:").grid(row=1, column=0)
    tk.Label(janela, text="Quantidade:").grid(row=2, column=0)

    entry_nome = tk.Entry(janela)
    entry_preco = tk.Entry(janela)
    entry_qtd = tk.Entry(janela)

    entry_nome.insert(0, produto["nome"])
    entry_preco.insert(0, produto["preco"])
    entry_qtd.insert(0, produto["quantidade"])

    entry_nome.grid(row=0, column=1)
    entry_preco.grid(row=1, column=1)
    entry_qtd.grid(row=2, column=1)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, columnspan=2)

def excluir_produto():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um produto.")
        return
    index = int(tree.item(selecionado)['values'][0]) - 1
    confirm = messagebox.askyesno("Excluir", f"Deseja excluir '{produtos[index]['nome']}'?")
    if confirm:
        produtos.pop(index)
        salvar_produtos()
        atualizar_tabela()

# ------------------- APP -----------------------

produtos = carregar_produtos()

root = tk.Tk()
root.title("Gerenciamento de Produtos")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tree = ttk.Treeview(frame, columns=("ID", "Nome", "Preço", "Quantidade"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Preço", text="Preço")
tree.heading("Quantidade", text="Quantidade")
tree.pack()

botao_frame = tk.Frame(root)
botao_frame.pack(pady=10)

tk.Button(botao_frame, text="Cadastrar", command=adicionar_produto).grid(row=0, column=0, padx=5)
tk.Button(botao_frame, text="Editar", command=editar_produto).grid(row=0, column=1, padx=5)
tk.Button(botao_frame, text="Excluir", command=excluir_produto).grid(row=0, column=2, padx=5)
tk.Button(botao_frame, text="Exportar CSV", command=exportar_para_csv).grid(row=0, column=3, padx=5)
tk.Button(botao_frame, text="Sair", command=root.quit).grid(row=0, column=4, padx=5)

atualizar_tabela()
root.mainloop()
