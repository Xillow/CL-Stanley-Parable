import door
import time
GO = "go"

def freedom():
    print("Blackness...and a rising chill of uncertainty...Was it over?")
    time.sleep(3)
    print("Yes! He had won. He had defeated the machine, unshackled himself from someone else's command. Freedom was mere moments away.")
    time.sleep(3)
    print("And, yet, even as the immense door slowly opened, Stanley reflected on how many puzzles still lay unsolved. Where had his co-workers gone? How had he been freed from the machine's grasp? What other mysteries did this strange building hold?")
    time.sleep(7)
    print("But as sunlight streamed into the chamber, he realized none of this mattered to him. For it was not knowledge, or even power, that he had been seeking, but happiness.")
    time.sleep(6)
    print("Perhaps his goal had not been to understand, but to let go.")
    time.sleep(3)
    print("No longer would anyone tell him where to go, what to do, or how to feel. Whatever life he lives, it will be his. And that was all he needed to know. It was, perhaps, the only thing worth knowing.")
    time.sleep(6)
    lastChoice = input("Stanley stepped through the open door. ('go') ")
    while lastChoice != GO:
        lastChoice = input("Stanley stepped through the open door. ('go') ")
    print("Stanley felt the cool breeze upon his skin, the feeling of liberation, the immense possibility of the new path before him. This was exactly the way, right now, that things were meant to happen. And Stanley was happy.")
    lastChoice = ""
    lastChoice = input("(You may now return to the beginning. Type 'go'.)")
    while lastChoice != GO:
        lastChoice = input("(You may now return to the beginning. Type 'go'.)")
    door.door()
    
    
