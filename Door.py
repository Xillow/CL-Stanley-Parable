CHOICE_1 = "enter"
CHOICE_2 = "close"
MISTAKE_LIM = 5

def door():
    
    decision = ""
    count = 0
    
    #while loop checks to make sure you have selected a correct option
    while (decision != CHOICE_1) and (decision != CHOICE_2):
        
	decision = input("what is your choice?(\"enter\" or \"close\")
	
        if decision == CHOICE_1:
        
        
        elif decision == CHOICE_2:
		
	elif count > MISTAKE_LIM:
			 
        else:
            print( "No, No, No stanley please select the correct option")
		
	count += 1
