import os
os.system('cls')
print('Téglatest térfogata, felszíne.')
a=int(input('Kérem a téglatest egyik élének hosszát: '))
b=int(input('Kérem a téglatest másik élének hosszát: '))
c=int(input('Kérem a téglatest harmadik élének hosszát: '))
if a<=0:
    print('Csak nullánál nagyobb szám adható meg!!!')
if b<=0:
    print('Csak nullánál nagyobb szám adható meg!!!')
if c<=0:
    print('Csak nullánál nagyobb szám adható meg!!!')
else:
    terfogat=a*b*c
    felszin=(2*a*b)+(2*a*c)+(2*b*c)
    print('A téglatest térfogata: ', terfogat)
    print('A téglatest felszine: ', felszin)


   