"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 12:11
"""
from domain.entities.address import Address
from domain.entities.driver import Driver
from domain.repository.repo import Repository
from ui.ui import UI


class Controller(object):

    def __init__(self):
        self.fileAddresses = "addresses.txt"
        self.fileDrivers = "drivers.txt"
        self.addresToCalculate = None

    def startApp(self):
        """
        Main function for starting the app
        :return:
        """
        #
        # with open(self.fileAddresses, "w") as f:
        #     for i in range(10):
        #         f.write(str(Address(i, "Address" + str(i), str(i*3), str(i*4))))
        # with open(self.fileDrivers, "w") as f:
        #     for i in range(10):
        #         f.write(str(Driver("Name" + str(i), str(i*5), str(i*6))))
        repoAddresses = Repository(self.fileAddresses, Address)
        repoDrivers = Repository(self.fileDrivers, Driver)
        while True:
            UI.printMenu()
            try:
                cmd = UI.readCmd()
                if cmd == 1:
                    UI.printAll(repoAddresses, repoDrivers)
                if cmd == 2:
                    address = UI.readAddress()
                    listOfDrivers = self.calculateDistance(address, repoDrivers)
                    UI.printList(listOfDrivers)
                if cmd == 3:
                    pairs = self.getPairOfDrivers(repoDrivers)
                    UI.printPairs(pairs)
            except Exception as ex:
                print(ex)

    def calculateDistance(self, address, repoDrivers):
        """
        Calculate the distance between an address and a driver
        :param address:
        :param repoDrivers:
        :return:
        """
        drivers = repoDrivers.getAll()
        self.addresToCalculate = address
        for i in range(len(drivers)):
            for j in range(len(drivers)):
                if self.distanceFrom(drivers[i], drivers[j]):
                    tmp = drivers[i]
                    drivers[i] = drivers[j]
                    drivers[j] = tmp
        return drivers
        #print(*drivers)

    def getPairOfDrivers(self, repoDrivers):
        """
        Returns the pair of closest drivers
        :param repoDrivers:
        :return:
        """
        drivers = repoDrivers.getAll()
        pairs = []
        poz = 0
        dist = self.manhattan(drivers[0], drivers[1])
        self.addresToCalculate = Address(1, "abc", 0, 0)
        for i in range(len(drivers)):
            for j in range(len(drivers)):
                if self.distanceFrom(drivers[i], drivers[j]):
                    tmp = drivers[i]
                    drivers[i] = drivers[j]
                    drivers[j] = tmp
        for i in range(0, len(drivers), 2):
            pairs.append([drivers[i], drivers[i+1]])
        return pairs


    def distanceFrom(self, d1, d2):
        """
        Return the boolean value resulting from comparation of two distances
        :param d1: driver1
        :param d2: driver2
        :return: True if driver1 is closer to the address
        """
        return self.manhattanDistanceAddressDriver(self.addresToCalculate, d1) < self.manhattanDistanceAddressDriver(self.addresToCalculate, d2)

    def manhattanDistanceAddressDriver(self, address, driver):
        """
        Distance between an address and a driver
        :param address:
        :param driver:
        :return:
        """
        return abs(address.dx - driver.dx) + abs(address.dy - driver.dy)

    def manhattan(self, d1, d2):
        """
        distance between two drivers
        :param d1:
        :param d2:
        :return:
        """
        return abs(d1.dx - d2.dx) + abs(d2.dy - d2.dy)
