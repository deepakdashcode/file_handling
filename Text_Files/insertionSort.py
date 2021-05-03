def insertionSort(ls):
    for i in range(1, len(ls)):
        j = i - 1
        key = ls[i]
        while (j >= 0 and ls[j] > key):
            ls[j + 1] = ls[j]
            j = j - 1
        ls[j + 1] = key

    print(ls)


ls = [1, 32, 43, 4, -23, 4, 2, 2, 1, 4, 5, 7, 3, 2, -56, 243, -234, 24]
insertionSort(ls)