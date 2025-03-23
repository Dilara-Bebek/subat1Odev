# 1. Hesap makinesi fonksiyonu
def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"  # Bölme işleminde 0'a bölme hatasını önleme
    return toplam, fark, carpim, bolum

# Kullanıcıdan iki sayı al
s1 = float(input("Birinci sayıyı girin: "))
s2 = float(input("İkinci sayıyı girin: "))

t, f, c, b = hesap_makinesi(s1, s2)
print(f"Toplam: {t}, Fark: {f}, Çarpım: {c}, Bölüm: {b}")

# 2. Palindrom kontrol fonksiyonu
def palindrom_mu(kelime):
    return kelime == kelime[::-1]  # Kelimeyi ters çevirerek kontrol etme

kelime = input("Bir kelime girin: ").lower()  # Küçük harfe çevirerek büyük/küçük harf farkını önleme
if palindrom_mu(kelime):
    print(f'"{kelime}" bir palindromdur.')
else:
    print(f'"{kelime}" bir palindrom değildir.')

# 3. 100 yaşına kaç yıl kaldığını hesaplayan fonksiyon
def kac_yil_sonra_100(yas):
    if yas < 100:
        return f"100 yaşına ulaşmanıza {100 - yas} yıl kaldı."
        
    else:
        return "Zaten 100 veya daha büyük yaşta!" 
      
     

yas = int(input("Yaşınızı girin: "))
sonuc = kac_yil_sonra_100(yas)
print(sonuc)


