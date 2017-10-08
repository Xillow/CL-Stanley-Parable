import door
GO = "go"

def escape():
    moveInput = input("(You exit the boss's office. Type 'go' to continue.)")
        while moveInput != GO:
            moveInput = input("(You exit the boss's office. Type 'go' to continue.)")
    moveInput = input("(You go down the stairs, back to your office. Type 'go' to continue.)")
        while moveInput != GO:
            moveInput = input("(You go down the stairs, back to your office. Type 'go' to continue.)")
    moveInput = input("(You proceed through the adjacent door to the emergency stairway. Type 'go' to continue.)")
        while moveInput != GO:
            moveInput = input("(You proceed through the adjacent door to the emergency stairway. Type 'go' to continue.)")
    moveInput = input("(You climb multiple flights. The world grows dim. Type 'go' to continue.)")
        while moveInput != GO:
            moveInput = input("(You climb multiple flights. The world grows dim. Type 'go' to continue.)")
    moveInput = input("(You see a growing light, and walk towards it. Type 'go' to continue.)")
        while moveInput != GO:
            moveInput = input("(You see a growing light, and walk towards it. Type 'go' to continue.)")
    door.door
