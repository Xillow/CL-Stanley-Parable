

CHOICE_1 = "climb out"
CHOICE_2 = "pass"
MISTAKE_LIM = 4

def window():
    
    decision = ""
    count = 0
    
    #while loop checks to make sure you have selected a correct option
    while (decision != CHOICE_1) and (decision != CHOICE_2):
        
        decision = input("what is your choice?('enter' or 'close')")
	      
         #
        if decision == CHOICE_1:
        
        
        
        elif decision == CHOICE_2:
		
	      elif count > MISTAKE_LIM:
			 
       
		
	      count += 1
