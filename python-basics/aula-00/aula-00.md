### Aula 00

**Guia Básico de Python para Iniciantes**
Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, conhecida por sua sintaxe clara e legível. É uma ótima escolha para iniciantes e é amplamente utilizada em desenvolvimento web, ciência de dados, inteligência artificial, automação e muito mais.   

### 1. O Que é Python?
- Linguagem popular e versátil.
- Foco na legibilidade do código (menos "sintaxe barulhenta").
- Grande comunidade e vasta biblioteca padrão.
- Funciona em diferentes sistemas operacionais (Windows, macOS, Linux).

### 2. Primeiros Passos: Instalação ou Ambiente Online
Para rodar Python, você precisa de um interpretador. Você pode:

- Instalar Python: Baixe o instalador oficial do site python.org. Certifique-se de marcar a opção "Add Python to PATH" durante a instalação no Windows.
- Usar um Ambiente Online: Sites como Replit, Google Colab ou OnlineGDB permitem escrever e executar código Python diretamente no navegador, sem instalação.

### 3. Sintaxe Básica: Indentação
Diferente de muitas outras linguagens que usam chaves {} para definir blocos de código, Python usa indentação (espaços em branco no início da linha). Isso força um código mais organizado. Geralmente, usa-se 4 espaços para cada nível de indentação.

```python
# Exemplo de indentação
if True:
    print("Este código está dentro do if")
    print("Ele está identado com 4 espaços")
print("Este código está fora do if")
```

Okay, excelente ideia! Vamos começar com um guia básico do Python, cobrindo os fundamentos essenciais. Depois, podemos mergulhar em tópicos específicos, um de cada vez, com explicações mais detalhadas e exercícios de lógica para praticar.

Guia Básico de Python para Iniciantes
Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, conhecida por sua sintaxe clara e legível. É uma ótima escolha para iniciantes e é amplamente utilizada em desenvolvimento web, ciência de dados, inteligência artificial, automação e muito mais.   

1. O Que é Python?

Linguagem popular e versátil.
Foco na legibilidade do código (menos "sintaxe barulhenta").
Grande comunidade e vasta biblioteca padrão.
Funciona em diferentes sistemas operacionais (Windows, macOS, Linux).
2. Primeiros Passos: Instalação ou Ambiente Online

Para rodar Python, você precisa de um interpretador. Você pode:

Instalar Python: Baixe o instalador oficial do site python.org. Certifique-se de marcar a opção "Add Python to PATH" durante a instalação no Windows.
Usar um Ambiente Online: Sites como Replit, Google Colab ou OnlineGDB permitem escrever e executar código Python diretamente no navegador, sem instalação.
3. Sintaxe Básica: Indentação

Diferente de muitas outras linguagens que usam chaves {} para definir blocos de código, Python usa indentação (espaços em branco no início da linha). Isso força um código mais organizado. Geralmente, usa-se 4 espaços para cada nível de indentação.

### 4. Variáveis e Tipos de Dados

Variáveis são usadas para armazenar dados. Você não precisa declarar o tipo de variável; Python infere o tipo automaticamente.

Principais Tipos de Dados:

- `int`: Números inteiros (ex: `10`, `-5`, `0`)
- `float`: Números de ponto flutuante (decimais) (ex: `3.14`, `-0.5`,` 2.0`)
- `str`: Cadeias de caracteres (texto) (ex: `"Olá, mundo!"`, `'Python'`)
- `bool`: Booleanos (Verdadeiro ou Falso) (ex: `True`, `False`)
- `list`: Listas (coleções ordenadas e mutáveis) (ex: [`1`, `2`, `3`], [`'a'`, `'b'`, `'c'`])
- `tuple`: Tuplas (coleções ordenadas e imutáveis) (ex: `(1, 2, 3)`, `('a, b')`)
- `dict`: Dicionários (coleções não ordenadas de pares chave-valor) (ex: `{'nome': 'Ana', 'idade': 30}`)
- `set`: Conjuntos (coleções não ordenadas e únicas) (ex: `{1, 2, 3}`)

```python
nome = "Carlos"   # str
idade = 25        # int
altura = 1.75     # float
tem_carro = False # bool
numeros = [1, 2, 3, 4] # list
```

### 5. Entrada e Saída (I/O)

`print()`: Exibe informações na tela.
`input()`: Permite que o usuário insira dados. A entrada é sempre lida como `str` (string), então pode precisar converter para outros tipos (usando `int()`, `float()`, etc.).

```python
print("Olá, Python!")

nome = input("Qual é o seu nome? ")
print("Olá,", nome)

idade_str = input("Qual é a sua idade? ")
idade = int(idade_str) # Convertendo para int
print("Você tem", idade, "anos.")
```

### 6. Operadores

**Aritméticos:** 
`+` Adição:
`-` Subtração
`*` Multiplicação 
`/` Divisão 
`%` Resto da Divisão / Módulo
`**` Potência 
`//` Divisão Inteira 

**Comparação:**
`==` Igual a
`!=` Diferente de
`<` Menor que
`>` Maior que
`<=` Menor ou igual a
`>=` Maior ou igual a

**Lógicos:** 
`and` e
`or` ou
`not` não

```python
x = 10
y = 5
print(x + y)  # 15
print(x > y)  # True
print((x > 5) and (y < 10)) # True
```

### 7. Estruturas de Controle de Fluxo
- **Condicionais** (`if`, `elif`, `else`): Executa blocos de código dependendo de condições.

```python
temperatura = 25
if temperatura > 30:
    print("Está muito quente!")
elif temperatura > 20:
    print("A temperatura está agradável.")
else:
    print("Está frio.")
```

- **Loops** (`for`, `while`): Repetem a execução de blocos de código.
`for`: Usado para iterar sobre sequências (listas, strings, ranges, etc.).

```python
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Iterando sobre um intervalo de números
for i in range(5): # range(5) gera números de 0 a 4
    print(i)
```

- `while`: Repete enquanto uma condição for verdadeira.

```python
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1 # ou contador += 1
```

### 8. Funções
Blocos de código reutilizáveis. Definidos com a palavra-chave `def`.
```python
def saudar(nome):
    # Esta função saúda a pessoa passada como parâmetro.
    print("Olá,", nome + "!")

# Chamando a função
saudar("Alice")
saudar("Bob")

def somar(a, b):
    return a + b # A palavra-chave return envia um valor de volta

resultado = somar(5, 3)
print(resultado) # 8
```

9. Comentários
Usados para explicar o código. Linhas que começam com `#` são ignoradas pelo interpretador. Comentários de várias linhas podem ser feitos com `"""` `"""` (frequentemente usados como docstrings para funções, classes, etc.).

# Este é um comentário de uma linha

```python
"""
Este é um comentário
de várias linhas.
"""
```

