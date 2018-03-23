from random import shuffle as rs

NOVICE = ['r','r','r','r','r','r','b','b','b','b','b','b','w','w','e']
APPRENTICE = ['r','r','r','r','r','r','b','b','b','b','w','w','y','y', 'e']
EXPERT = ['r','r','r','r','b','b','b','b','w','w','y','y','g','g','e']
MASTER = ['r','r','r','r','b','b','w','w','y','y','g','g','p','p','e']

rs(NOVICE)
rs(APPRENTICE)
rs(EXPERT)
rs(MASTER)


with open("inputs1.txt", "w") as f:
    for i in range(50):
        rs(NOVICE)
        for char in NOVICE:
            f.write(char + " ")
        f.write("\n")

with open("inputs2.txt", "w") as f:
    for i in range(50):
        rs(APPRENTICE)
        for char in APPRENTICE:
            f.write(char + " ")
        f.write("\n")

with open("inputs3.txt", "w") as f:
    for i in range(30):
        rs(EXPERT)
        for char in EXPERT:
            f.write(char + " ")
        f.write("\n")

with open("inputs4.txt", "w") as f:
    for i in range(10):
        rs(MASTER)
        for char in MASTER:
            f.write(char + " ")
        f.write("\n")   
