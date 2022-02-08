def bubble_sort(lst):
    """
    Função do bubble sort.
    :param lst: lst é uma lista de inteiros
    """

    # Percorrer a lista
    for i in range(len(lst)):
        for j in range(0, len(lst) -i -1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j] 



# Testando a função
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    bubble_sort(lst)

    print("Sorted list is: ", lst)