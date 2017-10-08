import door
import time
ESCAPE = "escape"

def no():
    print("Ah, well in that case we'll continue! But now here comes the real question: what do you think would have happened if you had told me that you wanted this to stop? Do you think it would have been particularly different?")
    time.sleep(8)
    print("Would I have taken this same idea but rephrased it superficially to fit that answer? Perhaps you never would even have thought of it if I hadn't brought up the issue in the first place!")
    time.sleep(6)
    print("Oh, now think about it, will it be worth it for you to restart, and then come BACK here, just to do the other option? Clearly this whole gag takes some time, what if the other option is even longer! How long will you spend in total just to have heard all the narration!")
    time.sleep(8)
    print("Or - oh this is rich! - perhaps you've just played the other option and now you've come to see what happens in this one! So, what do you think, which choice was the better one?")
    time.sleep(6)
    print("Imagine if you had selected 'continue' on your first playthrough, how tantalizing it would be, not knowing what happens when you pick the other option. Indeed, you are one of the lucky ones.")
    time.sleep(5)
    print("Though if the other option is really miserable to listen to then perhaps you're not. In fact, i'm just going to say that no one who's listening to this is lucky.")
    time.sleep(4)
    choice = input("Well now I've built up the other option so much that I'm going to stop talking and leave you to your decision whether to come back here, continue with the game, or just sit here in this spot forever and ever. Cheers. ")
    while choice != ESCAPE:
        print("...")
