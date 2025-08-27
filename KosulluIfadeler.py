#8- Koşullu İfadeler
yagmurlu = False
gunesli = False

if yagmurlu:  #Eğer
    print("Paltonu giy.")  #Yağmurlu değişkeni True ise Paltonu giy. Else if olduğu için False ise else if satırına geç.

elif gunesli:
    print("Güneş Gözlüğünü tak.")  #Python sıra tabanlı bir dil olduğu için baştan sona doğru işler. Yani yagmurlu True ise gunesliyi kontrol etmez bile.

else:
    print("Normal şekilde dışarı çık.")

#Üsttekilerden yagmurlu = True ise if çalışacak. yagmurlu = False & gunesli = True ise elif çalışacak. İkisi de False ise else çalışacak.
#Yani sıra sıra kontrol ediyor.
