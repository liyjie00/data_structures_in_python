def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]



a = [21,334,5,232,64,67,84,2,78,854]
print(a)
print('-'*30)
bubbleSort(a)
print(a)