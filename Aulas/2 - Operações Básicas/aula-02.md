### Aula 02 - Operações Básicas

### O que são Operações Básicas?
Em programação, "operações" são ações que realizamos sobre dados ou variáveis para produzir novos valores ou modificar os existentes. As operações mais comuns são as matemáticas, mas existem outras.

Vamos focar nas mais fundamentais:

Operações Aritméticas: São as operações matemáticas que usamos para fazer cálculos com números.
- `+` (Adição): Soma dois valores.
- `-` (Subtração): Subtrai o segundo valor do primeiro.
- `*` (Multiplicação): Multiplica dois valores.
- `/` (Divisão): Divide o primeiro valor pelo segundo.1 *Nota: A divisão sempre retorna um número float, mesmo que o resultado seja um número inteiro.*
- `//` (Divisão Inteira): Divide e retorna apenas a parte inteira do resultado.
- `%` (Módulo/Resto da Divisão): Retorna o resto de uma divisão. Útil para verificar se um número é par ou ímpar, por exemplo.
- `**` (Exponenciação): Eleva o primeiro valor à potência do segundo.

```py
a = 10
b = 5

soma = a + b       # soma será 15
subtracao = a - b  # subtracao será 5
multiplicacao = a * b # multiplicacao será 50
divisao = a / b    # divisao será 2.0 (float!)
divisao_inteira = a // b # divisao_inteira será 2
resto = a % 3      # resto será 1 (10 dividido por 3 dá 3 com resto 1)
potencia = a ** 2  # potencia será 100 (10 elevado a 2)
```

### 2. Operações de Atribuição: 
Já vimos a mais básica, que é o =. Ela simplesmente atribui um valor a uma variável. No entanto, é muito comum querer realizar uma operação em uma variável e, em seguida, armazenar o resultado de volta na mesma variável. Para isso, existem as operações de atribuição composta:

- `+=`: Soma o valor e atribui o resultado à variável. (Ex: `x += 5` é o mesmo que `x = x + 5`)
- `-=`: Subtrai o valor e atribui o resultado à variável.
- `*=`: Multiplica o valor e atribui o resultado à variável.
- `/=`: Divide o valor e atribui o resultado à variável.
- `//=`: Realiza a divisão inteira e atribui o resultado à variável.
- `%=`: Calcula o resto da divisão e atribui o resultado à variável.
- `**=`: Realiza a exponenciação e atribui o resultado à variável.

```py
contador = 0
contador += 1 # contador agora é 1

saldo = 1000
saldo -= 200  # saldo agora é 800

preco = 10
preco *= 1.1 # preco agora é 11.0
```

### Conectando com a Lógica de Programação

A lógica por trás das operações é o processamento. Uma vez que temos dados armazenados em variáveis, precisamos processá-los para obter novos resultados. Seja somando valores de um carrinho de compras, calculando uma média, ou determinando um resto para verificar alguma condição, as operações são os "verbos" da programação que nos permitem manipular os dados.

Resumo:
**Operações Aritméticas:** Realizam cálculos matemáticos (+, -, *, /, //, %, **).
**Operações de Atribuição:** Atribuem valores a variáveis, incluindo as formas compostas (+=, -=, etc.) para modificar o valor existente na própria variável.

### Exercício Prático:
Vamos praticar as operações! Crie um script Python que:

Crie duas variáveis, `num1` com o valor `25` e `num2` com o valor `7`.
Crie variáveis para armazenar os resultados das seguintes operações entre `num1` e `num2`:
- Soma
- Subtração
- Multiplicação
- Divisão (usando `/`)
- Divisão Inteira (usando `//`)
- Resto da Divisão (usando `%`)
- Crie uma variável `saldo_conta` com o valor `500`.
- Use uma operação de atribuição composta para adicionar `150` ao `saldo_conta`.
- Use outra operação de atribuição composta para subtrair `75` do `saldo_conta`.
- Imprima o valor de todas as variáveis criadas no passo 2 e o valor final da variável `saldo_conta`.

```py
# Exemplo:
# soma = num1 + num2
# print("Soma:", soma)
```
