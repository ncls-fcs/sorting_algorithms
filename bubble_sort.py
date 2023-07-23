def bubble_sort(array):
    did_switch = True
    while did_switch:
        did_switch = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                did_switch = True
                array[i], array[i+1] = array[i+1], array[i]
    return array
