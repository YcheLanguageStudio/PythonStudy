strin = 'BABABABANANABABABABABANANABABABABABANANABANANANAAHH'
stri = '^' + strin + '|'
allrota = {}
firstchar =[]
for i in range(len(stri)):
    allrota[i] = stri[-i:] + stri[0:len(stri) - i]
    firstchar.append(allrota[i])
firstchar.sort()
out = ''
for i in firstchar:
    out = out + i[-1]
old = '-'
counter = 0
outstring = ''
for i in out:
    if(i != old):
        outstring = outstring + old + str(counter)
        old = i
        counter = 1
    else:
        old = i
        counter += 1

outstring = outstring + old + str(counter)
outstring = outstring[2:]
print(outstring)
