# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()

    mapeamento = {')': '(', '}': '{', ']': '['}
    
    for caractere in expression:
        # Se for um símbolo de abertura, empilha
        if caractere in "({[":
            pilha.push(caractere)
        
        # Se for um símbolo de fechamento
        elif caractere in ")}]":
            # Se a pilha estiver vazia ou o topo não corresponder ao par, está desbalanceado
            if pilha.is_empty() or pilha.pop() != mapeamento[caractere]:
                return False
                
    # Ao final, a expressão só é válida se a pilha estiver totalmente vazia
    return pilha.is_empty()

                
    # Ao final, a expressão só é válida se a pilha estiver totalmente vazia
    return pilha.is_empty()

# Alguns Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False

print(" ")
print(is_balanced(""))                         # Expressão vazia → True
print(is_balanced("()"))                       # Um par de parênteses simples → True
print(is_balanced("({[]})"))                   # Vários pares aninhados → True
print(is_balanced("{[()()]()}"))               # Aninhamento complexo correto → True
print(is_balanced("if (a[0] > b) { return c; }")) # Parênteses misturados com código → True

print(" ")
print(is_balanced("("))                        # Apenas abertura → False
print(is_balanced("]"))                        # Apenas fechamento → False
print(is_balanced("({[)]}"))                   # Ordem incorreta → False
print(is_balanced("{[(()]}"))                  # Um fechamento errado no meio → False
print(is_balanced("((()))]"))                  # Um fechamento extra → False