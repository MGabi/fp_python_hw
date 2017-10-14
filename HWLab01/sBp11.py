def checkPalindrome(x):
    """
    Checks if a number is palindrome
    :param x: the number which will be checked
    :return: True if it's palindrome, False if not
    """
    if x < 0:
        return "That's not a natural number."

    numbers = []
    while x != 0:
        numbers.append(x % 10)
        x //= 10

    for i in range(0, len(numbers) // 2):
        if numbers[i] != numbers[len(numbers)-1]:
            return False

    return True


def main():
    x = int(input("Enter a number to check if it's palindrome: "))
    print(checkPalindrome(x))

main()