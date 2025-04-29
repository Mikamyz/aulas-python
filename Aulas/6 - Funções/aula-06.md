### Aula 06 - Funções
Imagine que você tem uma tarefa específica que precisa realizar várias vezes no seu programa, ou talvez uma tarefa complexa que você quer dividir em passos menores e mais gerenciáveis. É aí que entram as funções.

Uma função é um bloco de código organizado e reutilizável que executa uma tarefa específica. Pense nela como uma "mini-programa" dentro do seu programa principal, ou como uma receita: você define a receita uma vez, e pode "chamar" ou "usar" essa receita sempre que precisar do resultado que ela produz, sem ter que escrever todos os passos novamente.

### Por que usar Funções?
Usar funções traz muitas vantagens:

- **Reutilização de Código:** Escreva o código uma vez e chame a função sempre que precisar.
- **Organização:** Ajuda a dividir programas grandes em partes menores e mais fáceis de entender.
- **Legibilidade:** Torna o código mais fácil de ler e entender, pois cada função geralmente tem um nome que descreve sua finalidade.
- **Manutenção:** Se houver um erro em uma tarefa, você só precisa corrigir o código naquele bloco da função, em vez de procurar e corrigir o mesmo erro em vários lugares.

### Como Definir uma Função em Python?
Em Python, definimos uma função usando a palavra-chave ``def``, seguida pelo nome da função, parênteses ``()`` (que podem conter parâmetros) e dois pontos ``:``. O corpo da função é o código que vem abaixo, indentado (assim como nos blocos ``if`` e ``while``).

A sintaxe básica é:

```py
def nome_da_funcao():
    # Código que a função executa
    # Este código deve ser INDENTADO
    print("Esta função faz alguma coisa!")

# O código fora da função não é executado quando a função é definida
# Ele só será executado quando a função for CHAMADA
```

### Parâmetros e Argumentos
Funções podem aceitar parâmetros, que são valores que você passa para a função usar dentro dela. Os parâmetros são definidos entre os parênteses na definição da função. Quando você chama a função, os valores que você passa são chamados de argumentos.

```py
def saudar(nome): # 'nome' é um parâmetro
    print(f"Olá, {nome}!")

# Chamando a função e passando um argumento:
saudar("Alice") # "Alice" é o argumento
saudar("Bob")   # "Bob" é outro argumento
```

Uma função pode ter zero, um ou vários parâmetros, separados por vírgula.

**Valores de Retorno** (``return``)
Uma função pode, opcionalmente, retornar um valor para o lugar onde ela foi chamada. Usamos a palavra-chave ``return`` para isso. Se uma função não tem uma instrução ``return`` explícita, ela retorna o valor especial None por padrão.

```py
def somar(a, b):
    resultado = a + b
    return resultado # A função retorna o valor da variável resultado

# Chamando a função e armazenando o valor retornado:
soma_total = somar(5, 3) # soma_total receberá o valor 8
print("A soma é:", soma_total)

def dizer_ola():
    print("Olá!")
    # Esta função não tem return, então retorna None
```

Quando uma função encontra uma instrução ``return``, ela para imediatamente de executar e envia o valor de volta.

Como Chamar (Executar) uma Função?
Para usar o código dentro de uma função, você precisa chamá-la (ou invocá-la). Você faz isso escrevendo o nome da função seguido por parênteses ``()``, colocando os argumentos necessários dentro deles.

```py
# Definindo a função
def mostrar_mensagem():
    print("Estou dentro da função!")

# Chamando a função para executá-la
mostrar_mensagem()
```

#### Conectando com a Lógica de Programação
O uso de funções está ligado à lógica de **modularidade** e **abstração**. Modularidade significa dividir um grande problema em módulos menores e independentes (as funções). Abstração significa focar no "o que" a função faz (sua finalidade) sem se preocupar demais com o "como" ela faz (os detalhes internos do código). Isso torna o pensamento sobre o programa mais organizado e facilita a resolução de problemas complexos.

### Resumo:
- ``def nome_da_funcao(parametros):``: Define uma função.
- Corpo da função é o código indentado abaixo da definição.
- Parâmetros: Variáveis na definição que recebem valores (argumentos) quando a função é chamada.
- ``return`` valor: Envia um resultado de volta para onde a função foi chamada (opcional).
- Chamar a função: ``nome_da_funcao(argumentos)``.
- Funções ajudam a organizar, reutilizar e entender o código.

### Exercício Prático:
Vamos praticar a criação e o uso de funções! Crie um script Python que:

1. Defina uma função chamada ``calcular_area_retangulo``.
2. Esta função deve aceitar dois parâmetros: ``largura`` e ``altura``.
3.  Dentro da função, calcule a área multiplicando a largura pela altura.
4. A função deve retornar o valor da área calculada.
5. Depois de definir a função, chame-a com valores de exemplo para largura e altura (por exemplo, 5 e 10).
6. Armazene o valor retornado pela função em uma variável.
8. Imprima o valor da área calculada (a variável que você armazenou).

```py
# Exemplo da estrutura:
# def nome_da_funcao(param1, param2):
#    # faz algo
#    return resultado
#
# valor_obtido = nome_da_funcao(arg1, arg2)
# print(valor_obtido)
```