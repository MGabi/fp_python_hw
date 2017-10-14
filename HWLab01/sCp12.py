def checkNumbers(a, b):
    """
    Checks if two numbers have the same digits in their construction
    :param a: first number
    :param b: second number
    :return: True if they have the same numbers, False if not
    """

    if a < 0 or b < 0:
        return "The number(s) is(are) not natural"

    numbersA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numbersB = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while a != 0:
        numbersA[a%10] = 1
        a //= 10

    while b != 0:
        numbersB[b%10] = 1
        b //= 10

    for i in range(0, 10):
        if numbersA[i] != numbersB[i]:
            return False

    return True


def main():
    print("Enter two numbers to check if they\nhave the same numbers in their writtings in base 10: \n")
    a = int(input("a = "))
    b = int(input("b = "))
    print(checkNumbers(a, b))


main()