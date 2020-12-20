
# ali.erbey@usak.edu.tr

# 1 adet @ içermeli
# en az 1 adet . içermeli
# @ den en az 2 karakter sonra . gelmeli
# @ den önce en az 1 karakter içermeli
# . dan sonra en az 2 karakter olmalı

atAdet = 0
atIndex = 0
sonNoktaIndex = 0

email=input("Email : ")
for index, i in enumerate(email):
    if i=="@":
        atIndex = index
        atAdet+=1
    if i == ".":
        sonNoktaIndex = index
    
if atAdet == 1 and atIndex >= 1 and atIndex + 2 < sonNoktaIndex and sonNoktaIndex + 2 <= len(email) -1:
    print("EPosta adresidir")
else:
    print("EPosta adresi değildir")

# if değerleri kontrolü
#print(atAdet == 1, atAdet)
#print(atIndex > 1, atIndex)
#print(atIndex + 2 < sonNoktaIndex, atIndex +2, sonNoktaIndex)
#print(sonNoktaIndex + 2 <= len(email) -1 , sonNoktaIndex +2, len(email) -1)

input()