print("Kodlama.io")


#string => metinsel ifade
head = "Taşıt Kredisi"
print(head)
head = "İhtiyaç Kredisi"
print(head)


#int, integer => tam sayı
vade = 36
ekVade = 10
vade2 = "36"


#float, decimal, double
aylikOdeme = 200.50


#bool , boolean => true veya false
yukselisteMi = False


#matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)

# - 
print(5 - 5)
print(vade - ekVade)
print(75 - vade)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)

# /
print(24 / 6)
print(vade / ekVade)
print(vade / 3)



yeniVade = vade / 2
fiyat = 110
indirimliFiyat = fiyat - yeniVade

print(yeniVade)
print(indirimliFiyat)


# % => mod operatör
print(10 % 2)
print(vade % 7)
print(vade % ekVade)


# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)

print(1 < 2)
print(4 < 3)
print(5 < 5)

print(1 <= 1)
print(1 <= 2)
print(5 <= 3)

print(153 != 124)
print(134 != 134)


# or and

# or => veya
print(1 > 2 or 5 > 2)

# and => ve
print(1 > 2 and 5 > 2)

print(1 > 2 or 4 > 3 and 3 > 2)
print(True and 3 > 2)


#karar yapıları
#if else
sayi1 = 10 
sayi2 = 24
#sayi1 sayi2'den büyükse ekrana sayi1 daha büyüktür yaz
#condition

#indent
if sayi1 > sayi2:
    print("Sayı1 sayı2'den daha büyüktür.")
elif sayi1 == sayi2:
    print("Sayı1 ve sayı2 eşittir.")
else:
    print("Sayı2 sayı1'den daha büyüktür.")    