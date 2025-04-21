print("Cadastro")

# Coletando os dados
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = input("Idade: ")
altura = input("Altura (ex: 1,75): ")
estudante_status = input("Estuda? (sim/não): ")

# Convertendo os dados
try:
    idade = int(idade)
except ValueError:
    print("Idade inválida. Use apenas números.")
    exit()

try:
    altura = altura.replace(",", ".")
    altura = float(altura)
except ValueError:
    print("Altura inválida. Use formato como 1,75.")
    exit()

# Exibindo os dados
print("\n--- Perfil do Usuário ---")
print("Nome: ", nome.capitalize(), sobrenome.capitalize())
print(f"Idade: {idade} Anos")
print(f"Altura: {altura} Metros")

# Verificando se estuda
if estudante_status.lower() == "sim":
    print("Estudante: Sim")
elif estudante_status.lower() == "não":
    print("Estudante: Não")
else:
    print("Erro: Digite 'sim' ou 'não'")

print("Cadastro Concluído")
print("------------------------")
