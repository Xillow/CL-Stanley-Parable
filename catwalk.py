import museum
import power
ESCAPE = "escape"
MIND_CONTROL = "mind control"

def catwalk():
    door = "none"
    
    while door != ESCAPE and door != MIND_CONTROL:
    print("Stanley walked straight ahead through the large door that read Mind Control Facility.")
    input("(What is your choice? (\"escape\" or \"mind control\"))")
    
    if door == ESCAPE:
        museum.museum()
    elif door == MIND_CONTROL:
        power.power()
