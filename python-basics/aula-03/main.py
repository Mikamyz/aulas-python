print("Calculadora de Orçamento")

# Colentando dados
produto = input("Digite o produto: ")
quantidade = input("Quantidade: ")
preco_unitario = input("Preço unitário: ex: 1.50: ")
desconto = input("Porcentagem de desconto ex: 10%: ")

# Covertendo os dados
quantidade = int(quantidade)
preco_unitario = preco_unitario.replace(",", ".") # Trocando o (,) por (.) para não dar erro
preco_unitario = float(preco_unitario)
desconto = desconto.replace(",", ".")
desconto = float(desconto)

# Calculando
subtotal = quantidade * preco_unitario
valor_desconto = subtotal * desconto / 100
total = subtotal - valor_desconto

# Exibindo os dados
print("--- Resumo do Orçamento ---")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto Aplicado: {desconto}%")
print(f"Valor do Desconto: R$ {desconto:.2f}")
print(f"Totoal a pagar: R$ {total}")
print("---------------------------")
