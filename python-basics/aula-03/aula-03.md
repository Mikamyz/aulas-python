### Aula 03: Entrada e Saída (I/O) em Python
A comunicação entre o seu programa e o "mundo exterior" (geralmente o usuário ou arquivos) é feita através de operações de `Entrada (Input)` e `Saída (Output)`, ou I/O. Em Python, as funções mais comuns para isso são `input()` e `print()`.

### 1. A Função `print()`: Exibindo Saída
No básico, vimos que `print()` exibe texto na tela. Agora, vamos ver mais sobre suas capacidades:
- Múltiplos Argumentos: Você pode passar vários itens para `print()`, separados por vírgulas. Por padrão, ele colocará um espaço entre eles.

```py
nome = "João"
idade = 29
print("Olá,", nome, "sua idade é:", idade) # Saída: Olá, João sua idade é: 29
```

- Parâmetro `sep`: Você pode mudar o separador entre os argumentos usando o parâmetro `sep`.

```py
print("Brasil", "Sil", "Sil", sep='-') # Saída: Brasil-Sil-Sil
print("user", "gmail", "com", sep='@') # Saída: user@gmail@com
```

Parâmetro `end`: Por padrão, `print()` adiciona uma quebra de linha (`\n`) no final. Você pode mudar isso com o parâmetro `end`. Isso é útil para imprimir coisas na mesma linha.

```py
print("Carregando", end='...')
print(" Concluído!")
# Saída (na mesma linha): Carregando... Concluído!

print("Item 1", end=' ')
print("Item 2", end=' ')
print("Item 3")
# Saída (na mesma linha): Item 1 Item 2 Item 3
```

- Formatando Saída: Combinar texto e valores de variáveis de forma legível.
    - Concatenação com `+`: Funciona apenas entre strings. Você precisa converter outros tipos para string com `str()`. Pode ficar um pouco confuso com muitas partes.

```py
quantidade = 5
produto = "canetas"
preco_unitario = 2.50
# print("Você comprou " + quantidade + " " + produto) # ERRO! quantidade é int
print("Você comprou " + str(quantidade) + " " + produto) # OK
```

- Método `.format()`: Uma forma mais estruturada de formatar strings (mais antiga que `f-strings`, mas ainda vista).

```py
quantidade = 5
produto = "canetas"
mensagem = "Você comprou {} {}".format(quantidade, produto)
print(mensagem) # Saída: Você comprou 5 canetas

# Com índices ou nomes
mensagem_posicao = "Você comprou {1} {0}".format(quantidade, produto) # Usa o 2o argumento (indice 1), depois o 1o (indice 0)
print(mensagem_posicao) # Saída: Você comprou canetas 5

mensagem_nomeada = "Preço total: R$ {total:.2f} ({} unidades de {})".format(total=quantidade * preco_unitario, quantidade=quantidade, produto=produto) # :.2f formata para 2 casas decimais float
print(mensagem_nomeada)
```

- **F-Strings (Strings Formatadas):** Introduzidas no Python 3.6, são a forma mais moderna, legível e geralmente recomendada. Basta colocar um f antes das aspas e colocar as variáveis (ou até expressões simples) entre chaves {} dentro da string.

```py
quantidade = 5
produto = "canetas"
preco_unitario = 2.50
total = quantidade * preco_unitario

print(f"Você comprou {quantidade} {produto}.")
print(f"O total é R$ {total:.2f}") # :.2f também funciona aqui para formatar float
print(f"Informações: {produto.upper()} - Quantidade: {quantidade}") # Pode chamar métodos também
```

### 2. A Função `input()`: Recebendo Entrada
Vimos que `input()` lê uma linha de texto digitada pelo usuário e a retorna.
- **Sempre String**: Lembre-se, o valor retornado por `input()` é sempre do tipo `str`.

```py
numero_digitado = input("Digite um número: ")
print(type(numero_digitado)) # Saída: <class 'str'>
# Mesmo que você digite "123", o input é a STRING "123"
```

- **Conversão de Tipo:** Se você espera um número (inteiro ou decimal) ou outro tipo de dado, você deve convertê-lo explicitamente.

```py
idade_str = input("Digite sua idade: ")
idade = int(idade_str) # Converte a string lida para inteiro

altura_str = input("Digite sua altura (ex: 1.75): ")
altura = float(altura_str) # Converte a string lida para float

# Como vimos, se a string não puder ser convertida (ex: input("abc") -> int("abc")), ocorrerá um ValueError.
# Lidaremos com isso no tópico de Tratamento de Erros.
```

- **Mensagem de Prompt:** A string que você passa para input() é exibida para o usuário antes de esperar a entrada.

```py
nome = input("Por favor, digite seu nome: ") # "Por favor, digite seu nome: " é a mensagem de prompt
```

### Resumo I/O:

Use `input()` para ler dados do usuário (sempre string).
Use `print()` para exibir informações.
Converta a entrada (`input()`) para o tipo correto (int(), float(), etc.) se necessário.
Use `f-strings` (principalmente), `.format()` ou concatenação para formatar a saída (`print()`).
Use sep e end em `print()` para controlar a separação e o final da saída.