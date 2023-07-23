import math


def bucket_sort(array, number_of_buckets):
    # find the largest value in array to later transform array to range from 0 to 1 (exclusive)
    max_value = 0
    for element in array:
        if element > max_value:
            max_value = element

    bucket_list = []
    for i in range(number_of_buckets):
        bucket_list.append([])

    for element in array:
        bucket_list[math.floor((element/(max_value+1))*number_of_buckets)].append(element)

    sorted_array = []
    for bucket in bucket_list:
        bucket.sort()
        sorted_array += bucket

    return sorted_array
