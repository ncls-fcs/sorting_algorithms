from numpy import random

import bogosort
import bubble_sort
import bucket_sort
import insertion_sort
import merge_sort
import quick_sort
import slightly_better_bubble_sort

unsorted_array = random.randint(1000, size=(100))

if __name__ == '__main__':
    #print(bubble_sort.bubble_sort(unsorted_array))
    #print(slightly_better_bubble_sort.slightly_better_bubble_sort(unsorted_array))
    #print(merge_sort.merge_sort(unsorted_array))
    #print(bogosort.bogosort(unsorted_array))       #DO NOT USE
    #print(quick_sort.quick_sort(unsorted_array, 0, 99))
    #print(bucket_sort.bucket_sort(unsorted_array, 10))
    print(insertion_sort.insertion_sort(unsorted_array))
