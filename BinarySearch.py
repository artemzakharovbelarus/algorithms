def search(list, number):
    """
       Finds the number in source list with help of binary search
    :param list: numbers
    :param number: need be found in list
    :return: if number was found - index, otherwise - None
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last)
        guess = list[mid]

        if guess == number:
            return mid
        if guess > number:
            last = mid - 1
        else:
            first = mid + 1
    return None


numbers = [1, 3, 5, 7, 9, 100]
print(search(numbers, 9))
print(search(numbers, -1))
