#
# [2, 5, 7, 7]
# find the second largest; ex: 5.
#

def find_second_largest(array):
    # Try 1
    # array.sort()
    #
    # length = len(array)
    #
    # last_element = array[-1]
    #
    # for index in range(length-1, -1, -1):
    #     if array[index] < last_element:
    #         last_element = array[index]
    #         break

    # Try 2
    largest_element = max(array)

    current_largest = -1

    for _, element in enumerate(array):
        if current_largest < element < largest_element:
            current_largest = element

    return current_largest


if __name__ == "__main__":
    print(find_second_largest([29,17,16,24,33]))
    print(find_second_largest([29,33]))
