gizli_sayi = 777

print("Sayı tahmin oyununa hoş geldin!")
print("Aklımdan bir sayı tuttum.")
print("Bakalım bulabilecek misin?")

tahmin = int(input("Tahminini gir: "))

while tahmin != gizli_sayi:
    print("Yanlış tahmin! Tekrar dene.")
    tahmin = int(input("Yeni tahminin: "))

print("Tebrikler! Doğru sayıyı buldun.")
