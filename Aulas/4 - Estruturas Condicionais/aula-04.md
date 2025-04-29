### Aula 04 - Estruturas Condicionais
Na vida real, tomamos decisões o tempo todo: "`SE` chover, ENTÃO levo um guarda-chuva". "`SE` estiver sol, ENTÃO vou à praia, `SE` NÃO, vou ao cinema".

Em programação, é a mesma ideia. As estruturas condicionais permitem que o seu código execute um bloco de instruções apenas se uma determinada condição for verdadeira. Caso contrário, ele pode executar outro bloco de instruções ou simplesmente pular aquele trecho.

As palavras-chave principais para isso em Python são `if`, `elif` e `else`.

O `if` (Se)
O `if` é a estrutura condicional mais básica. Ele verifica se uma condição é verdadeira e, se for, executa o código que está "dentro" dele.

A sintaxe é assim:

```py
if condicao:
    # Código a ser executado SE a condicao for VERDADEIRA
    # Note a INDENTAÇÃO! É assim que Python sabe que este código pertence ao if
```

A condicao é uma expressão que resulta em `True` ou `False` (um valor booleano).

O `else` (Senão)
O `else` é opcional e vem depois de um `if`. O código dentro do `else` é executado apenas se a condição do `if` for falsa. Você pode ter quantos `elif` precisar entre um `if` e um `else`.

```py
if primeira_condicao:
    # Código executado SE a primeira_condicao for VERDADEIRA
elif segunda_condicao:
    # Código executado SE a primeira_condicao for FALSA E a segunda_condicao for VERDADEIRA
elif terceira_condicao:
    # Código executado SE as primeiras duas condicoes forem FALSAS E a terceira for VERDADEIRA
else:
    # Código executado SE NENHUMA das condicoes acima for VERDADEIRA
```

### Criando Condições: Operadores de Comparação e Lógicos
Para criar as condicaos que o if, elif e else verificam, usamos:

Operadores de Comparação: Comparam dois valores e retornam `True` ou `False`.

`==`: Igual a
`!=`: Diferente de
`>`: Maior que
`<`: Menor que
`>=`: Maior ou igual a
`<=`: Menor ou igual a

Exemplos: `idade > 18`, `nome == "Python"`, `saldo >= 1000`

Operadores Lógicos: Combinam condições booleanas.

`and`: Verdadeiro APENAS se AMBAS as condições forem verdadeiras.
`or`: Verdadeiro se PELO MENOS UMA das condições for verdadeira.
`not`: Inverte o resultado da condição (verdadeiro vira falso, falso vira verdadeiro).
Exemplos: `idade > 18 and tem_carteira_motorista`, `tem_dinheiro or tem_cartao, not esta_chovendo`

### Conectando com a Lógica de Programação
A lógica das estruturas condicionais é o controle de fluxo. Elas permitem que o programa siga caminhos diferentes dependendo dos dados ou das circunstâncias. É assim que programas se tornam dinâmicos e podem responder de maneiras variadas a diferentes entradas ou situações. Sem condicionais, um programa sempre executaria as mesmas instruções na mesma ordem.

### Resumo:
- `if`: Executa código se a condição for verdadeira.
- `else`: Executa código se a condição do `if` (e e`lifs` anteriores) for falsa.
- `elif`: Verifica uma nova condição se as anteriores forem `falsas`.
- A indentação define quais linhas de código pertencem a cada bloco (if, elif, `else`).
- Condições são criadas com Operadores de Comparação (`==`, `!=`, `>`, `<`, `>=`, `<=`) e podem ser combinadas com Operadores Lógicos (`and`, `or`, `not`).

### Exercício Prático:
Vamos praticar as estruturas condicionais! Crie um script Python que:

1. Peça ao usuário para digitar um número inteiro.
2. Converta a entrada para um número inteiro.
3. Verifique se o número é:
    -Positivo (maior que zero)
    - Negativo (menor que zero)
    - Igual a zero
4. Imprima uma mensagem informando ao usuário se o número é positivo, negativo ou zero. Use `if`, `elif` e `else` para isso.

```py
# Dica:
# numero = int(input("..."))
# if numero > 0:
#    print(...)
# elif ...
```