def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))

def merge(array1, array2):
    merged_array = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        elif array2[j] < array1[i]:
            merged_array.append(array2[j])
            j += 1

    # either array1 or array2 is fully traversed now -> append remaining elements in array to merged_array
    while i < len(array1):
        merged_array.append(array1[i])
        i += 1

    while j < len(array2):
        merged_array.append(array2[j])
        j += 1

    return merged_array
