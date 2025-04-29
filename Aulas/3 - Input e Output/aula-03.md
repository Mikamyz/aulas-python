### Aula 03: Input e Output - I/O


### Entrada (`Input`)
Como fazer o seu programa "conversar" com a pessoa que o está usando e pedir uma informação? Em Python, usamos a função `input().`

A função `input()` pausa a execução do programa, exibe uma mensagem (opcional) para o usuário e espera que ele digite algo e pressione Enter. O que o usuário digitar é então retornado pela função.

Importante: A função `input()` sempre retorna o que o usuário digitou como uma `string` (texto), mesmo que ele tenha digitado números. Se você precisar usar essa entrada como um número para fazer cálculos, precisará converter a `string` para o tipo numérico desejado (como `int` ou `float`).

```py
nome_usuario = input("Digite o seu nome: ") # Pede o nome e armazena na variável nome_usuario
print("Olá,", nome_usuario)

# Exemplo pedindo um número:
idade_str = input("Digite a sua idade: ") # Pede a idade (retorna como texto)
idade_int = int(idade_str)                # CONVERTE a string para um número inteiro

print(f"Você tem {idade_int} anos.")
print(f"Daqui a 10 anos você terá {idade_int + 10} anos.") # Agora podemos fazer cálculos!
```

Neste exemplo, vimos a conversão usando `int()`. Se você esperasse um número com casas decimais, usaria `float()`.

### Saída (Output)
Já usamos a função `print()` nos exercícios anteriores para exibir informações na tela. `print()` é a função mais comum para saída em Python.

Você pode usar `print()` para:

Exibir texto simples: `print("Olá, mundo!")`
Exibir o valor de variáveis: `print(minha_variavel)`
Exibir múltiplos itens (separados por vírgula): `print("Seu nome é", nome_usuario, "e você tem", idade_int, "anos.")`
Exibir texto formatado (usando `f-strings`,): `print(f"O resultado é {resultado}"`)

```py
produto = "Notebook"
preco = 1200.50

print("Informações do Produto:") # Texto simples
print("Nome:", produto)          # Texto e variável
print("Preço: R$", preco)       # Texto e variável

# Usando f-string para uma saída mais bonita:
print(f"O produto {produto} custa R${preco:.2f}.") # O ":.2f" formata o float para 2 casas decimais
```

### Conectando com a Lógica de Programação
A lógica de Entrada/Saída é fundamental para a interatividade de um programa. Sem a entrada, o programa não pode receber informações externas para processar. Sem a saída, o programa não pode mostrar os resultados ou comunicar algo ao usuário. A combinação de I/O com variáveis e operações permite criar programas que solicitam dados, processam-nos e apresentam uma resposta útil.

## Resumo:
- `input()`: Usado para obter dados do usuário (sempre retorna uma `string`).
- `print()`: Usado para exibir informações na tela.
- Conversão de tipo (`int()`, `float()`, etc.) é necessária para usar a entrada numérica em cálculos.
- F-strings (`f"..."`) são uma ótima forma de formatar a saída.

### Exercício Prático:
Vamos combinar o que aprendemos! Crie um script Python que:

- Peça ao usuário para digitar o preço de um produto.
- Peça ao usuário para digitar a quantidade desse produto.
- Converta as entradas (que são `strings`) para números apropriados (o preço pode ser `float`, a quantidade pode ser `int`).
- Calcule o valor total (`preço * quantidade`).
- Imprima o valor total de uma forma clara para o usuário, indicando qual é o total.