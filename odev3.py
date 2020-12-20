girilenIfade = input("Girilen İfade : ")
arananIfade = input("Aranan İfade : ")

index = girilenIfade.index(arananIfade)
onceki = girilenIfade[index-1]
sonraki = girilenIfade[len(arananIfade) + index]

print(onceki+arananIfade+sonraki)

input()