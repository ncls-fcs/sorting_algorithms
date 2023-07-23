def insertion_sort(array):
    for i in range(len(array)-1):
        j = i + 1
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array
