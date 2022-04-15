import random

characters = {
    "albedo": ["sword", "geo", "mondstadt"],
    "aloy": ["bow", "cryo", "collab"],
    "amber": ["bow", "pyro", "mondstadt"],
    "arataki itto": ["claymore", "geo", "inazuma"],
    "barbara": ["catalyst", "hydro", "mondstadt"],
    "beidou": ["claymore", "electro", "liyue"],
    "bennett": ["sword", "pyro", "mondstadt"],
    "chongyun": ["claymore", "cryo", "liyue"],
    "diluc": ["claymore", "pyro", "mondstadt"],
    "diona": ["bow", "cryo", "mondstadt"],
    "eula": ["claymore", "cryo", "mondstadt"],
    "fischl": ["bow", "electro", "mondstadt"],
    "ganyu": ["bow", "cryo", "liyue"],
    "gorou": ["bow", "geo", "inazuma"],
    "hu tao": ["polearm", "pyro", "liyue"],
    "jean": ["sword", "anemo", "mondstadt"],
    "kaedehara kazuha": ["sword", "anemo", "inazuma"],
    "kaeya": ["sword", "cryo", "mondstadt"],
    "kamisato ayaka": ["sword", "cryo", "inazuma"],
    "kamisato ayato": ["sword", "hydro", "inazuma"],
    "keqing": ["sword", "electro", "liyue"],
    "klee": ["catalyst", "pyro", "mondstadt"],
    "kujou sara": ["bow", "electro", "inazuma"],
    "lisa": ["catalyst", "electro", "mondstadt"],
    "mona": ["catalyst", "hydro", "mondstadt"],
    "ningguang": ["catalyst", "geo", "liyue"],
    "noelle": ["claymore", "geo", "mondstadt"],
    "qiqi": ["sword", "cryo", "liyue"],
    "raiden shogun": ["polearm", "electro", "inazuma"],
    "razor": ["claymore", "electro", "mondstadt"],
    "rosaria": ["polearm", "cryo", "mondstadt"],
    "sangonomiya kokomi": ["catalyst", "hydro", "inazuma"],
    "sayu": ["claymore", "anemo", "inazuma"],
    "shenhe": ["polearm", "cryo", "liyue"],
    "sucrose": ["catalyst", "anemo", "mondstadt"],
    "tartaglia": ["bow", "hydro", "liyue"],
    "thoma": ["polearm", "pyro", "inazuma"],
    "venti": ["bow", "anemo", "mondstadt"],
    "xiangling": ["polearm", "pyro", "liyue"],
    "xiao": ["polearm", "anemo", "liyue"],
    "xingqiu": ["sword", "hydro", "liyue"],
    "xinyan": ["claymore", "pyro", "liyue"],
    "yae miko": ["catalyst", "electro", "inazuma"],
    "yanfei": ["catalyst", "pyro", "liyue"],
    "yoimiya": ["bow", "pyro", "inazuma"],
    "yun jin": ["polearm", "geo", "liyue"],
    "zhongli": ["polearm", "geo", "liyue"]
}
MAX_ATTEMPT = 5
play_again = True
while play_again:
    ans = random.choice(list(characters.keys()))
    attempt = MAX_ATTEMPT
    while attempt > 0:
        guess = input("\nguess genshin char: ").lower()
        if guess not in characters:
            print("invalid input") 
        elif guess != ans:
            wep = "O" if characters[guess][0] == characters[ans][0] else "X"
            vision = "O" if characters[guess][1] == characters[ans][1] else "X"
            nation = "O" if characters[guess][2] == characters[ans][2] else "X"
            attempt -= 1
            print(f"{guess}: \t{wep} weapon \t{vision} vision \t{nation} nation \t{attempt} guesses left")
        else:
            print("correct")
            break
            
    if attempt == 0:
        print(f"game over, answer was {ans.title()}")

    inp = input("play again? y/n ")
    play_again = True if inp.lower() == "y" else False
