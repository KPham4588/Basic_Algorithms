# an implementation of merge sort to help understand the concepts
# the implementation is recursive


def merge_sort(input_array):

    # this part divides the input up into smaller chunks,
    # terminating at the base case

    # if the list's size is 1, it is trivially sorted
    # this is the base case
    if len(input_array) == 1:
        return input_array

    # recursive case is dividing up the list
    middle = len(input_array)//2
    left = input_array[:middle]
    right = input_array[middle:]

    print("current left array: {}".format(left))
    print("current right array: {}".format(right))
    print()

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# this part combines the arrays in sorted order
def merge(first_array, second_array):

    new_array = []

    # since the earlier elements are the smallest, we can repeatedly compare the first elements
    # and pop them out of the list as we merge those into a bigger list
    while first_array and second_array:
        if first_array[0] > second_array[0]:
            new_array.append(second_array.pop(0))

        elif first_array[0] < second_array[0]:
            new_array.append(first_array.pop(0))

    while first_array:
        new_array.append(first_array.pop(0))
    while second_array:
        new_array.append(second_array.pop(0))
    print(new_array)
    return new_array


iteration = 0
input_list = [38, 27, 43, 3, 9, 82, 10]
output_list = merge_sort(input_list)

print("output is: ", output_list)
