import random
dice = [
    {"value": 0, "%": 0},
    {"value": 0, "%": 0},
    {"value": 0, "%": 0},
    {"value": 0, "%": 0},
    {"value": 0, "%": 0},
    {"value": 0, "%": 0}
]

#generate random number
def roll_dice():
    rand = random.random()
    if rand <= 1 / 6:
        dice[0]["value"] += 1
    elif rand < 2 / 6:
        dice[1]["value"] += 1
    elif rand < 3 / 6:
        dice[2]["value"] += 1
    elif rand < 4 / 6:
        dice[3]["value"] += 1
    elif rand < 5 / 6:
        dice[4]["value"] += 1
    else:
        dice[5]["value"] += 1

def printTable():
    # compute percentage
    for die in dice:
        die["%"] = die["value"] / 10

    # print table
    print('\nface    frequency    %')
    print("-----------------------")

    for idx, die in enumerate(dice):
        print('{0}       {1}      {2}'.format(idx + 1, die["value"], die["%"]))

# roll dice 1000 times
for x in range(0, 1000):
    roll_dice()

printTable()