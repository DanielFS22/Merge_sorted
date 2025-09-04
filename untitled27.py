## 📌 Código comentado
```python
# Implementação do algoritmo Merge Sort em Python

# Função principal do Merge Sort
def merge_sort(lista):
    n = len(lista)

    # Caso base: listas de tamanho 0 ou 1 já estão ordenadas
    if n <= 1:
        return lista

    # Encontrar o índice do meio
    meio = n // 2

    # Dividir a lista em duas partes
    l1 = lista[0:meio]   # do início até o meio
    l2 = lista[meio:n]   # do meio até o final

    # Chamar recursivamente para ordenar as duas metades
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

    # Mesclar as duas metades ordenadas
    return mesclar(l1, l2)


# Função para mesclar duas listas ordenadas em uma única lista ordenada
def mesclar(a, b):
    c = []

    # Enquanto as duas listas tiverem elementos, compara e pega o menor
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b.pop(0))  # remove e adiciona o menor de b
        else:
            c.append(a.pop(0))  # remove e adiciona o menor de a

    # Se sobrarem elementos em a, adiciona todos em c
    while len(a) > 0:
        c.append(a.pop(0))

    # Se sobrarem elementos em b, adiciona todos em c
    while len(b) > 0:
        c.append(b.pop(0))

    return c


# Exemplo de lista desordenada
lista_para_ordenar = [37, 5, 92, 18, 63, 74, 29, 8, 41, 56]

# Chamada do algoritmo
print(merge_sort(lista_para_ordenar))
