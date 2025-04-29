### Aula 08 - Estruturas de Dados

**Por que precisamos de Estruturas de Dados?**
Até agora, trabalhamos com variáveis que guardam um único valor por vez (um número, um nome, um booleano). Mas e se quisermos guardar uma lista de compras, os nomes de todos os alunos de uma turma, ou as informações (nome, idade, cidade) de uma pessoa? Precisamos de contêineres que possam guardar múltiplos valores, e é isso que as estruturas de dados fazem.

Vamos focar em duas das estruturas de dados mais comuns e úteis em Python: **Listas e Dicionários**=.

1. Listas (``list``)
Uma lista é uma coleção ordenada de itens. Pense nela como uma fila ou uma sequência onde cada item tem uma posição. As listas são mutáveis, o que significa que você pode mudar, adicionar ou remover itens depois que a lista for criada.

- Criando uma Lista: Usamos colchetes ``[]`` com os itens dentro, separados por vírgulas.

```py
minha_lista = [10, 20, 30, 40]
nomes = ["Alice", "Bob", "Charlie"]
lista_misturada = [1, "Python", True, 3.14] # Listas podem conter tipos de dados diferentes
lista_vazia = []
```

- **Acessando Itens:** Você acessa itens em uma lista pela sua posição ou índice. Em Python, os índices começam em 0.

```py
frutas = ["maçã", "banana", "cereja"]
print(frutas[0]) # Saída: maçã (o primeiro item)
print(frutas[1]) # Saída: banana (o segundo item)
# print(frutas[3]) # Isso daria um erro, pois não existe índice 3
```

- Você também pode usar índices negativos para acessar itens a partir do final da lista (``-1`` é o último, ``-2`` o penúltimo, etc.).

```py
print(frutas[-1]) # Saída: cereja (o último item)
```

- **Modificando Itens:** Como listas são mutáveis, você pode mudar um item acessando seu índice e atribuindo um novo valor.
```py
numeros = [1, 2, 3, 4]
numeros[0] = 5 # O primeiro item agora é 5
print(numeros) # Saída: [5, 2, 3, 4]
```

- A**dicionando Itens:** O método mais comum é ``append()``, que adiciona um item ao final da lista.

```py
tarefas = ["Comprar pão", "Estudar Python"]
tarefas.append("Fazer exercício") # Adiciona ao final
print(tarefas) # Saída: ['Comprar pão', 'Estudar Python', 'Fazer exercício']
```

- **Removendo Itens:** Você pode usar`` remove()`` para remover a primeira ocorrência de um valor específico, ou ``pop()`` (opcionalmente com um índice) para remover um item por posição e retorná-lo.

```py
cores = ["vermelho", "azul", "verde", "azul"]
cores.remove("azul") # Remove o primeiro "azul"
print(cores) # Saída: ['vermelho', 'verde', 'azul']

ultimo_item = cores.pop() # Remove e retorna o último item
print(cores) # Saída: ['vermelho', 'verde']
print(ultimo_item) # Saída: azul

primeiro_item = cores.pop(0) # Remove e retorna o item no índice 0
print(cores) # Saída: ['verde']
print(primeiro_item) # Saída: vermelho
```

- T**amanho da Lista:** Use a função ``len()`` para saber quantos itens a lista tem.

### 2. Dicionários (dict)
Um dicionário é uma coleção não ordenada (em versões antigas do Python, a partir da 3.7+ eles mantêm a ordem de inserção) de itens armazenados como pares de chave-valor. Pense nele como um caderno de endereços onde você procura uma pessoa pelo nome (a chave) para encontrar seu telefone (o valor). As chaves devem ser únicas e imutáveis (como strings ou números), e os valores podem ser de qualquer tipo. Dicionários também são mutáveis.

- **Criando um Dicionário:** Usamos chaves ``{}`` com pares ``chave: valor``, separados por vírgulas.

```py
pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
produto = {"id": "A123", "nome": "Teclado", "preco": 150.00}
dicionario_vazio = {}
```

- **Acessando Valores:** Você acessa um valor usando sua chave entre colchetes ``[]``.
```py
pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"]) # Saída: Ana
print(pessoa["idade"]) # Saída: 25
# print(pessoa["endereco"]) # Isso daria um erro, pois a chave 'endereco' não existe
```

Uma forma mais segura de acessar um valor e evitar erros caso a chave não exista é usar o método ``get()``. Ele retorna ``None`` (ou um valor padrão que você especifique) se a chave não for encontrada, em vez de dar um erro.

```py
print(pessoa.get("nome"))     # Saída: Ana
print(pessoa.get("endereco")) # Saída: None
print(pessoa.get("endereco", "Chave não encontrada")) # Saída: Chave não encontrada
```

- **Adicionando ou Modificando Itens:** Você adiciona um novo par chave-valor ou modifica um valor existente atribuindo um valor a uma chave.

```py
pessoa = {"nome": "Ana", "idade": 25}
pessoa["cidade"] = "Rio de Janeiro" # Adiciona a chave 'cidade'
print(pessoa) # Saída: {'nome': 'Ana', 'idade': 25, 'cidade': 'Rio de Janeiro'}

pessoa["idade"] = 26 # Modifica o valor da chave 'idade'
print(pessoa) # Saída: {'nome': 'Ana', 'idade': 26, 'cidade': 'Rio de Janeiro'}
```

- **Removendo Itens:** Use ``pop()`` com a chave para remover um par chave-valor e obter o valor, ou ``del`` com a chave.

```py
produto = {"id": "A123", "nome": "Teclado", "preco": 150.00}
preco_removido = produto.pop("preco") # Remove a chave 'preco' e retorna seu valor
print(produto) # Saída: {'id': 'A123', 'nome': 'Teclado'}
print(preco_removido) # Saída: 150.0

del produto["id"] # Remove a chave 'id'
print(produto) # Saída: {'nome': 'Teclado'}
```

- **Tamanho do Dicionário:** Use ``len()`` para saber quantos pares chave-valor o dicionário tem.

```py
meu_dict = {"a": 1, "b": 2}
print(len(meu_dict)) # Saída: 2
```

### Conectando com a Lógica de Programação
Estruturas de dados são sobre como organizar e gerenciar informações. Listas são ideais quando a ordem dos itens é importante ou quando você precisa acessar itens por posição. Dicionários são perfeitos quando você precisa associar informações (valor) a identificadores únicos (chaves) e acessar essas informações rapidamente usando a chave. A escolha da estrutura de dados correta simplifica muito a lógica do seu programa para manipular coleções de dados.

Resumo:
Listas ``[]``: Coleções ordenadas, mutáveis, acessadas por índice (começa em 0). Métodos comuns: ``append()``, ``remove()``, ``pop()``, ``len()``.
Dicionários ``{}``: Coleções de pares chave-valor, mutáveis, acessados por chave. Chaves são únicas. Métodos comuns: ``pop(chave)``, ``get(chave)``, ``len()``.
``len()``: Retorna o número de itens em ambas as estruturas.

### Exercício Prático:
Vamos praticar com Listas e Dicionários! Crie um script Python que:

1. Crie uma lista chamada frutas com pelo menos 4 nomes de frutas.
2. Imprima a lista completa.
3. Imprima o primeiro e o último item da lista frutas.
4. Adicione uma nova fruta ao final da lista frutas.
5. Crie um dicionário chamado produto com as seguintes chaves e valores:
    - ``"nome"``: o nome de um produto (texto)
    - ``"preco"``: o preço do produto (número)
    - ``"quantidade_em_estoque"``: a quantidade em estoque (número inteiro)
    - Imprima o dicionário completo.
    - Imprima o preço do produto usando a chave correta no dicionário.
    - Atualize a quantidade em estoque no dicionário (simulando uma venda, por exemplo, subtraindo um valor).
    - Imprima a quantidade em estoque atualizada.
```py
# Exemplo de como criar e imprimir:
# minha_lista = [...]
# print(minha_lista)
# meu_dicionario = { chave: valor, ... }
# print(meu_dicionario)
```