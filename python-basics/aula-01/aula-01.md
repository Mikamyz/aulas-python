### Aula 1: Variáveis e Tipos de Dados em Python
No guia básico, vimos que variáveis são nomes que damos a locais na memória para armazenar valores e que Python infere o tipo. Agora, vamos explorar um pouco mais.

### 1. Variáveis: Mais Detalhes
O que realmente são: Em Python, uma variável é como uma etiqueta ou um nome que você anexa a um objeto (o valor em si) na memória do computador. Quando você atribui um novo valor a uma variável, você está essencialmente movendo essa etiqueta para apontar para um novo objeto.

**Regras para Nomes de Variáveis:**
- Devem começar com uma letra (`a-z`, `A-Z`) ou um underscore (`_`).
- Podem conter letras, números (`0-9`) e underscores.
- São case-sensitive (`idade` é diferente de `Idade`).
- Não podem ser palavras reservadas de Python (como `if`, `for`, `while`, `print`, etc.).
- Exemplos válidos: `nome`, `idade`, `saldo_conta`, `_temp`, `numero1`.
- Exemplos inválidos: `1numero` (começa com número), `meu-nome` (contém hífen), `-` 
- `print` (palavra reservada).

- Boas Práticas de `Nomenclatura`:
    - Use nomes descritivos (`nome_completo` em vez de `nc`).
    - Use letras minúsculas e underscores para separar palavras (convenção `snake_case`).
- Atribuição e Reatribuição:

```python
idade = 30 # Atribui o valor 30 à variável idade
print(idade) # Saída: 30

idade = 31 # Reatribui a variável idade para apontar para o valor 31
print(idade) # Saída: 31

nome = "Maria"
nome = nome + " Silva" # Reatribui concatenando strings
print(nome) # Saída: Maria Silva
```

Você também pode atribuir múltiplos valores a múltiplas variáveis na mesma linha:

```python
x, y, z = 10, 20, 30
print(x, y, z) # Saída: 10 20 30
```

- Verificando o Tipo (`type()`):
Você pode verificar o tipo de dado que uma variável armazena usando a função `type()`.

```python
preco = 19.99
print(type(preco)) # Saída: <class 'float'>

cidade = "São Paulo"
print(type(cidade)) # Saída: <class 'str'>
```

### 2. Tipos de Dados: Aprofundamento nos Básicos

Vamos olhar com um pouco mais de detalhe para os tipos escalares (que representam um único valor). Os tipos de coleção (listas, etc.) serão tópicos futuros de aprofundamento.
- `int` (Inteiros):
    - Representam números inteiros positivos ou negativos sem limite de tamanho (limitado apenas pela memória disponível).

```python
numero_grande = 12345678901234567890
print(numero_grande)
```

- `float` (Ponto Flutuante):
    - Representam números reais (com parte decimal).
    - Podem ser representados em notação científica (ex: 1.2e-4 é 1.2 * 10^-4).
    - Importante: Operações com floats podem ter pequenas imprecisões devido à forma como computadores representam números de ponto flutuante. Para cálculos financeiros precisos, use o módulo decimal.

```python
pi = 3.14159
gravidade = 9.81
notacao = 6.022e23 # Número de Avogadro
print(pi, gravidade, notacao)
```

`str` (Strings):
- Sequências de caracteres. Podem ser definidas com aspas simples (`'`) ou duplas (`"`).
- Strings são imutáveis: uma vez criadas, não podem ser modificadas no local. - Qualquer operação que pareça modificar uma string, na verdade, cria uma nova string.
- Indexação e Fatiamento (Slicing): Você pode acessar caracteres individuais ou partes da string. O índice começa em 0.

```python
palavra = "Python"
print(palavra[0])    # Saída: P (primeiro caractere)
print(palavra[5])    # Saída: n (último caractere)
print(palavra[-1])   # Saída: n (último caractere usando índice negativo)
print(palavra[2:5])  # Saída: tho (do índice 2 até o 5, exclusive)
print(palavra[:3])   # Saída: Pyt (do início até o índice 3, exclusive)
print(palavra[3:])   # Saída: hon (do índice 3 até o final)
print(palavra[:])    # Saída: Python (a string inteira)
```

- Métodos Comuns de String: Strings têm muitos métodos úteis (funções associadas a objetos string).

```python
texto = "  Olá, Mundo!  "
print(len(texto))         # Saída: 15 (com espaços)
print(texto.strip())      # Saída: "Olá, Mundo!" (remove espaços no início e fim)
print(texto.lower())      # Saída: "  olá, mundo!  "
print(texto.upper())      # Saída: "  OLÁ, MUNDO!  "
print(texto.replace("Mundo", "Python")) # Saída: "  Olá, Python!  "
print("Python" in texto)  # Saída: False (verifica se "Python" está na string)
```

`bool` (Booleanos):
- Representam os valores lógicos True ou False.
- Resultam frequentemente de operações de comparação.
- São fundamentais para estruturas de controle (condicionais e loops).

```python
chovendo = True
ensolarado = False
print(chovendo and ensolarado) # Saída: False
print(chovendo or ensolarado)  # Saída: True
```

- Conversão de Tipos (`Type Casting`):
Você pode converter valores de um tipo para outro usando funções com o nome do tipo.

```python
numero_str = "123"
numero_int = int(numero_str) # Converte string para inteiro
print(type(numero_int)) # Saída: <class 'int'>

numero_float = float(numero_int) # Converte inteiro para float
print(numero_float) # Saída: 123.0
print(type(numero_float)) # Saída: <class 'float'>

valor = 10
valor_str = str(valor) # Converte inteiro para string
print(valor_str + " é um texto agora.") # Saída: 10 é um texto agora.

# Cuidado com conversões inválidas:
# int("Olá")  # Geraria um erro!
```

### Exercício de Lógica: Cadastro Simples
Objetivo: Praticar o uso de variáveis, diferentes tipos de dados, entrada (`input`), saída (`print`) e conversão de tipos.

Problema: Crie um programa que solicite ao usuário as seguintes informações:

- Seu nome completo.
- Sua idade (em anos).
- Sua altura (em metros, usando ponto como separador decimal).
- Se é estudante (responda "Sim" ou "Não").
- Armazene cada informação em uma variável com um nome descritivo e o tipo de dado apropriado (lembre-se que` input()` retorna `string` e pode precisar de conversão).

Após coletar os dados, imprima na tela um resumo formatado com as informações coletadas, algo como:

```
--- Perfil do Usuário ---
Nome: [Nome Completo]
Idade: [Idade] anos
Altura: [Altura] m
Estudante: [Sim/Não]
------------------------
```

**Dicas:**

- Use a função `input()` para obter os dados do usuário.
- Use `int()`, `float()`, e talvez a função `bool()` ou uma verificação simples com if para converter os dados de entrada para os tipos corretos, quando necessário.
- Use a função `print()` para exibir o resumo. Você pode concatenar strings com `+` ou usar` f-strings` (strings formatadas, um recurso bem útil: `f"Texto {variavel}"`) para formatar a saída.