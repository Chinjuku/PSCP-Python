"""Impostor"""
import json

def main():
    """Dict Methods"""

    name = {}
    die = {}
    survival = {}
    whoimpos = 0

    while True:
        txt = input()
        if txt == "Start":
            break
        name.update(json.loads(txt))

    while True:
        name_die = input()
        if name_die == "End":
            break
        die.update({name_die:name[name_die]})

    for i in name:
        if i not in die:
            survival.update({i:name[i]})

    for i in survival:
        if survival[i] == "Impostor":
            whoimpos += 1

    print("%d Impostor Remains" %whoimpos)
    print("***Alive***")
    for i in sorted(survival):
        print("%s : %s" %(i, survival[i]))
    print("***Dead***")
    for i in sorted(die):
        print("%s : %s" %(i, die[i]))
main()
