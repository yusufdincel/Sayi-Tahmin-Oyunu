import random
sayi = random.randrange(1,1000)
deneme = 1
print(deneme,". Tahmininizi giriniz: ")
tahmin = int(input())

while(tahmin != sayi):
    if(tahmin>sayi):
        print("Büyük")
        deneme += 1
        print(deneme, ". Tahmininizi giriniz: ")
        tahmin = int(input())
    elif(tahmin<sayi):
        print("Küçük")
        deneme += 1
        print(deneme, ". Tahmininizi giriniz: ")
        tahmin = int(input())
    else:
        break
if(tahmin==sayi):
    print("Tebrikler ", deneme, ". denemede buldunuz.")
