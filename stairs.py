import insane
import boss
DOWN = "down"
UP = "up"

def stairs():
    stairs = "none"

    while stairs != DOWN and stairs != UP:
        print("Coming to a staircase, Stanley walked upstairs to his boss's office.")
        stairs = input("(What is your choice? (\"down\" or \"up\")) ")
    
        if stairs == DOWN:
            insane.insane()
        elif stairs == UP:
            boss.boss()
