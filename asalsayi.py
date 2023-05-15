tabanSayi = 500
tavanSayi = 999


for i in range(tabanSayi , tavanSayi):
    asalMi = True
    for j in range(2 , i):
        if i % j == 0:
            asalMi = False
            break
    if asalMi and i <= 599:
        print(i)