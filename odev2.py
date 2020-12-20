
# www.alierbey.com 

# www. ile başlamalı
# 2 . arasında en az 3 karakter olmalı
# son . dan sonra en az 2 karakter olmalı

ilkNoktaIndex = 0
sonNoktaIndex = 0
wwwLength = 0

url=input("URL : ")
for index, i in enumerate(url):
    if i == ".":
        sonNoktaIndex = index
        if ilkNoktaIndex == 0:
            ilkNoktaIndex = index

for i in range(0, ilkNoktaIndex):
    if url[i] == "w":
        wwwLength +=1

if wwwLength == 3 and ilkNoktaIndex == 3 and sonNoktaIndex + 2 < len(url) and ilkNoktaIndex + 3 <= sonNoktaIndex:
    print("URL'dir")
else:
    print("URL değildir")

# if değerleri kontrolü
#print(wwwLength == 3, wwwLength)
#print(ilkNoktaIndex == 3, ilkNoktaIndex)
#print(sonNoktaIndex + 2 < len(url), sonNoktaIndex, len(url))
#print(ilkNoktaIndex +3 <= sonNoktaIndex, ilkNoktaIndex +3, sonNoktaIndex)

input()