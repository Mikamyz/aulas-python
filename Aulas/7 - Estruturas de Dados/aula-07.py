
# Definindo a lista
frutas = ["Maçã", "Banana", "Uva"]

# Exibindo a lista
print(f"Lista de Frutas: {frutas}") 
print(f"Fruta: {frutas[0]}") # Primeiro item da lista
print(f"Fruta: {frutas[2]}") # Último item da lista
frutas.append("Manga") # Add item a lista
print(f"Fruta add: {frutas[3]}") # Manga

# Dist
produto = {"Id": 123, "Nome": "Notebook", "Preço": 499.99, "Stock": 100
}

print(produto)
print(produto["Preço"])
produto["Stock"] = produto["Stock"] - 1 # Ou a forma abreviada: produto["Stock"] -= 1
print(produto["Stock"])