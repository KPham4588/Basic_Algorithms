# a simple quicksort implementation
# here the pivot will be the middle value of the list


# split the input and recursively calls itself on smaller partitions
def quick_sort(input_array, low, high):

    # check to see if the indices are sound before recursively calling itself
    if low < high:

        # "part" takes the value of an index to divide up the input into two smaller parts,
        # both of which goes through quicksort again
        part = partition(input_array, low, high)
        quick_sort(input_array, low, part)
        quick_sort(input_array, part+1, high)


# split the input list and return the index to use for recursion
def partition(input_array, low, high):

    # the pivot will be the first element in the input for simplicity
    pivot = input_array[low]

    i = low
    j = high

    while True:

        # while the lower indices have lower values than the pivot, move up the array
        # and vice versa
        # the reason is because those numbers are in their correct
        # segment of the list; we want to move bigger numbers behind the pivot and lower numbers before
        while input_array[i] < pivot:
            print('comparing {} and pivot {}'.format(input_array[i], pivot))
            i += 1
            print('from {} to {}'.format(i-1, i))
        while input_array[j] > pivot:
            print('comparing {} and pivot {}'.format(input_array[j], pivot))
            j -= 1
            print(print('from {} to {}'.format(j+1, j)))

        # if i >+ j at any point, that means we have no more to swap and we return the
        # index to cut the original list into a smaller one
        if i >= j:
            print('returning {}'.format(j))
            return j

        print('from {}'.format(input_array), end=' ')
        # swap the elements to correct their positions
        input_array[i], input_array[j] = input_array[j], input_array[i]
        print('to {}'.format(input_array))


test_list = [9, 8, 7, 6, 5, 10, 3]
quick_sort(test_list, 0, len(test_list) - 1)
print(test_list)
