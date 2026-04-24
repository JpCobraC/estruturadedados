class Node:
    def __init__(self, data):
        self.data = data      # Valor do nó
        self.next = None      # Ponteiro para o próximo nó


class SingleLinkedList:
    def __init__(self):
        self.head = None      # Ponteiro para o início da lista
        self.tail = None      # Ponteiro para o final da lista (para facilitar append)
        self.size = 0         # Tamanho da lista

    def append(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  
            self.tail = new_node       
        self.size += 1

    def insert(self, index, data):
        """
        Insere um novo nó na posição desejada (base 0) da lista.

        Objetivo:
            - Criar um novo nó contendo o valor fornecido.
            - Inserir esse nó na posição indicada pelo índice.
            - Atualizar os ponteiros necessários e o contador `size`.
            - A explicação dos detalhes foi dada na aula passada.
            - Não esquecer de verificar se a lista está vazia e tratar de acordo.

        Exemplo esperado:
            lista = SingleLinkedList()
            lista.append(5)
            lista.append(23)
            lista.append(7)
            lista.insert(1, 11)   # Insere o 11 na posição 1
            print(lista)          # "5 -> 11 -> 23 -> 7"
        """
        new_node = Node(data)

        if index <= 0:               
            new_node.next = self.head
            self.head = new_node
            if self.size == 0: 
                self.tail = new_node
            self.size += 1
            return

        if index >= self.size:         
            self.append(data)
            return

        trav = self.head
        for _ in range(index - 1):
            trav = trav.next

        new_node.next = trav.next
        trav.next = new_node
        self.size += 1

    def __str__(self):
        """
        Retorna uma representação string da lista (ex: 5 -> 23 -> 7 -> 13).
        """
        elements = []
        trav = self.head  
        while trav:
            elements.append(str(trav.data))
            trav = trav.next
        return " -> ".join(elements)


# Criando a lista inicial: 5 -> 23 -> 7 -> 13
linked_list = SingleLinkedList()
linked_list.append(5)
linked_list.append(23)
linked_list.append(7)
linked_list.append(13)

print("Lista original:")
print(linked_list)

# Inserindo 11 na terceira posição (índice 2, entre 23 e 7)
linked_list.insert(2, 11)

print("\nLista após inserir 11 na terceira posição:")
print(linked_list)