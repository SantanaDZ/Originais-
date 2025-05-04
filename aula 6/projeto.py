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
=====================================
--> Selecione uma Opção: 
""")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("\nLista de Produtos:")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    quantidade = int(input("Quantidade: "))
    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print("Produto cadastrado com sucesso!")

def editar_produto(produtos):
    listar_produtos(produtos)
    if not produtos:
        return
    try:
        indice = int(input("Digite o número do produto a editar: ")) - 1
        if 0 <= indice < len(produtos):
            nome = input("Novo nome (deixe em branco para manter o atual): ")
            preco = input("Novo preço (deixe em branco para manter o atual): ")
            quantidade = input("Nova quantidade (deixe em branco para manter o atual): ")

            if nome:
                produtos[indice]['nome'] = nome
            if preco:
                produtos[indice]['preco'] = float(preco)
            if quantidade:
                produtos[indice]['quantidade'] = int(quantidade)
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def excluir_produto(produtos):
    listar_produtos(produtos)
    if not produtos:
        return
    try:
        indice = int(input("Digite o número do produto a excluir: ")) - 1
        if 0 <= indice < len(produtos):
            produto_removido = produtos.pop(indice)
            print(f"Produto '{produto_removido['nome']}' removido com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def main():
    produtos = []
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
        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
