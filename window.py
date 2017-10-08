import doorchoice
import areyou

CHOICE_1 = "climb out"
CHOICE_2 = "pass"

def window():

    decision = ""

    #while loop checks to make sure you have selected a correct option
    while (decision != CHOICE_1) and (decision != CHOICE_2):

        decision = input("what is your choice?('climb out' or 'pass')")

        if decision == CHOICE_1:
            areyou.areyou()

        elif decision == CHOICE_2:

            doorchoice.doorchoice()


