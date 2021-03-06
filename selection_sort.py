def selection_sort(lst):
    """
    Função do selection sort
    :param lst: Lista de inteiros
    """

    for i in range(len(lst)):
        # Encontrar o menor elemento da lista
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index= j
        
        # Trocar o menor valor encontrado com o maior elemento
        lst[i],lst[min_index] = lst[min_index], lst[i]
    

# Codigo para testar a funcao
if __name__ == '__main__':
    lst = [3, 2, 1,  5, 4]
    selection_sort(lst)

    print("Lista ordenada: ", lst)