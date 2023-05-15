


from human import Human


faiz = 1.48
vade = "36" 
krediAdi = "İhtiyaç kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade) + 12)
faiz = str(faiz)
print(type(faiz))

vade = 24 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
print(vade + 2)

vade2 = 36 #input("Lütfen istediğiniz vade sayısını giriniz: ")
print(type(vade2))
print(int(vade2) + 12)

vade = vade + 15
#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {a}".format(a = vade))

harf = 'a'
metin = "Seçili harf: {sec} ".format(sec = 'c')
print(metin)


# f-string
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")


# listeler

dizi = ["İhtiyaç Kredisi", 10 , 5.2 , 4.24232424]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0])

print(len(krediler))
krediler.append("Özel Kredi")
print(krediler)

print("Borç Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["X Kredisi", "Y Kredisi"])
print(krediler)

# for 
# i=0 i<10

for i in range(10):
    print(i)

print("***********************************************************")
for i in range(5, 15):
    print(i)

print("***********************************************************")
for i in range(0,51,10):
    print(i)
print("***********************************************************")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("***********************************************************")
for i in range(len(krediler)):
    print(krediler[i])
print("***********************************************************")

# while 

i = 0;
while i < 10:
    print("x")
    i += 1
print("y")

print("***********************************************************")

while True:
    print("x")
    break

print("***********************************************************")

i = 0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i += 1

# fonksiyonlar

fiyat = 100 
indirim = 20 

# definition - define
def calculate():
    print(100 - 20)



def calculateWithParams(fiyat , indirim):
    yeniFiyat = fiyat * ((100 - indirim) / 100)
    print(yeniFiyat)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(200 , 20)
sayHello("Tarık")
calculateWithParams(128 , 15)
sayHello("Enes")


def calculateAndReturn(price , discount):
    return price - discount

yeniFiyat2 = calculateAndReturn(200 , 34)
print(yeniFiyat2)


# instance => örnek
human1 = Human("Emre")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Melis")
human2.talk("Naber")
human2.walk()
print(human2)

Human("Tarık").talk("Naber")

