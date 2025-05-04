import json
import os
import csv

ARQUIVO_PRODUTOS = 'produtos.json'

# Carrega os produtos do arquivo JSON, se existir
def carregar_produtos():
    if os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                print("Erro ao ler o arquivo de produtos. Iniciando com lista vazia.")
                return []
    return []

# Salva os produtos no arquivo JSON
def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

# Exibe o menu principal
def exibir_menu():
    print("""
=====================================
     Gerenciamento de Produtos
=====================================
[1] - Listar Produtos
[2] - Cadastrar Produto
[3] - Editar Produto
[4] - Excluir Produto
[5] - Sair
[6] - Buscar Produto por Nome
[7] - Listar Ordenado (Preço ou Quantidade)
[8] - Exportar para CSV          
=====================================
--> Selecione uma Opção: 
""")

# Lista todos os produtos
def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("\nLista de Produtos:")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

# Cadastra um novo produto
def cadastrar_produto(produtos):
    nome = input("Nome do produto: ").strip()
    try:
        preco = float(input("Preço do produto: R$ ").strip())
        quantidade = int(input("Quantidade: ").strip())
    except ValueError:
        print("Erro: preço e quantidade devem ser numéricos.")
        return

    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")

# Edita um produto existente
def editar_produto(produtos):
    listar_produtos(produtos)
    if not produtos:
        return
    try:
        indice = int(input("Digite o número do produto a editar: ").strip()) - 1
        if 0 <= indice < len(produtos):
            produto = produtos[indice]
            print(f"Editando '{produto['nome']}'")

            nome = input("Novo nome (deixe em branco para manter): ").strip()
            preco = input("Novo preço (deixe em branco para manter): ").strip()
            quantidade = input("Nova quantidade (deixe em branco para manter): ").strip()

            if nome:
                produto['nome'] = nome
            if preco:
                try:
                    produto['preco'] = float(preco)
                except ValueError:
                    print("Preço inválido, mantendo valor anterior.")
            if quantidade:
                try:
                    produto['quantidade'] = int(quantidade)
                except ValueError:
                    print("Quantidade inválida, mantendo valor anterior.")

            salvar_produtos(produtos)
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Exclui um produto
def excluir_produto(produtos):
    listar_produtos(produtos)
    if not produtos:
        return
    try:
        indice = int(input("Digite o número do produto a excluir: ").strip()) - 1
        if 0 <= indice < len(produtos):
            produto_removido = produtos.pop(indice)
            salvar_produtos(produtos)
            print(f"Produto '{produto_removido['nome']}' removido com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Buscar produtos por nome
def buscar_produto_por_nome(produtos):
    termo = input("Digite o nome ou parte do nome do produto: ").strip().lower()
    resultados = [p for p in produtos if termo in p['nome'].lower()]
    
    if resultados:
        print("\nProdutos encontrados:")
        for i, produto in enumerate(resultados, start=1):
            print(f"{i}. Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
    else:
        print("Nenhum produto encontrado com esse nome.")

# Ordenar produtos por preço ou quantidade
def listar_ordenado(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("""
[1] - Ordenar por Preço (crescente)
[2] - Ordenar por Preço (decrescente)
[3] - Ordenar por Quantidade (crescente)
[4] - Ordenar por Quantidade (decrescente)
    """)
    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        ordenados = sorted(produtos, key=lambda x: x['preco'])
    elif opcao == '2':
        ordenados = sorted(produtos, key=lambda x: x['preco'], reverse=True)
    elif opcao == '3':
        ordenados = sorted(produtos, key=lambda x: x['quantidade'])
    elif opcao == '4':
        ordenados = sorted(produtos, key=lambda x: x['quantidade'], reverse=True)
    else:
        print("Opção inválida.")
        return

    print("\nProdutos ordenados:")
    for i, produto in enumerate(ordenados, start=1):
        print(f"{i}. Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def exportar_para_csv(produtos):
    if not produtos:
        print("Nenhum produto para exportar.")
        return

    nome_arquivo = 'produtos.csv'
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            campos = ['nome', 'preco', 'quantidade']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
            escritor.writeheader()
            for produto in produtos:
                escritor.writerow(produto)
        print(f"Produtos exportados com sucesso para '{nome_arquivo}'!")
    except Exception as e:
        print(f"Ocorreu um erro ao exportar: {e}")


# Função principal que executa o sistema
def main():
    produtos = carregar_produtos()
    while True:
        exibir_menu()
        opcao = input().strip()
        if opcao == '1':
            listar_produtos(produtos)
        elif opcao == '2':
            cadastrar_produto(produtos)
        elif opcao == '3':
            editar_produto(produtos)
        elif opcao == '4':
            excluir_produto(produtos)
        elif opcao == '5':
            print("Encerrando o sistema...")
            break
        elif opcao == '6':
            buscar_produto_por_nome(produtos)
        elif opcao == '7':
            listar_ordenado(produtos)
        elif opcao == '8':
            exportar_para_csv(produtos)    
            
        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")

# Inicia o programa
if __name__ == "__main__":
    main()
