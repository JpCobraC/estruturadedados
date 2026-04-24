from stack import Stack

class QueueUsingStacks:
    """
    Fila (Queue) implementada usando duas pilhas (Stacks)
    para manter o comportamento FIFO (First In, First Out).
    """
    def __init__(self):
        self.pilha_principal = Stack()   # Pilha onde inserimos os elementos.
        self.pilha_aux = Stack()         # Pilha auxiliar que deve ser usada.

    def enqueue(self, data):
        """
        Adiciona um elemento ao final da fila.
        """
        self.pilha_principal.push(data)

    def dequeue(self):
        """
        Remove e retorna o elemento do início da fila.
        """
        # Transfere elementos para a pilha auxiliar se ela estiver vazia.
        if self.pilha_aux.is_empty():
            while not self.pilha_principal.is_empty():
                self.pilha_aux.push(self.pilha_principal.pop())

        if self.pilha_aux.is_empty():
            raise IndexError("Fila vazia")

        return self.pilha_aux.pop()

    def is_empty(self):
        """
        Verifica se a fila está vazia.
        """
        return self.pilha_principal.is_empty() and self.pilha_aux.is_empty()

    def __str__(self):
        # Copiar elementos mantendo a ordem correta da fila
        temp_principal = Stack()
        temp_aux = Stack()
        result = []

        # Esvaziar a pilha auxiliar para acessar os elementos em ordem
        while not self.pilha_aux.is_empty():
            val = self.pilha_aux.pop()
            result.append(val)
            temp_aux.push(val)

        # Esvaziar a pilha principal para empilhar em ordem reversa
        while not self.pilha_principal.is_empty():
            val = self.pilha_principal.pop()
            temp_principal.push(val)

        # Recuperar os elementos da pilha principal (revertendo a ordem)
        while not temp_principal.is_empty():
            val = temp_principal.pop()
            result.append(val)
            self.pilha_principal.push(val)

        # Restaurar a pilha auxiliar
        while not temp_aux.is_empty():
            self.pilha_aux.push(temp_aux.pop())

        if not result:
            return "Fila vazia"

        result[0] = f"{result[0]} (Início)"
        result[-1] = f"{result[-1]} (Fim)"
        return "\n↓\n".join(str(x) for x in result)


# Testando a fila
if __name__ == "__main__":
    fila = QueueUsingStacks()

    print("\nInserindo: 10, 20, 30")
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    print(fila)

    print("\nRemovendo dois elementos:")
    print(fila.dequeue())
    print(fila.dequeue())
    fila.enqueue(40)

    print("\nEstado atual da fila:")
    print(fila)

    print("\nA fila está vazia?", fila.is_empty())

    print("\nRemovendo mais um elemento:")
    print(fila.dequeue())

    print("\nA fila está vazia?", fila.is_empty())

    print(" ")
    print(fila)