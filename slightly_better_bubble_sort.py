def slightly_better_bubble_sort(array):
    did_switch = True
    j = 0   #after each iteration the last element is already in its final position so it doesnt need to be checked again
    while did_switch:
        did_switch = False
        for i in range(len(array)-1-j):
            if array[i] > array[i+1]:
                did_switch = True
                array[i], array[i+1] = array[i+1], array[i]
    j += 1
    return array
