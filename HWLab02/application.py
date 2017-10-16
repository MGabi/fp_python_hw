import os

def check010Range(numbers):
    """
    Checks if all elements are in [0, 10] range
    :param numbers: the list that needs to be verified
    :return: true if the condition from above is aquired, false if not
    """
    start = 0
    length = 0
    max = 0
    for i in range(0, len(numbers)):
        if numbers[i] >= 0 and numbers[i] <= 10:
            length += 1
        else:
            if length > max:
                max = length
                start = i - max
            length = 0

    if length > 0:
        if length > max:
            max = length
            start = len(numbers) - max

    print(numbers[start: start + max])

    if length > 0:
        return True
    return False


def checkElementsSum(numbers):
    """
    Checks if the sum of all elements is 10
    :param numbers: the list that needs to be verified
    :return: true if the condition from above is aquired, false if not
    """
    start = 0
    length = 0
    max = 0
    s = 0
    for i in range(0, len(numbers)):
        if s < 10 and numbers[i] <= 10:
            length += 1
        else:
            if s == 10:
                if length > max:
                    max = length
                    start = i - max
        length = 0

    if length > 0:
        if length > max:
            max = length
            start = len(numbers) - max

    print(numbers[start: start + max])

    if length > 0:
        return True
    return False


def checkDigits(nr1, nr2):
    """
    Verify if two numbers have at least 2 common digits
    :param param: first number
    :param param1: second number
    :return: true if they have at least 2 common digist
    """

    n1 = [0] * 10
    n2 = [0] * 10

    while nr1 > 0:
        n1[nr1 % 10] = 1
        nr1 //= 10

    while nr2 > 0:
        n2[nr2 % 10] = 1
        nr2 //= 10

    counter = 0

    for i in range(0, 10):
        if n1[i] == n2[i] == 1:
            counter += 1

    return counter >= 2

def checkConsecutiveCommonDigits(numbers):
    """
    Checks if all consecutive number pairs have at least 2 common digits
    :param numbers: the list that needs to be verified
    :return: true if the condition from above is aquired, false if not
    """

    start = 0
    length = 0
    max = 0
    for i in range(0, len(numbers) - 1):
        if checkDigits(numbers[i], numbers[i+1]):
            length += 1
        else:
            if length > max:
                max = length
                start = i - max
            length = 0

    '''
    if length > 0:
        if length > max:
            max = length
            start = len(numbers) - max - 1
    '''
    if start != start + max:
        print(numbers[start: start + max + 1])
        return True
    return False
    '''
    if length > 0:
        print(numbers[start: start + max + 1])
        return True
    return False
    '''

def main():
    numbers = []
    word = "/0"
    print("Enter an array of numbers.\nPress enter one more time to stop reading.\n")

    while word != "":
        word = input()
        if(word.isnumeric()):
            numbers.append(int(word))

    print("The number list is: ", numbers)

    #numbers = [10, 1, 5, 2, 8, 12, 5, 3, 2, 19, 1, 2, 3, 5, 2, 4]
    printMenu()
    option = int(readOption())
    result = True
    if option == 1:
        result = check010Range(numbers)
    elif option == 2:
        #not working properly
        return
        result = checkElementsSum(numbers)
    elif option == 3:
        result = checkConsecutiveCommonDigits(numbers)
    elif option == 4:
        return

    if result:
        print("The array you typed have the ", option, " property.")
    else:
        print("The array you typed doesn't have the ", option, " property.")



def clearConsole():
    """
    Clear the console when needed
    :return: nothing
    """
    clear = lambda: os.system('cls')
    clear()


def readOption():
    """
    Reads the desired option from a listed menu
    :return: selected option ( from 1 to 4 )
    """
    option = input()
    while not option.isnumeric() or int(option) < 1 or int(option) > 4:
        #clearConsole()
        print("Invalid option. Try again.\n")
        printMenu()
        option = input()

    #clearConsole()
    return option


def printMenu():
    """
    Prints a menu
    :return: nothing
    """
    print("Which properties do you want to check on this list?")
    print("1. All elements are in the [0, 10] range")
    print("2. The sum of all elements is 10 - not working right now")
    print("3. All consecutive number pairs have at least 2 common digits")
    print("4. Close the app")

main()