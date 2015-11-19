#Once, my dad asked me to pick lotto numbers. 
#I don't remember which game it was, but the instructions were to select 
#three sets of 7 numbers between 1 and 49, each number in two-digit format. 
#This random number generator does just that.
#If you win the lottery because of this, it's purely by chance.
#... but only if you believe in coincidence. 

import random

count = 0
set1 = []
set2 = []
set3 = []

while count < 7:
    x = random.randint(1,49)
    strx = str(x)
    if len(strx) < 2:
        backstrx = strx + '0'
        strx = backstrx[1] + backstrx[0]
    set1.append(strx)
    count += 1

while count < 14:
    y = random.randint(1,49)
    stry = str(y)
    if len(stry) < 2:
        backstry = stry + '0'
        stry = backstry[1] + backstry[0]
    set2.append(stry)
    count += 1
    
while count < 21:
    z = random.randint(1,49)
    strz = str(z)
    if len(strz) < 2:
        backstrz = strz + '0'
        strz = backstrz[1] + backstrz[0]
    set3.append(strz)
    count += 1

print set1
print set2
print set3