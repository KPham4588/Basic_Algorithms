# there are other data structures that can utilize binary search,
# but I use an array(list in python) for easier implementation
# so that one can focus on the concept


def binary_search(input_array, input_size, target):

    # make sure input is sorted
    if input_array != sorted(input_array):
        input_array = sorted(input_array)

    left = 0
    right = input_size-1

    # exit condition is right index < left index; signifies out-of-bound/nonsensical indexing
    # and that number doesn't exist in array
    while not (left > right):

        # find center index
        center = int((left + right) / 2)

        # if the center is higher than target, take the lower half of the list
        if input_array[center] > target:
            right = center - 1

        # if the center is lower than target, take the higher half of the list
        elif input_array[center] < target:
            left = center + 1

        # else, center = target and we return the index
        else:
            return center

    # return -1 to signify the number was not found
    return -1


result = binary_search([3, 4, 5, 2, 1], 5, 5)
print("index of target is: ", result)
