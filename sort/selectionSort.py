def selectionSort(list):
    length = len(list)
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]


a = [21,334,5,232,64,67,84,2,78,854]
print(a)
print('-'*30)
selectionSort(a)
print(a)