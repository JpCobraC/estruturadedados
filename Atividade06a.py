# Tente deduzir e implementar sem consultar pelo menos a parte de chamadas recursivas do Merge Sort. _mergesort.

def mergesort(arr):
    """
    Função principal do Merge Sort.
    Apenas chama a função recursiva.
    """
    _mergesort(arr, 0, len(arr) - 1)


def _mergesort(arr, left, right):
    """
    Função recursiva do Merge Sort.
    Divide o array em partes menores.
    """
    if left < right:  # Caso base: subarray possui pelo menos 2 elementos.
        
        # Calcula o meio do array.
        middle = (left + right) // 2

        # Ordena recursivamente a metade esquerda.
        _mergesort(arr, left, middle)

        # Ordena recursivamente a metade direita.
        _mergesort(arr, middle + 1, right)

        # Junta as duas metades ordenadas.
        merge(arr, left, middle, right)


def merge(arr, left, middle, right):
    """
    Função responsável por intercalar (merge)
    duas partes ordenadas do array.
    """

    # Cria cópias das duas metades.
    left_part = arr[left:middle + 1]
    right_part = arr[middle + 1:right + 1]

    i = 0  # Ponteiro da metade esquerda.
    j = 0  # Ponteiro da metade direita.
    k = left  # Ponteiro do array principal.

    # Compara elementos das duas metades.
    while i < len(left_part) and j < len(right_part):

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        k += 1

    # Copia elementos restantes da esquerda.
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Copia elementos restantes da direita.
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


nums = [9, 4, 3, 8, 2, 7]

mergesort(nums)

print(nums)