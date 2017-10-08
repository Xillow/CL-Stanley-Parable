import stairs

CHOICE_1 = "pass"
CHOICE_2 = "enter"
LEAVE = "leave"

def left():
	decision = ""
	count = 0
	inCloset = 8
	inputAnswer = ""
    

    #while loop checks to make sure you have selected a correct option
	while (decision != CHOICE_1) and (decision != CHOICE_2):
        
		decision = input("what is your choice?('pass' or 'enter')")
	
		if decision == CHOICE_1:
			stairs.stairs()
        
		elif decision == CHOICE_2:
		
			print("In the meeting room: \n")
			
			print("Yet there was not a single person here either. Feeling a wave of disbelief, Stanley decided to go up to his boss's office, hoping he might find an answer there.")
			print("Entering the broom closet:\n")
			
			print("Stanley stepped into the broom closet, but there was nothing here, so he turned around and got back on track.")
			
			print("There was nothing here. No choice to make. No path to follow. Just an empty broom closet. No reason to still be here.")
		      		      
			while (count < inCloset):
		      
				inputAnswer = input("what is your choice?('leave' or 'stay')")
				
				if inputAnswer != LEAVE and count == 0:
					print("It was baffling that Stanley was still just sitting in the broom closet. He wasn't even doing anything. At least if there was something to interact with, he'd be justified in some way. As it is, he's literally just standing there, doing sweet FA.\n")
					
					count += 1
					
				elif inputAnswer != LEAVE and count == 1:
					print("Are you... Are you really still in the broom closet? Standing around doing nothing? Why? Please offer me some explanation here; I'm- I'm genuinely confused.\n")
					
					count += 1
					
				elif inputAnswer != LEAVE and count == 2:
					print("You do realize there's no choice or anything in here right? If I said \"Stanley walked past the broom closet\" at least you would've had a reason for exploring it to find out. But it didn't even occur to me, because literally, this closet, is of absolutely, no significance to the story, whatsoever. I never would've thought to mention it.\n")					
					count += 1
					
				elif inputAnswer != LEAVE and count == 3:
					print("Maybe to you, this is somehow it's own branching path. Maybe, when you go talk about this with your friends, you'll say: \"OH! DID U GET THE BROOM CLOSET ENDING? THEB ROOM CLOSET ENDING WAS MY FAVRITE!1 XD\" I hope your friends find this concerning.\n")
					 
					count += 1
					
				elif inputAnswer != LEAVE and count == 4:
					print("Stanley was fat and ugly, and really, really stupid. He probably only got the job because of a family connection; that's how stupid he is. That, or with drug money. Also, Stanley is addicted to drugs and hookers.\n")
					count += 1
					
				elif inputAnswer != LEAVE and count == 5:
					print("Well, I've come to a very definite conclusion about what's going on right now. You're dead. You got to this broom closet, explored it a bit, and were just about to leave because there's nothing here, when a physical malady of some sort shut down your central nervous system and you collapsed on the keyboard. Well, in a situation like this, the responsible thing is to alert someone nearby so as to ensure that your body is taken care of, before it begins to decompose.\n")
					count += 1
					
				elif inputAnswer != LEAVE and count == 6:
					print("HELLO!? ANYONE WHO HAPPENS TO BE NEARBY!! THE PERSON AT THIS COMPUTER IS DEAD!! HE OR SHE HAS FALLEN PREY TO ANY NUMBER OF YOUR COUNTLESS HUMAN PHYSIOLOGICAL VULNERABILITIES. IT'S INDICATIVE OF THE LONG-TERM SUSTAINABILITY OF YOUR SPECIES. PLEASE REMOVE THEIR CORPSE FROM THE AREA AND INSTRUCT ANOTHER HUMAN TO TAKE THEIR PLACE AT THE COMPUTER, MAKING SURE THEY UNDERSTAND BASIC FIRST-PERSON VIDEO GAME MECHANICS, AND FILLING THEM IN ON THE HISTORY OF NARRATIVE TROPES IN VIDEO GAMING, SO THAT THE IRONY AND INSIGHTFUL COMMENTARY OF THIS GAME IS NOT LOST ON THEM.\n")
					count += 1
					  
				elif inputAnswer != LEAVE:
					print("...")
				else:
					count += 1
			stairs.stairs()
                
                
            
