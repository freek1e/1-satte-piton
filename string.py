#7- Stringleri detaylandırıyorum.
#YanlisKonusma = "Benimle "adam gibi" konuş." #Bu
#BirBaskaYanlisKonusma = 'Benimle 'adam gibi' konuş.' #Ve bu yanlış.
DogruKonusma1 = 'Benimle "adam gibi" konuş.' #Doğru yöntem içerideki ve dışarıdaki tırnakları farklı yapmak.
DogruKonusma2 = "Benimle 'adam gibi' konuş." # Bu da bir diğer doğru yazım.


print(DogruKonusma1)
print()
print(DogruKonusma2)
print()

mektup = """Merhaba mehmet
umarım iyisindir."""
print(mektup)
print()

#Python'da bir stringin harfleri sırayla 012345 diye gider. Mesela Mehmet ismindeki h harfi "2" koduna sahiptir.
isim = "mehmet"
print(isim[2])  #2 kodlu harf yani "h"
print(isim[0:3])  #İlk 3 harfi yazdır. 0 kodludan başla ve 3 kodluda bitir. 3 kodlu harf dahil değil.
print(isim[-1])  #Sondan 1. harfi almak için başına - getiriyorum.

#Diğer fonksiyonlar

print(len(isim))  #String'in uzunluğunu yazdır.
print(isim.title())  #İlk harfi büyütüp yazdır.
print(isim.upper())  #Bütün harfleri büyütüp yazdır.

BuyukIsim = "MEHMET"
print(BuyukIsim.lower())  #Bütün harfleri küçültme.
print(isim.find("t"))  #Bir harfin kaçıncı sırada olduğunu yazdır. (Dikkat 0'dan başlar)

cumle = "Samet bakkaldan süt aldı."
print(cumle.replace("aldı.","almadı."))

#Alıştırma
print()
name = input("Adınız nedir? ")
print("Merhaba, " + name.title())
