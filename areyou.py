import yes
import no
# import time
YES = "yes"
NO = "no"

def areyou():
    sickGag = "none"
    
    print("At first, Stanley assumed he had broken the map, until he heard this narration and realized it was part of the game all along. He then praised the game for its insightful and witty commentary into the nature of video game structure and its examination of structural narrative tropes.")
    # time.sleep(8)
    print("So now that you're here, what do you think? Isn't this a fun and unique place to be? Why don't we take a minute just to drink it all in!")
    # time.sleep(6)
    
    while sickGag != YES and sickGag != NO:
        print("Okay I'm over it now. What do you think, are you sick of this gag yet?")
        sickGag = input("YES/NO ")
    
        if sickGag == YES:
            yes.yes()
        elif sickGag == NO:
            no.no()
