from random import randrange
#how many coinflips should be made
datasize = 100_000_000

#last flip function
def lastFlip(run):
    if run == datasize - 1:
        dataList.append(counter)

#list to store the results
dataList = []

#first coinflip
coinflip = randrange(2)
lastflip = coinflip
counter = 1

for i in range(1, datasize):
    coinflip = randrange(2)
    if coinflip == lastflip:
        counter = counter + 1
        #check if is the last flip
        lastFlip(i)
    else:
        dataList.append(counter)
        counter = 1
        lastFlip(i)
    lastflip = coinflip

#print(dataList)
print("sum of coinflips:", "{:,}".format(sum(dataList)))

for i in range(1, max(dataList)+1):
    print(i, "in a row: ",dataList.count(i))