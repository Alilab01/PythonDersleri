oteleme = input("oteleme sayisi girin: ")
oteleme = int(oteleme)

metin = "merhaba"

for c in metin:
    print(ord(c),end="")
    print(" ",end="")

print("")

for c in metin:
    print(ord(c)+oteleme,end="")
    print(" ",end="")

print("")

for c in metin:
    print(chr(ord(c)),end="") 

print("")

for c in metin:
    print(chr(ord(c)+oteleme),end="") 
    
print("")
    
sifreliMetin = input("sifreli metin girin: ")
sifreOteleme = input("sifre geri oteleme girin: ")
sifreOteleme = int(sifreOteleme)

for c in sifreliMetin:
    print(chr(ord(c)-sifreOteleme),end="") 