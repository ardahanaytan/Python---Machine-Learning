maaslar = [8000,5000,2000,1000,3000,7000,1000]

#dir(maaslar)

maaslar.sort()

for i in maaslar:
    if i == 3000:
        print('kesildi')
        break
    print(i)


for i in maaslar:
    if i == 3000:
        continue
    print(i)