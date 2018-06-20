def insertionSort(list):
    for index in range(len(list)):
        if index == 0:
            continue
        tempIndex = index
        while tempIndex > 0:
            if list[tempIndex] >= list[tempIndex - 1]:
                break
            else:
                list[tempIndex - 1], list[tempIndex] = list[tempIndex], list[tempIndex - 1]
            tempIndex -= 1
        index += 1


a = [21,334,5,232,64,67,84,2,78,854]
print(a)
print('-'*30)
insertionSort(a)
print(a)