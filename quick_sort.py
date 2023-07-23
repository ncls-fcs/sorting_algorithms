def quick_sort(array, start, end):
    if end > start:
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index-1)
        quick_sort(array, pivot_index+1, end)
    return array


def partition(array, start, end):
    pivot = array[end]
    i = start-1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[end], array[i+1] = array[i+1], array[end]
    return i+1
