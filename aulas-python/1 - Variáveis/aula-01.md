### Aula 01 - Variáveis
O que são Variáveis?
Imagine que você tem uma caixa onde guarda alguma informação que vai precisar usar depois. No mundo da programação, essa "caixa" é o que chamamos de variável.

Uma variável é basicamente um nome que damos a um espaço na memória do computador para armazenar um valor. Esse valor pode ser um número, um texto, uma verdade/falsidade, etc.

Em Python, criar uma variável é super simples. Você apenas escolhe um nome para ela e usa o sinal de igual (`=`) para atribuir um valor a ela.

Exemplo:

```py
nome = "Maria" # Criamos uma variável chamada 'nome' e guardamos o texto "Maria" nela
idade = 18      # Criamos uma variável chamada 'idade' e guardamos o número 18 nela
altura = 1.75   # Criamos uma variável chamada 'altura' e guardamos o número 1.75 nela
```

Aqui, `nome`, `idade` e `altura` são nomes de variáveis. "`Maria`", `18` e `1.75` são os valores armazenados nelas.

### O que são Tipos de Dados?
Os Tipos de Dados dizem respeito à natureza da informação que está sendo armazenada na variável. **O Python é uma linguagem de tipagem dinâmica, o que significa que você não precisa dizer explicitamente qual o tipo da variável quando a cria**; o Python descobre isso automaticamente com base no valor que você atribui a ela.

Vamos ver os tipos de dados mais comuns:

1. Inteiro (`int`): Números inteiros, positivos ou negativos, sem casas decimais.
    - Exemplo: `10`, `-5`, `0`

2. Ponto Flutuante (`float`): Números com casas decimais.
    - Exemplo: `3.14`, `-0.5`, `100.0`

3. String (`str`): Sequências de caracteres (texto). Elas são geralmente definidas entre aspas simples (`'`) ou duplas (`"`).
    - Exemplo: `"Olá, mundo!"`, `'Python é legal'`, `"123"` (números entre aspas são tratados como texto!)

4. Booleano (`bool`): Representa um valor verdadeiro (`True`) ou falso (`False`). Usado frequentemente em lógica para tomar decisões.
    - Exemplo: `True`, `False`

### Conectando com a Lógica de Programação
A lógica aqui é que, ao resolver um problema com um programa, você precisa armazenar informações temporariamente ou permanentemente. As variáveis são as ferramentas que usamos para isso. Escolher o tipo de dado correto para armazenar a informação (um número inteiro para idade, um texto para nome, etc.) é crucial para que as operações e cálculos que faremos depois funcionem corretamente.

Por exemplo, você pode somar dois números inteiros ou flutuantes, mas não faz sentido somar um número com um texto diretamente, a menos que você converta um deles.

**Resumo:**
- Variável: Um nome para um espaço na memória que armazena um valor.
- Tipos de Dados: A categoria do valor armazenado (inteiro, decimal, texto, verdadeiro/falso, etc.).
- Python identifica o tipo de dado automaticamente.

### Exercício Prático:
Vamos colocar isso em prática! Crie um pequeno script Python que:

- Crie uma variável chamada `nome_completo` e atribua a ela o seu nome completo (como texto).
- Crie uma variável chamada `ano_nascimento` e atribua a ela o ano em que você nasceu (como número inteiro).
- Crie uma variável chamada `altura_em_metros` e atribua a ela a sua altura (como número decimal).
- Crie uma variável chamada `eh_estudante` e atribua a ela `True` se você for estudante, ou `False` caso contrário (como booleano).
- Depois de criar as variáveis, imprima na tela o valor de cada uma delas usando a função `print()`.