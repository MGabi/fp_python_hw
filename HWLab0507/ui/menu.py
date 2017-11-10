"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   11/2/2017 23:43
"""
def printMenu():
    print("\033[91m##############################\033[0m")
    print("\033[91m######MOVIE RENTAL STORE######\033[0m")
    print("\033[91m##############################\033[0m")
    print("")
    print("Managing the list of clients and available movies")

def printOptions():
    print("Choose one of the following options:")
    print("     \033[93m1\033[0m - \033[96mAdd\033[0m")
    print("     \033[93m2\033[0m - \033[96mRemove\033[0m")
    print("     \033[93m3\033[0m - \033[96mUpdate\033[0m")
    print("     \033[93m4\033[0m - \033[96mList\033[0m")
    print("     \033[93m5\033[0m - \033[96mRent a movie\033[0m")
    print("     \033[93m6\033[0m - \033[96mReturn a movie\033[0m")
    print("     \033[93m7\033[0m - \033[96mSearch users or movies\033[0m")
    print("     \033[93m8\033[0m - \033[96mCreate statistics\033[0m")
    print("     \033[93m9\033[0m - \033[96mUndo the last operation\033[0m")
    print("     \033[93m0\033[0m - \033[96mExit the program\033[0m")


def printChooseList():
    print("On which list do you want to make changes?")
    print("     \033[93m1\033[0m - \033[96mClients\033[0m")
    print("     \033[93m2\033[0m - \033[96mMovies\033[0m")
    print("     \033[93m3\033[0m - \033[96mRentals\033[0m")

def inputPromptForUpdateIndex(lenL):
    pr = "Which position do you want to update?\nEnter an index from 1 to " + str(lenL) + ":"
    return pr

def inputPromptForRemovalIndex(lenL):
    pr = "Which position do you want to remove?\nEnter an index from 1 to " + str(lenL) + ":"
    return pr

def printByeBye():
    print("Goodbye!")