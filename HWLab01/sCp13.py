def findDivisors(currNumber):
    if currNumber == 1:
        return [1]

    divs = []
    for i in range(2, currNumber + 1):
        if currNumber % i == 0:
            while currNumber % i == 0:
                currNumber /= i
            divs.append(i)

    return divs


def makeSequence(n):
    if n < 1:
        print("Invalid data")
        return
    if n == 1:
        return 1

    index = 0
    currNumber = 1
    divisors = []
    while True:
        divisors.clear()
        divisors = findDivisors(currNumber)
        index += len(divisors)

        if(index >= n):
            print(divisors[index - n - 1])
            return

        currNumber += 1


def main():
    n = int(input("Enter the n number: "))
    makeSequence(n)

main()