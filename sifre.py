import random
isim = input("Lütfen adınızı giriniz : ")
soyisim = input("Lütfen soyadınızı giriniz : ")
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Şifre Uzunluğunu Girin :"))
sifre = ""
for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)


print("Merhaba", isim, soyisim, "Şifreniz : " , sifre)
