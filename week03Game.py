
player = {
    "name":[]
}

def pay(minNum, maxNum):
        pay(3, 10)


def printGraphic(name):
    if(name == "miser"):
        print('   _____    _____    ')
        print('  /     \  /     \   ')
        print('  \      \/      /   ')
        print('   \            /    ')
        print('    \          /     ')
        print('     \        /      ')
        print('      \      /       ')
        print('       \    /        ')
        print('        \  /         ')
        print('         --          ')
        print('  see you next time  ')

    if(name == "paloma"):
        print('       _               ')
        print('      | |              ')
        print('      | |       _ _    ')
        print('     _| |_ _ _/_ _  \  ')
        print('    | | |         |  | ')
        print('    |_| |_ _ _ _ _|_/  ')
        print('    | | |         |    ')
        print('    | | |     / \ |    ')
        print('    | | |    / \ ||    ')
        print('    | | |  _ \ _ /|    ')
        print('    | | | | |     |    ')
        print('    | | |  -      |    ')
        print('    | | |   /\    |    ')
        print('    | |_|   \/    |    ')
        print(' \  |_ _ _ _ _ _ _|  / ')
        print('  \ _ _ _ _ _ _ _ _ /  ')
        print('                       ')
        print('         paloma        ')

    if(name == "espresso martini"):
        print('  _ _ _ __ _ _ _ _ _ _ _ _ _ _  ')
        print('  \---_|__|-__---------------/  ')
        print('   \ |_|   |__|             /   ')
        print('    \                      /    ')
        print('     \                    /     ')
        print('      \                  /      ')
        print('       \                /       ')
        print('        \              /        ')
        print('         \            /         ')
        print('          \          /          ')
        print('           \        /           ')
        print('            --------            ')
        print('             \    /             ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('              |  |              ')
        print('       _ _ _ _|  |_ _ _ _       ')
        print('      |_ _ _ _ _ _ _ _ _ |      ')
        print('                                ')
        print('        espresso martini        ')
 


def introStory():
    print("Hello there, may I know your name?")
    player["name"] = input("Please enter your name >")

    print("Welcom to the cocktail factory" + player["name"] + ">.<")
    print("Let me introduce my cocktail factory to you...")
    print("In cocktail factory, you can buy a cocktail and enjoy,")
    print("or, you can also make your own cocktail.")
    print("Friendly reminder: if you choose to make your own cocktails, we'll buy it for you.")
    print("Would you like to buy a cocktail?")

    pcmd = input("please choose yes or no >")
    
    #add while loop

    if (pcmd == "yes"):
        print("How much you're willing to pay for this cocktail?")

        a = input("Enter a number: ")
        if(a >= 10):
             print("Thank you for your generosity" + player["name"] + ",")
             print("Here is your expresso martini,")
             print("Enjoy!")
             printGraphic("espresso martini")

        if(3 <= a < 10):
            print("Thank you" + player["name"] + ",")
            print("Enjoy your paloma!")
            printGraphic("paloma")

        if(a < 3):
            print("Alright, see you next time, miser.")
            printGraphic("miser")

    elif(pcmd == "no"):
        print("No? Maybe you want to DIY your cocktail")
        pcmd = input("please choose yes or no >")

        if (pcmd == "yes"):
             print("to be continued...")

    else:
        print("How much you're willing to pay for this cocktail?")



def main():
    introStory()

main()






