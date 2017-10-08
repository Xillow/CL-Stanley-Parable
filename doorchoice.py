import left
import right
LEFT = "left"
RIGHT = "right"

def doorchoice():
    door = "none"

    while door != LEFT and door != RIGHT:
        print("When Stanley came to a set of 2 open doors, he entered the door on his left.")
        door = input("(What is your choice? (\"yes\" or \"no\"))")
    
        if door == LEFT:
            left.left()
        if door == RIGHT:
            right.right()
        
