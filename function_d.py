def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

=======
    max_value = max(numbers)
    return max_value


>>>>>>> 7791cd9eab1031672918fe23c8221aadd9390f9d


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
