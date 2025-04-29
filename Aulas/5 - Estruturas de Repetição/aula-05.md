### Aula 05 - Estruturas de Repetição (Loops)
Imagine que você precisa imprimir a palavra "Olá" 10 vezes, ou percorrer todos os itens de uma lista de compras, ou continuar pedindo uma senha ao usuário até que ele digite a correta. Fazer isso escrevendo a mesma linha de código várias vezes seria tedioso e ineficiente.

Os loops nos permitem executar um bloco de código repetidamente. Existem dois tipos principais de loops em Python: `while` e `for`.

O Loop `while` (Enquanto)
O loop `while` executa um bloco de código enquanto uma determinada condição for verdadeira. A condição é verificada no início de cada repetição.

A sintaxe é:

```py
while condicao:
    # Código a ser executado ENQUANTO a condicao for VERDADEIRA
    # É CRUCIAL que algo dentro do loop mude a condicao
    # para que ela eventualmente se torne falsa, evitando LOOP INFINITO!
```

Exemplo:

```py
contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador = contador + 1 # ou contador += 1 - ESSENCIAL para sair do loop!

print("Loop while terminou.")
```

Neste exemplo, o loop continuará executando enquanto `contador` for menor que 5. A cada repetição, o valor de `contador` aumenta em 1. Quando `contador` chegar a 5, a condição `contador` < 5 se torna falsa e o loop termina.

O Loop `for` (Para)
O loop `for` é usado para iterar (percorrer) os itens de uma sequência (como uma string, uma lista - que veremos mais tarde, ou um `range` de números) ou qualquer outro objeto "iterável". Ele executa o bloco de código uma vez para cada item da sequência.

A sintaxe é:
```py
for item in sequencia:
    # Código a ser executado para cada item na sequencia
```

Uma sequência muito comum para usar com for é a gerada pela função `range()`.

A função `range()` cria uma sequência de números.

`range(fim)`: Gera números de 0 até `fim - 1.`
`range(inicio, fim)`: Gera números de `inicio` até `fim - 1.`
`range(inicio, fim, passo)`: Gera números de `inicio` até `fim - 1`, pulando de passo em passo.

Exemplos:

```py
# Iterando sobre números (de 0 a 4)
for i in range(5):
    print("Iteração:", i)

# Iterando sobre os caracteres de uma string
nome = "Python"
for letra in nome:
    print("Letra:", letra)

# Iterando sobre números (de 2 a 10, pulando de 2 em 2)
for numero in range(2, 11, 2):
    print("Número par:", numero)
```

`while` vs `for`
- Use `while` quando você não sabe exatamente quantas vezes o loop precisa rodar, mas tem uma condição para ele parar (ex: "repita enquanto a senha estiver errada").
- Use `for` quando você quer repetir uma ação para cada item em uma sequência ou um número conhecido de vezes (ex: "para cada item nesta lista", "repita 10 vezes").

### Conectando com a Lógica de Programação
Loops representam a lógica de **automação** e **repetição**. Eles nos permitem executar tarefas repetitivas sem escrever o mesmo código várias vezes. Isso torna os programas mais curtos, mais fáceis de ler, manter e modificar. A escolha entre `while` e `for` depende da lógica de repetição que você precisa implementar: baseada em uma condição (`while`) ou na iteração sobre elementos (`for`).

### Resumo:
- Loops: Permitem repetir um bloco de código.
- `while condicao:`: Repete ENQUANTO a condição for verdadeira. Cuidado com loops infinitos!
- `for item in sequencia:`: Repete para cada `item` em uma `sequencia` (como gerada por `range()`, strings, etc.).
- `range():` Função útil para gerar sequências de números para loops for.

### Exercício Prático:
Vamos praticar os loops! Escolha um dos exercícios abaixo (ou faça os dois se quiser praticar mais!):

**Exercício 1 (Usando `while`):**

**Crie um script Python que:**

- Crie uma variável `contador` e inicialize-a com 1.
- Use um loop while para imprimir os números de 1 a 5.
- Certifique-se de atualizar o `contador` dentro do loop para que ele eventualmente termine.

**Exercício 2 (Usando for e range):**

**Crie um script Python que:**

1. Use um loop `for` com a função `range()` para iterar sobre os números de 0 a 9 (inclusive).
2. Dentro do loop, imprima o dobro de cada número.