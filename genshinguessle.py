class Ligma(object):
    def __init__(self) -> None:
        pass

#
# anemo geo pyro cryo electro hydro dendro
# 1     2   3    4    5       6     7
# sword claymore catalyst bow polearm
# 1     2        3        4   5
# height? gender? nation?
# order: weapon, vision
peepee = {
    "albedo": [1, 2],
    "aloy": [4, 4],
    "amber": [4, 3],
    "arataki itto": [2, 2],
    "barbara": [3, 6],
    "beidou": [2, 5],
    "bennett": [1, 3],
    "chongyun": [2, 4],
    "diluc": [2, 3],
    "diona": [4, 4],
    "eula": [2, 4],
    "fischl": [4, 5],
    "ganyu": [4, 4],
    "gorou": [4, 2],
    "hu tao": [5, 3],
    "jean": [1, 1],
    "kaedehara kazuha": [1, 1],
    "kaeya": [1, 4],
    "kamisato ayaka": [1, 4],
    "kamisato ayato": [1, 6],
    "keqing": [1, 5],
    "klee": [3, 3],
    "kujou sara": [4, 5],
    "lisa": [3, 5],
    "mona": [3, 6],
    "ningguang": [3, 2],
    "noelle": [2, 2],
    "qiqi": [1, 4],
    "raiden shogun": [5, 5],
    "razor": [2, 5],
    "rosaria": [5, 4],
    "sangonomiya kokomi": [3, 6],
    "sayu": [2, 1],
    "shenhe": [5, 4],
    "sucrose": [3, 1],
    "tartaglia": [4, 6],
    "thoma": [5, 3],# traveler vv
    "venti": [4, 1],# traveler ^^
    "xiangling": [5, 3],
    "xiao": [5, 1],
    "xingqiu": [1, 6],
    "xinyan": [2, 3],
    "yae miko": [3, 5],
    "yanfei": [3, 3],
    "yoimiya": [4, 3],
    "yun jin": [5, 2],
    "yunjin": [5, 2],
    "zhongli": [5, 2]
}

# ligma 
guesses = 5 # or less
guess = input("\nguess genshin char: ")
if guess not in peepee:
    print("guess again")