# Exibindo Dados
produto = "Bloodborne - PS4"
preco = 299.99
print("Informações do Produto:")
print("Nome: ", produto)
print("Preço: R$", preco)

# Colentando Dados
nome_produto = input("Digite o nome do Produto: ") # Só pra informação msm
preco_produto = input("Digite o preço do Produto: ")
quantidade_produto = input("Quantidade do Produto: ")

# Convertendo Dados
preco_produto = preco_produto.replace(",", ".") # Caso o user coloque ,
preco_produto = float(preco_produto)
quantidade_produto = int(quantidade_produto)

# Calculando o valor total
valor_total = preco_produto * quantidade_produto
print(f"Valor Total: {valor_total}")

# Checkout
print("Checkout")
print(f"Seu Checkout: Produto: {produto} Valor: {preco} Quantidade: {quantidade_produto} Valor Total: {valor_total}")