"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 12:25
"""
from domain.entities.address import Address


class UI(object):

    @staticmethod
    def readCmd():
        cmd = input(" >>> ")
        cmd = cmd.strip()
        cmd = int(cmd)
        if cmd not in [1, 2, 3]:
            raise Exception("Invalid option")
        return cmd

    @staticmethod
    def printDrivers(drivers):
        for driver in drivers:
            print(driver)

    @staticmethod
    def printAll(repoAddresses, repoDrivers):
        print("Addresses:")
        print(*repoAddresses.getAll())
        print("\n#########\n")
        print("Drivers:")
        print(*repoDrivers.getAll())

    @staticmethod
    def printMenu():
        print("1. Display all addresses and drivers")
        print("2. Print the closest drivers for a given address")
        print("3. Print the pair of drivers who are closes to each other")

    @staticmethod
    def readAddress():
        print("Enter an address of type : id,street,dx,dy - id,dx,dy - integers")
        address = input("   >>")
        address = address.split(",")
        addressObj = Address(int(address[0]), address[1], int(address[2]), int(address[3]))
        return addressObj

    @staticmethod
    def printList(listOfDrivers):
        print(*listOfDrivers)

    @staticmethod
    def printPairs(pairs):
        for pair in pairs:
            print(*pair)