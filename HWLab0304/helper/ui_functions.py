
def printAvailableCommands():
    print("")
    print("\033[91m###############################")
    print("\033[91m######  CONTEST MANAGER  ######")
    print("\033[91m###############################\033[0m")
    print("")
    print("Currently available commands for\
    \nmanaging contestants list are:")
    print("")
    print("  \033[32madd\033[0m <P1 score> <P2 score> <P3 score>\
    \n  \033[32minsert\033[0m <P1 score> <P2 score> <P3 score> \033[32mat\033[0m <position>\
    \n  \033[32mremove\033[0m <position>\
    \n  \033[32mremove\033[0m <start position> \033[32mto\033[0m <end position>\
    \n  \033[32mreplace\033[0m <old score> P1 / P2 / P3 \033[32mwith\033[0m <new score>\
    \n  \033[32mlist\033[0m\
    \n  \033[32mlist sorted\033[0m\
    \n  \033[32mlist\033[0m [ < / = / > ] <score>\
    \n\ntype \033[94mexit\033[0m for closing the program.")


def needCommand():
    print("\nYou can start using those commands by tiping below:")