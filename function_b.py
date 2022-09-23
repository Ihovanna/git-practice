# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
""" I don't think this explanation is necessary
    """
    num = int(input('Please enter a number => '))
    sum = 0

    while num != 0:
        sum += num
        if sum >= 1000:
            break

        num = int(input('Please enter a number => '))

    return sum


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
