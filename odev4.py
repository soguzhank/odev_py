adet = 0
for x in range(101, 988):
    strVal = str(x)
    if strVal[0] != strVal[1] and strVal[0] != strVal[2] and strVal[1] != strVal[2]:
        print(strVal[0]+strVal[1]+strVal[2])
        adet+=1

print("Üç basamaklı rakamları birbirinden farklı {} adet sayı listelendi".format(adet))
input()