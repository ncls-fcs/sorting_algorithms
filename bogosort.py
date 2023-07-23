import random


def bogosort(array):
    while(True):
        for i in range(len(array)-1):
            if array[i] <= array[i+1]:
                if i >= len(array) - 2:
                    return array
                continue
            else:
                random.shuffle(array)
                break
