import random
import math
from datetime import datetime


class Atribbutes:
    name = ""
    gender = ""
    age = ""
    aliases = []
    traits = []
    pronouns = []
    birthplace = []
    lives = 20
    stats = []
    occupation = ""
    reason = ""
    nemesis = ""
    weapon = []
    tier = 0
    gold = 0
    inv = []
    companion = ""
    companiondied = False
    exp = 0
    expcap = 50
    level = 1


class Meeting:
    name = ""
    gender = ""
    lives = random.randint(10, 20)
    race = ""
    weapon = []
    pronouns = []
    stats = []


def levelUp(mainchar):
    print("Level up!\nPick a stat to improve:")
    while True:
        a = input(f"\n 1 - STR ({mainchar.stats[0]})\n 2 - AGI ({mainchar.stats[1]})\n 3 - INT ({mainchar.stats[2]})\n 4 - CHA ({mainchar.stats[3]}).\n")
        if a == "1":
            mainchar.stats[0] += 1
            break
        elif a == "2":
            mainchar.stats[1] += 1
            break
        elif a == "3":
            mainchar.stats[2] += 1
            break
        elif a == "4":
            mainchar.stats[3] += 1
            break
        else:
            print("Wrong input.")


def checkLevel(mainchar):
    while True:
        if mainchar.exp >= mainchar.expcap:
            levelUp(mainchar)
            mainchar.exp = 0
            mainchar.expcap += 15
            mainchar.level += 1
        else:
            break


def createChar(playdict):
    names = open("chargen/names.txt", 'r').read()
    names = names.split("\n\n")
    genderc = random.randint(1, 3)
    mainchar = Atribbutes()
    if genderc == 1:
        mainchar.name = random.choice(names[0].split("\n"))
        mainchar.gender = "man"
        mainchar.pronouns = ["he", "him", "his"]
    elif genderc == 2:
        mainchar.name = random.choice(names[1].split("\n"))
        mainchar.gender = "woman"
        mainchar.pronouns = ["she", "her", "her"]
    else:
        mainchar.name = random.choice(names[random.randint(0,1)].split("\n"))
        mainchar.gender = "person"
        mainchar.pronouns = ["they", "them", "their"]
    traits = open("chargen/traits.txt", 'r').read()
    traits = traits.split("\n")
    twotraits = []
    while len(twotraits) < 2:
        traitchose = random.choice(traits)
        if traitchose not in twotraits:
            twotraits.append(traitchose)
    traitchose = []
    for i in twotraits:
        traitchose.append(random.choice(i.split(",")))
    mainchar.traits.extend(traitchose)
    aliases = open("chargen/aliases.txt", 'r').read()
    aliases = aliases.split("\n")
    for i in mainchar.traits:
        for j in aliases:
            aliac = j.split("|")
            if i == aliac[0]:
                aliac = aliac[1].split(",")
                mainchar.aliases.append("The " + random.choice(aliac))
    birthplace = random.choice(playdict["toponims"][0].split("\n"))
    birthK = []
    while len(birthK) < 2:
        topchose = random.choice(birthplace.split("|")[0].split(","))
        if topchose not in birthK:
            birthK.append(topchose)
    birthK.append(random.choice(birthplace.split("|")[1].split(",")))
    mainchar.birthplace = [birthK[0], birthK[1], birthK[2]]
    occ = open("chargen/occ.txt", 'r').read()
    occ = occ.split("\n\n")
    mainchar.tier = random.randint(1, 3)
    if mainchar.tier == 1:
        tier = occ[0].split("\n")
        del tier[0]
        mainchar.occupation = random.choice(tier).split("|")
        mainchar.stats = mainchar.occupation[1].split(",")
        mainchar.occupation = mainchar.occupation[0]
        mainchar.gold += random.randint(1, 10)
    elif mainchar.tier == 2:
        tier = occ[1].split("\n")
        del tier[0]
        mainchar.occupation = random.choice(tier).split("|")
        mainchar.stats = mainchar.occupation[1].split(",")
        mainchar.occupation = mainchar.occupation[0]
        mainchar.gold += random.randint(10, 25)
    else:
        tier = occ[2].split("\n")
        del tier[0]
        mainchar.occupation = random.choice(tier).split("|")
        mainchar.stats = mainchar.occupation[1].split(",")
        mainchar.occupation = mainchar.occupation[0]
        mainchar.gold += random.randint(40, 70)
    stats = []
    for i in mainchar.stats:
        stats.append(int(i) + random.randint(-1, 1))
    mainchar.stats = stats
    reason = open("chargen/reason.txt", 'r').read()
    reason = reason.split("\n")
    mainchar.reason = random.choice(reason)
    mainchar.nemesis = random.choice(playdict["nemnames"][0].split("\n")) + " " + random.choice(
        playdict["nemnames"][1].split("\n"))
    mainchar.weapon = pickWeapon(mainchar.tier)
    if random.randint(1, 20) > 10:
        if mainchar.occupation == "bard":
            mainchar.inv.append(random.choice(["lyre", "flute", "lute"]))
        elif mainchar.occupation == "engineer" or mainchar.occupation == "scholar":
            mainchar.inv.append(random.choice(["rope", "protractor", "abacus"]))
        elif mainchar.occupation == "monk" or mainchar.occupation == "archaeologist":
            mainchar.inv.append(random.choice(["book", "stone idol"]))
        elif mainchar.occupation == "aristocrat" or mainchar.occupation == "treasurer" or mainchar.occupation == "merchant":
            mainchar.inv.append(random.choice(["sigil", "golden cufflink", "lucky dime"]))
    return mainchar


def pickWeapon(tier):
    weapon = open("chargen/weapon.txt", 'r').read()
    weapon = weapon.split("\n\n")
    newweap = []
    if tier == 1:
        newweap.extend(random.choice(weapon[0].split("\n")).split("|"))
        newweap[2] = int(newweap[2])
        if newweap[1] == "m":
            newweap.extend(random.choice(
                [["rusty", "a", -2], ["worn", "a", -2], ["old", "an", -1], ["blunt", "a", -1], ["servicable", "a", 0]]))
        elif newweap[1] == "n":
            newweap.extend(random.choice(
                [["rusty", "a", -2], ["worn", "a", -2], ["old", "an", -1], ["unbalanced", "a", -1],
                 ["servicable", "a", 0], ["new", "a", 0]]))
        else:
            newweap.extend(["simple", "a", 0])
    elif tier == 2:
        newweap.extend(random.choice(weapon[1].split("\n")).split("|"))
        newweap[2] = int(newweap[2])
        if newweap[1] == "m":
            newweap.extend(random.choice(
                [["worn", "a", -2], ["old", "an", -1], ["blunt", "a", -1], ["new", "a", 0], ["servicable", "a", 0],
                 ["sharp", "a", 1]]))
        elif newweap[1] == "n":
            newweap.extend(random.choice(
                [["worn", "a", -2], ["old", "an", -1], ["unbalanced", "a", -1], ["servicable", "a", 0], ["new", "a", 0],
                 ["balanced", "a", 1], ["trusty", "a", 1]]))
        else:
            newweap.extend(["simple", "a", 0])
    elif tier == 3:
        newweap.extend(random.choice(weapon[2].split("\n")).split("|"))
        newweap[2] = int(newweap[2])
        if newweap[1] == "m":
            newweap.extend(random.choice(
                [["blunt", "a", -1], ["servicable", "a", 0], ["new", "a", 0], ["sharp", "a", 1],
                 ["excellent", "a", 2]]))
        elif newweap[1] == "n":
            newweap.extend(random.choice(
                [["old", "an", -1], ["servicable", "a", 0], ["new", "a", 0], ["balanced", "a", 1], ["trusty", "a", 1],
                 ["excellent", "an", 2]]))
        else:
            newweap.extend(["simple", "a", 0])
    else:
        newweap.extend(random.choice(weapon[3].split("\n")).split("|"))
        newweap[2] = int(newweap[2])
        if newweap[1] == "m":
            newweap.extend(
                random.choice([["servicable", "a", 0], ["new", "a", 0], ["sharp", "a", 1], ["excellent", "a", 2]]))
        elif newweap[1] == "n":
            newweap.extend(random.choice(
                [["servicable", "a", 0], ["new", "a", 0], ["balanced", "a", 1], ["trusty", "a", 1],
                 ["excellent", "an", 2]]))
        else:
            newweap.extend(["simple", "a", 0])
    newweap.append((newweap[2] + newweap[5]) * 10)
    return newweap


def importStories():
    playdict = {
        "char": [],
        "animv": [],
        "animadj": [],
        "obj": [],
        "inanimv": [],
        "inanimagj": [],
        "adv": [],
        "time": [],
        "place": [],
        "toponims": [],
        "weapons": [],
        "charnames": [],
        "nemnames": [],
        "dun": "",
        "creatures": [],
    }
    names = open("eventgen/charnames.txt", 'r', encoding="UTF-8").read()
    names = names.split("\n\n")
    nemnames = open("chargen/nemnames.txt", 'r').read()
    nemnames = nemnames.split("\n\n")
    animv = open("storygen/animv.txt", 'r').read()
    animv = animv.split("\n")
    animadj = open("storygen/animadj.txt", 'r').read()
    animadj = animadj.split("\n")
    obj = open("storygen/obj.txt", 'r').read()
    obj = obj.split("\n")
    inanimv = open("storygen/inanimv.txt", 'r').read()
    inanimv = inanimv.split("\n")
    inanimagj = open("storygen/inanimagj.txt", 'r').read()
    inanimagj = inanimagj.split("\n")
    adv = open("storygen/adv.txt", 'r').read()
    adv = adv.split("\n")
    time = open("storygen/time.txt", 'r').read()
    time = time.split("\n")
    place = open("storygen/place.txt", 'r').read()
    place = place.split("\n")
    toponims = open("chargen/toponims.txt", 'r', encoding="UTF-8").read()
    toponims = toponims.split("\n\n")
    weapon = open("chargen/weapon.txt", 'r').read()
    weapon = weapon.split("\n\n")
    weapons = []
    for i in weapon:
        for j in i:
            weapons.extend(j)
    creatures = open("eventgen/creatures.txt", 'r').read()
    creatures = creatures.split("\n\n")
    playdict["charnames"].extend(names)
    playdict["nemnames"].extend(nemnames)
    playdict["animv"].extend(animv)
    playdict["animadj"].extend(animadj)
    playdict["obj"].extend(obj)
    playdict["inanimv"].extend(inanimv)
    playdict["inanimagj"].extend(inanimagj)
    playdict["adv"].extend(adv)
    playdict["time"].extend(time)
    playdict["place"].extend(place)
    playdict["toponims"].extend(toponims)
    playdict["weapons"].extend(weapons)
    playdict["dun"] = random.choice(toponims[1].split(','))
    playdict["creatures"].extend(creatures)
    return playdict


def Safeinput():
    print(f"{mainchar.name} stayed awile in that room.")
    looked = False
    while True:
        a = input("Enter an action: \"inv\", \"look\", \"stats\", \"quit\".  -> ")
        if a == "inv" or a == "i":
            if len(mainchar.inv) != 0:
                if mainchar.companion != "":
                    while True:
                        b = input("Enter target: \"hero\", \"ally\".  -> ")
                        if b == "hero" or b == "h" or b == "self" or b == "s":
                            HealSelf()
                            break
                        elif b == "ally" or b == "a" or b == "friend" or b == "f" or b == "c":
                            HealComp()
                            break
                        else:
                            print("Wrong input.")
                else:
                    HealSelf()
            else:
                print("There's nothing in the inventory.")
        elif a == "look" or a == "l":
            if (random.randint(1, 20)+mainchar.stats[2]) > 15 and not looked:
                gold = random.randint(10, 40)
                print("Having a good look around", mainchar.name, "found", gold, "coins.")
                mainchar.gold += gold
                if (random.randint(1, 20)+mainchar.stats[2]) > 15:
                    newitem = random.choice(["health potion", "medicinal herb", "agility potion", "strength potion"])
                    mainchar.inv.append(newitem)
                    print(f"Found {newitem}.")
                looked = True
            else:
                print("Nothing around.")
                looked = True
        elif a == "stats" or a == "s":
            Stat()
        elif a == "quit" or a == "q" or a == "exit" or a == "e":
            break
        else:
            print("Wrong input.")


def Enemyinput(creaturelives, creatstats, creatures, anger):
    newcreat = [creatures.split("|")[0], "it", "them", "their", creatures.split("|")[0]]
    creaturesent = open("eventgen/creatures.txt", "r").read()
    creaturesent = creaturesent.split("\n\n")[2].split("\n")
    sentences = open("storygen/sentences.txt", 'r').read()
    sentences = sentences.split("\n\n")
    while True:
        if creaturelives > 0:
            if creatures.split("|")[1] == "s" and anger == 0:
                a = input("Enter an action: \"fight\", \"look\", \"stats\", \"run\".  -> ")
                if a == "run" or a == "r":
                    if creatstats[2] + random.randint(-1, 1) > mainchar.stats[2] + random.randint(0, 2):
                        print(creatures.split("|")[0].capitalize(), "is more agile, it won't let hero run away!")
                        return "f"
                    else:
                        print("Character ran away from the", creatures.split("|")[0])
                        if random.randint(1, 20) > 15:
                            if len(mainchar.inv) != 0:
                                lost = random.choice(mainchar.inv)
                                mainchar.inv.remove(lost)
                                print(f"While running away, {lost} slipped from {mainchar.name}'s bag and now lost.")
                        return "r"
                elif a == "look" or a == "l":
                    creatureinfo = ""
                    for k in creaturesent:
                        if k.split("|")[0] == creatures.split('|')[0]:
                            creatureinfo = random.choice(k.split("|")[1::])
                    print(f"{creatureinfo} \nHealth: {creaturelives}. Stats: STR {creatstats[0]}, AGI {creatstats[1]}, INT {creatstats[2]}, CHA {creatstats[3]}. \n It looks like it could be persuaded not to fight. Unsuccessful persuation will result in a fight.")
                    while True:
                        b = input("Try it?(y/n) ")
                        if b == "y" or b == "Y" or b == "yes" or b == "Yes":
                            if creatstats[3] + random.randint(0, 2) > mainchar.stats[3] + random.randint(0, 2):
                                print(replacing(replacingcreat(random.choice(sentences[15].split("\n")), newcreat)), end="")
                                return "f"
                            else:
                                return "p"
                        elif b == "n" or b == "N" or b == "no" or b == "Nos":
                            break
                        else:
                            print("Input \"y\" or \"n\".")
                elif a == "stats" or a == "s":
                    Stat()
                elif a == "fight" or a == "f":
                    return "f"
                else:
                    print("Wrong input.")
            else:
                a = input("Enter an action:  \"fight\", \"look\", \"stats\", \"run\".  -> ")
                if a == "run" or a == "r":
                    if creatstats[2] + random.randint(0, 2) > mainchar.stats[2] + random.randint(0, 2):
                        print(creatures.split("|")[0], "is more agile, it won't let hero run away!")
                        return "f"
                    else:
                        print("Character ran away from the", creatures.split("|")[0])
                        return "r"
                elif a == "look" or a == "l":
                    creatureinfo = ""
                    for k in creaturesent:
                        if k.split("|")[0] == creatures.split('|')[0]:
                            creatureinfo = random.choice(k.split("|")[1::])
                    print(f"{creatureinfo} \nHealth: {creaturelives}. Stats: STR {creatstats[0]}, AGI {creatstats[1]}, INT {creatstats[2]}, CHA {creatstats[3]}. \n This creature can't be persuaded not to fight.")
                elif a == "stats" or a == "s":
                    Stat()
                elif a == "fight" or a == "f":
                    return "f"
                else:
                    print("Wrong input.")
        else:
            return


def Stat():
    print(f"{mainchar.name} {mainchar.aliases[0]}. \nHealth: {mainchar.lives}. Stats: STR {mainchar.stats[0]}, AGI {mainchar.stats[1]}, INT {mainchar.stats[2]}, CHA {mainchar.stats[3]}. Level {mainchar.level} hero. Exp: {mainchar.exp}/{mainchar.expcap}. Wielding {mainchar.weapon[3]} {mainchar.weapon[0]} ({mainchar.weapon[2] + mainchar.weapon[5]} ATK). There's {mainchar.gold} gold coins in {mainchar.pronouns[2]} purse.", end=" ")
    if len(mainchar.inv) != 0:
        print("Inventory:", mainchar.inv, end=".\n")
    else:
        print("Inventory is empty.")
    if mainchar.companion != "":
        print(f"Companion: {mainchar.companion[0]}. Race - {mainchar.companion[3]}. \nHealth: {mainchar.companion[2]}. Stats: STR {mainchar.companion[5][0]}, AGI {mainchar.companion[5][1]}, INT {mainchar.companion[5][2]}, CHA {mainchar.companion[5][3]}. Wielding {mainchar.companion[4][3]} {mainchar.companion[4][0]}.")
    else:
        print("")


def HealSelf():
    while True:
        if len(mainchar.inv) != 0:
            num = 1
            for i in mainchar.inv:
                print(str(num)+".", i)
                num += 1
            c = input(
                f"Enter an item's number to use it. Or \"quit\" to exit.  -> ")
            if c == "q" or c == "quit":
                break
            else:
                try:
                    c = int(c)
                    if c > len(mainchar.inv) or c < 1:
                        print("Wrong input.")
                    else:
                        if mainchar.inv[c - 1] == "health potion":
                            if mainchar.lives < 20:
                                mainchar.inv.remove("health potion")
                                mainchar.lives += 5
                                if mainchar.lives > 20:
                                    mainchar.lives = 20
                                print(mainchar.name, "used health potion to mend wounds. Health now:", mainchar.lives)
                                break
                            else:
                                print(mainchar.name, "has full health.")
                        elif mainchar.inv[c - 1] == "medicinal herb":
                            if mainchar.lives < 20:
                                mainchar.inv.remove("medicinal herb")
                                mainchar.lives += 2
                                if mainchar.lives > 20:
                                    mainchar.lives = 20
                                print(mainchar.name, "used medicinal herb to mend wounds. Health now:", mainchar.lives)
                                break
                            else:
                                print(mainchar.name, "has full health.")
                        elif mainchar.inv[c - 1] == "agility potion":
                            mainchar.inv.remove("agility potion")
                            mainchar.stats[1] += 1
                            print(mainchar.name, "drank the agility potion. Shortly after that,", mainchar.pronouns[0], "felt more agile. AGI now:", mainchar.stats[1])
                            break
                        elif mainchar.inv[c - 1] == "strength potion":
                            mainchar.inv.remove("strength potion")
                            mainchar.stats[0] += 1
                            print(mainchar.name, "drank the strength potion. Shortly after that,", mainchar.pronouns[0], "felt stronger. STR now:", mainchar.stats[0])
                            break
                        elif mainchar.inv[c - 1] == "intellect potion":
                            mainchar.inv.remove("intellect potion")
                            mainchar.stats[2] += 1
                            print(mainchar.name, "drank the intellect potion. Shortly after that,", mainchar.pronouns[0], "felt smarter. INT now:", mainchar.stats[2])
                            break
                        elif mainchar.inv[c - 1] == "charisma potion":
                            mainchar.inv.remove("charisma potion")
                            mainchar.stats[3] += 1
                            print(mainchar.name, "drank the charisma potion. Shortly after that,", mainchar.pronouns[0], "felt more eloquent. CHA now:", mainchar.stats[3])
                            break
                        elif mainchar.inv[c - 1] == "experience potion":
                            mainchar.inv.remove("experience potion")
                            mainchar.exp += 25
                            print(mainchar.name, "drank the experience potion. Shortly after that,", mainchar.pronouns[0], "felt more experienced.")
                            checkLevel(mainchar)
                            break
                        else:
                            print("It has no use in the dungeon.")
                        break
                except ValueError:
                    print("Input error.")
        else:
            print("There's nothing in the inventory.")
            break


def HealComp():
    while True:
        if len(mainchar.inv) != 0:
            num = 1
            for i in mainchar.inv:
                print(str(num)+".", i)
                num += 1
            c = input(
                f"Enter an item's number to use it. Or \"quit\" to exit.  -> ")
            if c == "q" or c == "quit":
                break
            else:
                try:
                    c = int(c)
                    if c > len(mainchar.inv) or c < 1:
                        print("Wrong input.")
                    else:
                        if mainchar.inv[c - 1] == "health potion":
                            if mainchar.companion[2] < 20:
                                mainchar.inv.remove("health potion")
                                mainchar.companion[2] += 5
                                if mainchar.companion[2] > 20:
                                    mainchar.companion[2] = 20
                                print(f"{mainchar.name} used health potion to mend {mainchar.companion[0]}'s wounds. Health now: {mainchar.companion[2]}")
                                break
                            else:
                                print(mainchar.companion[0], "has full health.")
                        elif mainchar.inv[c - 1] == "medicinal herb":
                            if mainchar.companion[2] < 20:
                                mainchar.inv.remove("medicinal herb")
                                mainchar.companion[2] += 2
                                if mainchar.companion[2] > 20:
                                    mainchar.companion[2] = 20
                                print(f"{mainchar.name} used medicinal herb to mend {mainchar.companion[0]}'s wounds. Health now: {mainchar.companion[2]}")
                                break
                            else:
                                print(mainchar.companion[0], "has full health.")
                        elif mainchar.inv[c - 1] == "agility potion":
                            mainchar.inv.remove("agility potion")
                            mainchar.companion[5][1] += 1
                            print(f"{mainchar.name} gave the agility potion to {mainchar.companion[0]}. After drinking that, {mainchar.companion[0]} felt agile. INT now: {mainchar.companion[5][1]}")
                            break
                        elif mainchar.inv[c - 1] == "strength potion":
                            mainchar.inv.remove("strength potion")
                            mainchar.companion[5][0] += 1
                            print(f"{mainchar.name} gave the strength potion to {mainchar.companion[0]}. After drinking that, {mainchar.companion[0]} felt stronger. INT now: {mainchar.companion[5][0]}")
                            break
                        elif mainchar.inv[c - 1] == "intellect potion":
                            mainchar.inv.remove("intellect potion")
                            mainchar.companion[5][2] += 1
                            print(f"{mainchar.name} gave the intellect potion to {mainchar.companion[0]}. After drinking that, {mainchar.companion[0]} felt smarter. INT now: {mainchar.companion[5][2]}")
                            break
                        elif mainchar.inv[c - 1] == "charisma potion":
                            mainchar.inv.remove("charisma potion")
                            mainchar.companion[5][3] += 1
                            print(f"{mainchar.name} gave the charisma potion to {mainchar.companion[0]}. After drinking that, {mainchar.companion[0]} felt eloquent. INT now: {mainchar.companion[5][3]}")
                            break
                        elif mainchar.inv[c - 1] == "experience potion":
                            print(f"{mainchar.companion[0]}'s beliefs won't allow them to drink that.")
                        else:
                            print("It has no use in the dungeon.")
                        break
                except ValueError:
                    print("Input error.")
        else:
            print("There's nothing in the inventory.")
            break


def prologue(mainchar, playdict):
    prologues = open("storygen/prologues.txt", 'r').read()
    prologues = prologues.split("\n\n")
    story = ""
    iteration = 0
    storyline = ''
    for i in prologues:
        if iteration == 3 or iteration == 7:
            for j in i.split('\n'):
                occ = j.split("|")
                if mainchar.occupation == occ[0]:
                    storyline = random.choice(occ[1::])
        elif iteration == 4 or iteration == 6:
            for j in i.split('\n'):
                reas = j.split("|")
                if mainchar.reason == reas[0]:
                    storyline = random.choice(reas[1::])
        else:
            storyline = random.choice(i.split("\n"))
        storyline = replacing(storyline)
        story = story + storyline + " "
        iteration += 1
    story = story + "\n"
    print(story)


def sentences(mainchar, playdict):
    sentences = open("storygen/sentences.txt", 'r').read()
    sentences = sentences.split("\n\n")
    result = "w"
    if mainchar.lives >= 20:
        column = sentences[0].split("\n")
        story = random.choice(column)
    elif 20 > mainchar.lives >= 12:
        column = sentences[1].split("\n")
        story = random.choice(column)
    elif 12 > mainchar.lives >= 1:
        column = sentences[2].split("\n")
        story = random.choice(column)
    else:
        return
    print(replacing(story), end="")
    cont = input()
    roll = random.randint(1, 20)
    if roll <= 10:
        result = evFighting(mainchar, playdict)
        mainchar.exp += random.randint(10, 40)
    elif 10 < roll <= 15:
        evMeeting(mainchar, playdict)
        mainchar.exp += random.randint(2, 7)
    elif 15 < roll <= 18:
        column = sentences[11].split("\n")
        story = random.choice(column)
        print(replacing(story), end="")
        cont = input()
        evWeapon()
        mainchar.exp += random.randint(5, 10)
    else:
        evChest()
        mainchar.exp += random.randint(3, 8)
    if mainchar.lives > 0 and result == "w":
        checkLevel(mainchar)
        Safeinput()
    print("\n", end="")


def replacing(storyline):
    storyline = storyline.replace("[char]", mainchar.name)
    storyline = storyline.replace("[charp]", mainchar.pronouns[0])
    storyline = storyline.replace("[charpr]", mainchar.pronouns[1])
    storyline = storyline.replace("[charpp]", mainchar.pronouns[2])
    storyline = storyline.replace("[chara1]", mainchar.aliases[0])
    storyline = storyline.replace("[chara2]", mainchar.aliases[1])
    storyline = storyline.replace("[chart1]", mainchar.traits[0])
    storyline = storyline.replace("[chart2]", mainchar.traits[1])
    storyline = storyline.replace("[charg]", mainchar.gender)
    storyline = storyline.replace("[chart]", mainchar.birthplace[2])
    storyline = storyline.replace("[chartt]", mainchar.birthplace[1])
    storyline = storyline.replace("[charttt]", mainchar.birthplace[0])
    storyline = storyline.replace("[charo]", mainchar.occupation)
    storyline = storyline.replace("[charn]", mainchar.nemesis)
    storyline = storyline.replace("[dun]", playdict["dun"])
    storyline = storyline.replace("[nemr]", mainchar.nemesis)
    storyline = storyline.replace("[charw]", mainchar.weapon[4] + " " + mainchar.weapon[3] + " " + mainchar.weapon[0])
    storyline = storyline.replace("[charwo]", mainchar.weapon[3] + " " + mainchar.weapon[0])
    storyline = storyline.replace("[charws]", mainchar.weapon[0])
    storyline = storyline.replace("[charc]", str(mainchar.gold))
    storyline = storyline.replace("[fur]", random.choice(playdict["obj"][0].split(",")))
    storyline = storyline.replace("[furs]", random.choice(playdict["obj"][1].split(",")))
    storyline = storyline.replace("[obj]", random.choice(playdict["obj"][2].split(",")))
    storyline = storyline.replace("[objs]", random.choice(playdict["obj"][3].split(",")))
    storyline = storyline.replace("[bod]", random.choice(playdict["obj"][4].split(",")))
    storyline = storyline.replace("[fura]", random.choice(playdict["inanimagj"][0].split(",")))
    storyline = storyline.replace("[rooma]", random.choice(playdict["inanimagj"][1].split(",")))
    storyline = storyline.replace("[doora]", random.choice(playdict["inanimagj"][2].split(",")))
    storyline = storyline.replace("[obja]", random.choice(playdict["inanimagj"][3].split(",")))
    storyline = storyline.replace("[smil]", random.choice(playdict["animv"][1].split(",")))
    storyline = storyline.replace("[smiled]", random.choice(playdict["animv"][2].split(",")))
    storyline = storyline.replace("[name]", random.choice(playdict["animv"][0].split(",")))
    storyline = storyline.replace("[num]", str(random.randint(2, 7)))
    if mainchar.companion != "":
        storyline = storyline.replace("[char1comp]", mainchar.companion[0])
    newstor = ""
    dot = True
    for j in storyline:
        if j == ".":
            dot = True
        if dot is True and j != " " and j != ".":
            newstor = newstor + j.upper()
            dot = False
        else:
            newstor = newstor + j
    storyline = newstor
    return storyline


def replacingcreat(story, creature):   # replacing tags containing creatures or other characters
    story = story.replace("[creat]", creature[0])
    story = story.replace("[creatp]", creature[1])
    story = story.replace("[creatpr]", creature[2])
    story = story.replace("[creatpp]", creature[3])
    story = story.replace("[creatr]", creature[4])
    return story


def replacingcom(story, creature):   # replacing tags containing creatures or other characters
    story = story.replace("[com]", creature.name)
    story = story.replace("[comp]", creature.pronouns[0])
    story = story.replace("[compr]", creature.pronouns[1])
    story = story.replace("[compp]", creature.pronouns[2])
    story = story.replace("[comr]", creature.race)
    story = story.replace("[comw]", creature.weapon[0])
    return story


def evFighting(mainchar, playdict):    # fighting event
    creatures = playdict["creatures"]
    creatures = creatures[0].split("\n")
    creatures = random.choice(creatures)
    sentences = open("storygen/sentences.txt", 'r').read()
    sentences = sentences.split("\n\n")
    fighting = open("eventgen/fighting.txt", 'r').read()
    fighting = fighting.split("\n\n")
    creatstats = []
    if creatures.split("|")[2] == "d":
        creatstats = [random.randint(3, 6), random.randint(1, 5), random.randint(1, 4), random.randint(2, 6)]
    else:
        j = creatures.split("|")[2].split(",")
        for i in j:
            creatstats.append(int(i))
    creaturelives = creatstats[0] * 2 + 1
    creature = [creatures.split("|")[0], "it", "them", "their", creatures.split("|")[0]]
    print(replacing(replacingcreat(random.choice(sentences[12].split("\n")), creature)), end="")
    cont = input()
    if creatures.split("|")[1] == "h":
        print(replacing(replacingcreat(random.choice(sentences[13].split("\n")), creature)), end="")
        cont = input()
    a = Enemyinput(creaturelives, creatstats, creatures, 0)
    while True:
        if a == "f":
            while True:
                if mainchar.companion != "":
                    comp = Meeting()
                    comp.name = mainchar.companion[0]
                    if mainchar.companion[1] == "m":
                        comp.pronouns = ["he", "him", "his"]
                    elif mainchar.companion[1] == "f":
                        comp.pronouns = ["she", "her", "her"]
                    else:
                        comp.pronouns = ["they", "them", "their"]
                    comp.race = mainchar.companion[3]
                    comp.weapon = mainchar.companion[4][0]
                    while mainchar.lives > 0:
                        if creaturelives > 0:
                            if int(mainchar.companion[2]) > 0:
                                if mainchar.stats[1] + random.randint(1, 6) >= creatstats[1] + random.randint(1, 6):
                                    creaturelives = creaturelives - math.ceil(mainchar.stats[0]/2) - mainchar.weapon[2] - mainchar.weapon[5]
                                    if mainchar.weapon[1] == "o":
                                        print(replacing(replacingcreat(random.choice(fighting[1].split("\n")), creature)), creature[0], "hp:", creaturelives)
                                    else:
                                        print(replacing(replacingcreat(random.choice(fighting[0].split("\n")), creature)), creature[0], "hp:", creaturelives)
                                else:
                                    if mainchar.weapon[1] == "o":
                                        print(replacing(replacingcreat(random.choice(fighting[3].split("\n")), creature)), creature[0], "hp:", creaturelives)
                                    else:
                                        print(replacing(replacingcreat(random.choice(fighting[2].split("\n")), creature)))
                                if int(mainchar.companion[5][1]) + random.randint(1, 6) >= creatstats[1] + random.randint(1, 6):
                                    creaturelives = creaturelives - math.ceil(int(mainchar.companion[5][0])/2) - int(mainchar.companion[4][2]) - int(mainchar.companion[4][5])
                                    if mainchar.companion[4][1] == "o":
                                        print(replacing(replacingcom(replacingcreat(random.choice(fighting[9].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                                    else:
                                        print(replacing(replacingcom(replacingcreat(random.choice(fighting[8].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                                else:
                                    if mainchar.weapon[1] == "o":
                                        print(replacing(replacingcom(replacingcreat(random.choice(fighting[11].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                                    else:
                                        print(replacing(replacingcom(replacingcreat(random.choice(fighting[10].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                            else:
                                print(replacing(replacingcom(replacingcreat(random.choice(fighting[12].split("\n")), creature), comp)))
                                mainchar.companion = ""
                                break
                            if creaturelives > 0:
                                targ = random.randint(1, 2)
                                if targ == 1:
                                    if mainchar.stats[1] + random.randint(1, 6) < creatstats[1] + random.randint(1, 6):
                                        mainchar.lives = mainchar.lives - math.ceil(creatstats[0]/2) - random.randint(-1, 4)
                                        print(replacing(replacingcreat(random.choice(fighting[4].split("\n")), creature)), mainchar.name, "hp:", mainchar.lives)
                                    else:
                                        print(replacing(replacingcreat(random.choice(fighting[5].split("\n")), creature)), mainchar.name, "hp:", mainchar.lives)
                                if targ == 2:
                                    if int(mainchar.companion[5][1]) + random.randint(-1, 1) < creatstats[1] + random.randint(-1, 1):
                                        mainchar.companion[2] = int(mainchar.companion[2]) - math.ceil(creatstats[0]/2) - random.randint(-1, 4)
                                        print(replacing(replacingcom(replacingcreat(random.choice(fighting[6].split("\n")), creature), comp)), "hp:", mainchar.companion[2])
                                    else:
                                        print(replacing(replacingcom(replacingcreat(random.choice(fighting[7].split("\n")), creature), comp)), "hp:", mainchar.companion[2])
                                if mainchar.lives <= 0:
                                    print(replacing(replacingcreat(random.choice(fighting[13].split("\n")), creature)))
                                    cont = input()
                                    return "l"
                        else:
                            print(replacing(replacingcreat(random.choice(fighting[14].split("\n")), creature)))
                            cont = input()
                            break
                        y = Enemyinput(creaturelives, creatstats, creatures, 1)
                        if y == "r":
                            return "l"
                    break
                else:
                    while mainchar.lives > 0:
                        if creaturelives > 0:
                            if mainchar.stats[1] + random.randint(1, 6) >= creatstats[1] + random.randint(1, 6):
                                creaturelives = creaturelives - math.ceil(mainchar.stats[0]/2) - mainchar.weapon[2] - mainchar.weapon[5]
                                if mainchar.weapon[1] == "o":
                                    print(replacing(replacingcreat(random.choice(fighting[1].split("\n")), creature)), creature[0], "hp:",
                                          creaturelives)
                                else:
                                    print(replacing(replacingcreat(random.choice(fighting[0].split("\n")), creature)), creature[0], "hp:",
                                          creaturelives)
                            else:
                                if mainchar.weapon[1] == "o":
                                    print(replacing(replacingcreat(random.choice(fighting[3].split("\n")), creature)), creature[0], "hp:",
                                          creaturelives)
                                else:
                                    print(replacing(replacingcreat(random.choice(fighting[2].split("\n")), creature)), creature[0], "hp:",
                                          creaturelives)
                            if creaturelives > 0:
                                if mainchar.stats[1] + random.randint(1, 6) < creatstats[1] + random.randint(1, 6):
                                    mainchar.lives = mainchar.lives - math.ceil(creatstats[0]/2) - random.randint(-1, 4)
                                    print(replacing(replacingcreat(random.choice(fighting[4].split("\n")), creature)), mainchar.name, "hp:",
                                          mainchar.lives)
                                else:
                                    print(replacing(replacingcreat(random.choice(fighting[5].split("\n")), creature)))
                                if mainchar.lives <= 0:
                                    print(replacing(replacingcreat(random.choice(fighting[13].split("\n")), creature)))
                                    return "l"
                        else:
                            print(replacing(replacingcreat(random.choice(fighting[14].split("\n")), creature)))
                            break
                        y = Enemyinput(creaturelives, creatstats, creatures, 1)
                        if y == "r":
                            return "l"
                    break
            break
        elif a == "p":
            print(replacing(replacingcreat(random.choice(sentences[14].split("\n")), creature)))
            break
        else:
            print(replacing(replacingcreat(random.choice(sentences[16].split("\n")), creature)))
            return "l"
    if random.randint(1, 20) > 15:
        mainchar.inv.append("health potion")
        print("Found a health potion", end="")
        cont = input()
    if random.randint(1, 20) > 14:
        gold = random.randint(2, 15)
        mainchar.gold += gold
        print("Found", gold, "gold pieces in this room", end="")
        cont = input()
    return "w"


def evMeeting(mainchar, playdict):
    creatures = playdict["creatures"]
    creatures = creatures[1].split("\n")
    creatures = random.choice(creatures)
    creature = Meeting()
    creature.gender = random.choice(["m", "f", "n"])
    creature.race = creatures.split("|")[0]
    creature.stats = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    creature.weapon = pickWeapon(random.randint(2, 3))
    if creature.gender == "m":
        nam = playdict["charnames"][0].split("\n")
        creature.pronouns = ["he", "him", "his"]
        for i in nam:
            if i.split(":")[0] == creatures.split("|")[0]:
                nam = i.split(":")[1].split("|")[0]
                break
        creature.name = random.choice(nam.split(","))
        nam = playdict["charnames"][1].split("\n")
        for i in nam:
            if i.split(":")[0] == creatures.split("|")[0]:
                nam = i.split(":")[1]
                nam = random.choice(nam.split(","))
                creature.name = creature.name + " " + nam
                break
    elif creature.gender == "f":
        nam = playdict["charnames"][0].split("\n")
        creature.pronouns = ["she", "her", "her"]
        for i in nam:
            if i.split(":")[0] == creatures.split("|")[0]:
                nam = i.split(":")[1].split("|")[1]
                break
        creature.name = random.choice(nam.split(","))
        nam = playdict["charnames"][1].split("\n")
        for i in nam:
            if i.split(":")[0] == creatures.split("|")[0]:
                nam = i.split(":")[1]
                nam = random.choice(nam.split(","))
                creature.name = creature.name + " " + nam
                break
    elif creature.gender == "n":
        nam = playdict["charnames"][0].split("\n")
        creature.pronouns = ["they", "them", "their"]
        for i in nam:
            if i.split(":")[0] == creatures.split("|")[0]:
                nam = i.split(":")[1].split("|")[random.randint(0,1)]
                break
        creature.name = random.choice(nam.split(","))
        nam = playdict["charnames"][1].split("\n")
        for i in nam:
            if i.split(":")[0] == creatures.split("|")[0]:
                nam = i.split(":")[1]
                nam = random.choice(nam.split(","))
                creature.name = creature.name + " " + nam
                break
    relation = random.choice(creatures.split("|")[1].split(","))
    sentences = open("storygen/sentences.txt", 'r').read()
    sentences = sentences.split("\n\n")
    print(replacing(replacingcom(random.choice(sentences[3].split("\n")), creature)), end="")
    story = ""
    cont = input()
    if relation == "c":       # could be a companion
        if mainchar.companion == "":
            print("It was also an adventurer, so our hero thought about joining forces. ")
            if creature.stats[3] + random.randint(1, 6) > mainchar.stats[3] + random.randint(1, 6):
                print(replacing(replacingcom(random.choice(sentences[4].split("\n")), creature)))
            else:
                print(replacing(replacingcom(random.choice(sentences[5].split("\n")), creature)))
                mainchar.companion = [creature.name, creature.gender, int(creature.lives), creature.race, creature.weapon, creature.stats]
        else:
            print(f"It was also an adventurer, but {mainchar.name} already had someone with {mainchar.pronouns[1]}. So they just went about their business. ")
    elif relation == "a":
        print(replacing(replacingcom(random.choice(sentences[6].split("\n")), creature)))  # random person
    else:
        print(replacing(replacingcom(random.choice(sentences[7].split("\n")), creature)))  # merchant
        bought = False
        wares = []
        for i in range(random.randint(3, 8)):
            wares.append(random.choice(["health potion", "medicinal herb", "agility potion", "strength potion", "intellect potion", "charisma potion", "experience potion"]))
        ranweap = pickWeapon(random.randint(2,3))
        wares.append(f"{ranweap[3]} {ranweap[0]}")
        while True:
            if len(wares) > 0:
                print("Merchant has this in store:")
                while True:
                    num = 1
                    for i in wares:
                        print(str(num) + ".", i, end=" ")
                        if i == "health potion":
                            print("- 15 g.")
                        elif i == "medicinal herb":
                            print("- 5 g.")
                        elif i == "agility potion":
                            print("- 35 g.")
                        elif i == "strength potion":
                            print("- 25 g.")
                        elif i == "intellect potion":
                            print("- 20 g.")
                        elif i == "charisma potion":
                            print("- 30 g.")
                        elif i == "experience potion":
                            print("- 40 g.")
                        elif i == f"{ranweap[3]} {ranweap[0]}":
                            print(f"({mainchar.weapon[2] + mainchar.weapon[5]} ATK) - {ranweap[6]} g.")
                        num += 1
                    c = input(f"Character has {mainchar.gold} gold. Enter an item's number to purchase it. Or \"quit\" to exit.  -> ")
                    if c == "q" or c == "quit":
                        break
                    else:
                        try:
                            while True:
                                if len(wares) < 1:
                                    print("Merchant is all out of wares.")
                                    break
                                c = int(c)
                                if c > len(wares) or c < 1:
                                    print("Wrong input.")
                                    break
                                else:
                                    if wares[c-1] == "health potion":
                                        if mainchar.gold >= 15:
                                            mainchar.inv.append("health potion")
                                            wares.remove("health potion")
                                            mainchar.gold -= 15
                                            print(mainchar.name, "purchased health potion.")
                                            bought = True
                                            break
                                        else:
                                            print("Not enough money.")
                                            break
                                    if wares[c-1] == "medicinal herb":
                                        if mainchar.gold >= 5:
                                            mainchar.inv.append("medicinal herb")
                                            wares.remove("medicinal herb")
                                            mainchar.gold -= 5
                                            print(mainchar.name, "purchased medicinal herb.")
                                            bought = True
                                            break
                                        else:
                                            print("Not enough money.")
                                            break
                                    if wares[c-1] == "agility potion":
                                        if mainchar.gold >= 35:
                                            mainchar.inv.append("agility potion")
                                            wares.remove("agility potion")
                                            mainchar.gold -= 35
                                            print(mainchar.name, "purchased agility potion.")
                                            bought = True
                                            break
                                        else:
                                            print("Not enough money.")
                                            break
                                    if wares[c-1] == "strength potion":
                                        if mainchar.gold >= 25:
                                            mainchar.inv.append("strength potion")
                                            wares.remove("strength potion")
                                            mainchar.gold -= 25
                                            print(mainchar.name, "purchased strength potion.")
                                            bought = True
                                            break
                                        else:
                                            print("Not enough money.")
                                            break
                                    if wares[c-1] == "intellect potion":
                                        if mainchar.gold >= 30:
                                            mainchar.inv.append("intellect potion")
                                            wares.remove("intellect potion")
                                            mainchar.gold -= 30
                                            print(mainchar.name, "purchased intellect potion.")
                                            bought = True
                                            break
                                        else:
                                            print("Not enough money.")
                                            break
                                    if wares[c-1] == "charisma potion":
                                        if mainchar.gold >= 30:
                                            mainchar.inv.append("charisma potion")
                                            wares.remove("charisma potion")
                                            mainchar.gold -= 30
                                            print(mainchar.name, "purchased charisma potion.")
                                            bought = True
                                            break
                                        else:
                                            print("Not enough money.")
                                            break
                                    if wares[c-1] == f"{ranweap[3]} {ranweap[0]}":
                                        if mainchar.gold >= ranweap[6]:
                                            mainchar.gold -= ranweap[6]
                                            wares.remove(f"{ranweap[3]} {ranweap[0]}")
                                            mainchar.weapon = ranweap
                                            print(f"{mainchar.name} traded {ranweap[4]} {ranweap[3]} {ranweap[0]} for {ranweap[6]} gold and {mainchar.pronouns[2]} old weapon.")
                                            bought = True
                                            break
                                        else:
                                            print("Not enough money.")
                                            break
                        except ValueError:
                            print("Input error.")
            else:
                break
            if bought:
                print(replacing(replacingcom(random.choice(sentences[9].split("\n")), creature)))
                print(f" At the time {mainchar.name}'s inventory contained:", end="")
                inventory = ""
                for i in mainchar.inv:
                    inventory += " " + i + ","
                inventory = inventory[:-1] + "."
                print(inventory)
                break
            else:
                print(replacing(replacingcom(random.choice(sentences[8].split("\n")), creature)))
                break
    print(story)


def evWeapon():
    gold = random.randint(10, 25)
    tier = random.randint(2, 4)
    newweap = pickWeapon(tier)
    if newweap[2] + newweap[5] >= mainchar.weapon[2] + mainchar.weapon[5]:
        print(mainchar.name, "found", newweap[4], newweap[3], newweap[0], "and it's better than", mainchar.pronouns[2],
              mainchar.weapon[0], "so", mainchar.pronouns[0], "decided to take it instead.", end=" ")
        mainchar.weapon = newweap
        cont = input()
        print("Wielding", mainchar.pronouns[2], "new", mainchar.weapon[0], mainchar.name,
              "went further on into the dungeon.", end="")
    else:
        print(mainchar.name, "found", newweap[4], newweap[3], newweap[0], "and it's worse than", mainchar.pronouns[2],
              "own weapon.", mainchar.pronouns[0].capitalize(), "decided to leave it there.", end=" ")
        cont = input()
        print("Wielding", mainchar.pronouns[2], mainchar.weapon[3], mainchar.weapon[0], mainchar.name,
              "went further on into the dungeon.", end="")
    mainchar.gold += gold
    cont = input()


def evChest():
    sentences = open("storygen/sentences.txt", 'r').read()
    sentences = sentences.split("\n\n")
    column = sentences[10].split("\n")
    story = random.choice(column)
    print(replacing(story), end="")
    gold = random.randint(50, 125)
    cont = input()
    print("Inside was", gold, "gold pieces.", end=" ")
    mainchar.gold += gold
    print("Now", mainchar.pronouns[0], "has exactly", mainchar.gold, "gold coins.", end="")
    cont = input()


def BossFight(mainchar, playdict):
    bossfighttext = open("eventgen/bossfight.txt", 'r').read()
    bossfighttext = bossfighttext.split("\n\n")
    fighting = open("eventgen/fighting.txt", 'r').read()
    fighting = fighting.split("\n\n")
    bossrace = random.choice(bossfighttext[0].split("\n"))
    creature = [mainchar.nemesis, "it", "them", "their", bossrace.split("|")[0]]
    creatstats = bossrace.split("|")[1].split(",")
    creaturelives = (int(creatstats[0]) + 1) * 3 + 5
    iteration = 0
    bossappears = [""]
    bossattack = [""]
    bossmiss = [""]
    bosstalk = [""]
    bossdeath = [""]
    bosschardied = [""]
    bossreason = [""]
    for j in bossfighttext:
        if iteration == 0:
            bosstype = j.split("\n")
            for i in bosstype:
                if bossrace.split("|")[0] == i.split("|")[0]:
                    bossappears = i.split("|")[2::]
        elif iteration == 1:
            bosstype = j.split("\n")
            for i in bosstype:
                if bossrace.split("|")[0] == i.split("|")[0]:
                    bossattack = i.split("|")[1::]
        elif iteration == 2:
            bosstype = j.split("\n")
            for i in bosstype:
                if bossrace.split("|")[0] == i.split("|")[0]:
                    bossmiss = i.split("|")[1::]
        elif iteration == 3:
            bosstype = j.split("\n")
            for i in bosstype:
                if bossrace.split("|")[0] == i.split("|")[0]:
                    bosstalk = i.split("|")[1::]
        elif iteration == 4:
            bosstype = j.split("\n")
            for i in bosstype:
                if bossrace.split("|")[0] == i.split("|")[0]:
                    bossdeath = i.split("|")[1::]
        elif iteration == 5:
            bosstype = j.split("\n")
            for i in bosstype:
                if bossrace.split("|")[0] == i.split("|")[0]:
                    bosschardied = i.split("|")[1::]
        elif iteration == 6:
            bosstype = j.split("\n")
            for i in bosstype:
                if mainchar.reason == i.split("|")[0]:
                    bossreason = i.split("|")[1::]
        iteration += 1
    print(replacing(replacingcreat(random.choice(bossappears), creature)), end="")
    cont = input()
    print(replacing(replacingcreat(random.choice(bossreason), creature)), end="")
    cont = input()
    print(f"\n{creature[0]} \nHealth: {creaturelives}. Stats: STR {creatstats[0]}, AGI {creatstats[1]}, INT {creatstats[2]}, CHA {creatstats[3]}.", end="")
    cont = input()
    while True:
        if mainchar.companion != "":
            comp = Meeting()
            comp.name = mainchar.companion[0]
            if mainchar.companion[1] == "m":
                comp.pronouns = ["he", "him", "his"]
            else:
                comp.pronouns = ["she", "her", "he"]
            comp.race = mainchar.companion[3]
            comp.weapon = mainchar.companion[4][0]
            while mainchar.lives > 0:
                if mainchar.lives < 20:
                    if "health potion" in mainchar.inv:
                        if random.randint(1, 20) + mainchar.stats[2] > 15:
                            if random.randint(1, 20) + mainchar.stats[1] > 15:
                                mainchar.lives += 5
                                if mainchar.lives > 20:
                                    mainchar.lives = 20
                                print(f"{mainchar.name} used the {creature[4]}'s slowness to try to chug down healing potion. Health now: {mainchar.lives}.")
                            else:
                                print(f"{mainchar.name} tried using healing potion, but couldn't!")
                            cont = input()
                if creaturelives > 0:
                    if int(mainchar.companion[2]) > 0:
                        if mainchar.stats[1] + random.randint(1, 6) >= int(creatstats[1]) + random.randint(1, 6):
                            creaturelives = creaturelives - math.ceil(mainchar.stats[0] / 2) - mainchar.weapon[2] - mainchar.weapon[5]
                            if mainchar.weapon[1] == "o":
                                print(replacing(replacingcreat(random.choice(fighting[1].split("\n")), creature)), creature[0], "hp:", creaturelives)
                            else:
                                print(replacing(replacingcreat(random.choice(fighting[0].split("\n")), creature)), creature[0], "hp:", creaturelives)
                            cont = input()
                        else:
                            if mainchar.weapon[1] == "o":
                                print(replacing(replacingcreat(random.choice(fighting[3].split("\n")), creature)), creature[0], "hp:", creaturelives)
                            else:
                                print(replacing(replacingcreat(random.choice(fighting[2].split("\n")), creature)))
                            cont = input()
                            if int(mainchar.companion[5][1]) + random.randint(1, 6) >= int(creatstats[1]) + random.randint(1, 6):
                                creaturelives = creaturelives - math.ceil(int(mainchar.companion[5][0]) / 2) - int(mainchar.companion[4][2]) - int(mainchar.companion[4][5])
                                if mainchar.companion[4][1] == "o":
                                    print(replacing(replacingcom(replacingcreat(random.choice(fighting[9].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                                else:
                                    print(replacing(replacingcom(replacingcreat(random.choice(fighting[8].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                            else:
                                if mainchar.weapon[1] == "o":
                                    print(replacing(replacingcom(replacingcreat(random.choice(fighting[11].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                                else:
                                    print(replacing(replacingcom(replacingcreat(random.choice(fighting[10].split("\n")), creature), comp)), creature[0], "hp:", creaturelives)
                            cont = input()
                    else:
                        print(replacing(replacingcom(replacingcreat(random.choice(fighting[12].split("\n")), creature), comp)))
                        mainchar.companion = ""
                        mainchar.companiondied = True
                        break
                    cont = input()
                    if creaturelives > 0:
                        if random.randint(1, 20) > 15:
                            print(replacing(replacingcreat(random.choice(bosstalk), creature)))

                        targ = random.randint(1, 2)
                        if targ == 1:
                            if mainchar.stats[1] + random.randint(1, 6) < int(creatstats[1]) + random.randint(1, 6):
                                mainchar.lives = mainchar.lives - math.ceil(int(creatstats[0]) / 2) - random.randint(-1, 4)
                                print(replacing(replacingcreat(random.choice(bossattack), creature)), mainchar.name, "hp:", mainchar.lives)
                            else:
                                print(replacing(replacingcreat(random.choice(bossmiss), creature)), mainchar.name, "hp:", mainchar.lives)
                            cont = input()
                        if targ == 2:
                            if int(mainchar.companion[5][1]) + random.randint(-1, 1) < int(creatstats[1]) + random.randint(-1, 1):
                                mainchar.companion[2] = int(mainchar.companion[2]) - math.ceil(int(creatstats[0]) / 2) - random.randint(-1, 4)
                                print(replacing(replacingcom(replacingcreat(random.choice(fighting[6].split("\n")), creature), comp)), "hp:", mainchar.companion[2])
                            else:
                                print(replacing(replacingcom(replacingcreat(random.choice(fighting[7].split("\n")), creature), comp)), "hp:", mainchar.companion[2])
                            cont = input()
                        if mainchar.lives <= 0:
                            print(replacing(replacingcreat(random.choice(bosschardied), creature)))
                            cont = input()
                            return "d"
                else:
                    print(replacing(replacingcreat(random.choice(bossdeath), creature)), end="")
                    cont = input()
                    return "w"
            break
        else:
            while mainchar.lives > 0:
                if creaturelives > 0:
                    if mainchar.stats[1] + random.randint(1, 6) >= int(creatstats[1]) + random.randint(1, 6):
                        creaturelives = creaturelives - math.ceil(mainchar.stats[0] / 2) - mainchar.weapon[2] - mainchar.weapon[5]
                        if mainchar.weapon[1] == "o":
                            print(replacing(replacingcreat(random.choice(fighting[1].split("\n")), creature)),
                                  creature[0], "hp:",
                                  creaturelives)
                        else:
                            print(replacing(replacingcreat(random.choice(fighting[0].split("\n")), creature)),
                                  creature[0], "hp:",
                                  creaturelives)
                        cont = input()
                    else:
                        if mainchar.weapon[1] == "o":
                            print(replacing(replacingcreat(random.choice(fighting[3].split("\n")), creature)),
                                  creature[0], "hp:",
                                  creaturelives)
                        else:
                            print(replacing(replacingcreat(random.choice(fighting[2].split("\n")), creature)),
                                  creature[0], "hp:",
                                  creaturelives)
                        cont = input()
                    if creaturelives > 0:
                        if random.randint(1, 20) > 15:
                            print(replacing(replacingcreat(random.choice(bosstalk), creature)))
                        if mainchar.stats[1] + random.randint(1, 6) < int(creatstats[1]) + random.randint(1, 6):
                            mainchar.lives = mainchar.lives - math.ceil(int(creatstats[0]) / 2) - random.randint(-1, 4)
                            print(replacing(replacingcreat(random.choice(bossattack), creature)),
                                  mainchar.name, "hp:",
                                  mainchar.lives)
                        else:
                            print(replacing(replacingcreat(random.choice(bossmiss), creature)))
                        if mainchar.lives <= 0:
                            print(replacing(replacingcreat(random.choice(bosschardied), creature)))
                            return "d"
                    cont = input()
                else:
                    print(replacing(replacingcreat(random.choice(bossdeath), creature)), end="")
                    cont = input()
                    return "w"
            break
    return "w"


def epilogue(mainchar, playdict, result):
    epilogues = open("storygen/epilogues.txt", 'r').read()
    epilogues = epilogues.split("\n\n")
    cont = input()
    if result == "w" and not mainchar.companiondied:
        print(replacing(random.choice(epilogues[0].split("\n"))), end="")
    elif result == "w" and mainchar.companion != "":
        print(replacing(random.choice(epilogues[1].split("\n"))), end="")
    elif result == "l":
        print(replacing(random.choice(epilogues[4].split("\n"))), end="")
    elif result == "d" and mainchar.companiondied:
        print(replacing(random.choice(epilogues[3].split("\n"))), end="")
    elif result == "d" and not mainchar.companiondied:
        print(replacing(random.choice(epilogues[2].split("\n"))), end="")
    cont = input()
    print(replacing(random.choice(epilogues[5].split("\n"))), end="")
    cont = input()
    print("\n\n-----------------------\nYour personal score:")
    if mainchar.lives > 0:
        Stat()
        bonus = 0
        if mainchar.companion != "":
            bonus += 50
        score = mainchar.gold + mainchar.weapon[6] + bonus + (len(mainchar.inv) * 5) + (mainchar.level * 50) + mainchar.exp
        print(f"{mainchar.name}'s gold: {mainchar.gold}. Level {mainchar.level}")
        print(f"Final score: {score}!\n-----------------------")
        file = open('highscores.txt', 'a+')
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}   {mainchar.name} {mainchar.aliases[0]} - {score}")
        file.write("\n")
        file.close()
    else:
        print("Final score: 0.\n-----------------------")


if __name__ == "__main__":
    print("Written by HidingFox. Version 1.2\n")
    playdict = importStories()
    mainchar = createChar(playdict)
    prologue(mainchar, playdict)
    f = input(f"Press Enter after each sentence while wandering in the {playdict['dun']} Dungeon. When inputing a command you can enter only the first letter.\n ")
    randomn = random.randint(8, 12)
    for i in range(randomn):
        sentences(mainchar, playdict)
    result = "l"
    if mainchar.lives > 0:
        result = BossFight(mainchar, playdict)
    epilogue(mainchar, playdict, result)
    a = input("Press any key to exit.")
