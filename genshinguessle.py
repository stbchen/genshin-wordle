import random
from re import X
#
# anemo geo pyro cryo electro hydro dendro
# 1     2   3    4    5       6     7
# sword claymore catalyst bow polearm
# 1     2        3        4   5
# height? gender? nation?
# order: weapon, vision
peepee = {
    "albedo": ["sword", "geo"],
    "aloy": ["bow", "cryo"],
    "amber": [4, "pyro"],
    "arataki itto": ["claymore", "geo"],
    "barbara": ["catalyst", "hydro"],
    "beidou": ["claymore", "electro"],
    "bennett": ["sword", "pyro"],
    "chongyun": ["claymore", "cryo"],
    "diluc": ["claymore", "pyro"],
    "diona": [4, "cryo"],
    "eula": ["claymore", "cryo"],
    "fischl": [4, "electro"],
    "ganyu": [4, "cryo"],
    "gorou": [4, "geo"],
    "hu tao": [5, "pyro"],
    "jean": ["sword", "anemo"],
    "kaedehara kazuha": ["sword", "anemo"],
    "kaeya": ["sword", "cryo"],
    "kamisato ayaka": ["sword", "cryo"],
    "kamisato ayato": ["sword", "hydro"],
    "keqing": ["sword", "electro"],
    "klee": ["catalyst", "pyro"],
    "kujou sara": [4, "electro"],
    "lisa": ["catalyst", "electro"],
    "mona": ["catalyst", "hydro"],
    "ningguang": ["catalyst", "geo"],
    "noelle": ["claymore", "geo"],
    "qiqi": ["sword", "cryo"],
    "raiden shogun": [5, "electro"],
    "razor": ["claymore", "electro"],
    "rosaria": [5, "cryo"],
    "sangonomiya kokomi": ["catalyst", "hydro"],
    "sayu": ["claymore", "anemo"],
    "shenhe": [5, "cryo"],
    "sucrose": ["catalyst", "anemo"],
    "tartaglia": [4, "hydro"],
    "thoma": [5, "pyro"],# traveler vv
    "venti": [4, "anemo"],# traveler ^^
    "xiangling": [5, "pyro"],
    "xiao": [5, "anemo"],
    "xingqiu": ["sword", "hydro"],
    "xinyan": ["claymore", "pyro"],
    "yae miko": ["catalyst", "electro"],
    "yanfei": ["catalyst", "pyro"],
    "yoimiya": [4, "pyro"],
    "yun jin": [5, "geo"],
    "zhongli": [5, "geo"]
}
MAX_ATTEMPT = 7
play_again = True
while play_again:
    ans = random.choice(list(peepee.keys()))
    attempt = 0
    while (attempt < MAX_ATTEMPT):
        guess = input("\nguess genshin char: ").lower()
        if guess not in peepee:
            print(" invalid input") 
        elif guess != ans:
            if peepee[guess][0] == peepee[ans][0]:
                wep = "O"
            else: 
                wep = "X"
            if peepee[guess][1] == peepee[ans][1]:
                vision = "O"
            else:
                vision = "X"
            print(f"{guess}: \t{wep} weapon \t{vision} vision")
            attempt += 1
        else:
            print("correct")
            break
            
    if attempt == MAX_ATTEMPT:
        print("game over")
    
    inp = input("play again? y/n ")
    play_again = True if inp.lower() == "y" else False

"""
do i run it

if u put guesses back inside the loop we can ask to play again or quit
no
we need to generate a new answer
yea itll just go in the if or something
we could also structure the prints in the game to align in like a table
like print("name    weapon  vision")
print("{guess} {wep} {vision})
run it
oops the prompt for guess genshin char has to change now cuz itll ruin the table unless we indent for it or something idk
wait dude there shouldnt even be a number of guesses right
no

why 
are we done already
is there a league of legends wordle

okay we also need to make this more readable, i think we dont need to store each thing as an int just put the whole string
i think we should do the checks for vision and weapo nand then put it in one print with like x for wrong and o for right orsomething to match the wordle symbols

"""