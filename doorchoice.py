import left
import right
LEFT = "left"
RIGHT = "right"

def doorchoice():
	
	door = ""

	while door != LEFT and door != RIGHT:
        
		print("When Stanley came to a set of 2 open doors, he entered the door on his left.")
		door = input("(What is your choice? ('left' or 'right'))")
    
		if door == LEFT:
            left.left()
			
		elif door == RIGHT:
			right.right()
