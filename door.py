import window
import reluctant
CHOICE_1 = "enter"
CHOICE_2 = "close"
MISTAKE_LIM = 4

def door():
    
    decision = ""
    count = 0
    
    #while loop checks to make sure you have selected a correct option
    while (decision != CHOICE_1) and (decision != CHOICE_2):
        print("All his co-workers were gone. What could it mean? Stanley decided to go to the meeting room; perhaps he had simply missed a memo.")
    	decision = input("(what is your choice?(\"enter\" or \"close\")) ")
	
        if decision == CHOICE_1:
            window.window()
        
        elif decision == CHOICE_2:
		    reluctant.reluctant()
        
    	elif count > MISTAKE_LIM:
		    print("Stanley just kept touching doors and desks and pushing buttons meaninglessly, failing to realize that he was not progressing the story at all.")
		
    	count += 1
