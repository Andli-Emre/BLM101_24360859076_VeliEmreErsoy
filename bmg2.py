

def rle_encode(veri):
    #Kullanıcıdan alınan veriyi RLE algoritması ile sıkıştırır. 
    #Ardışık tekrar eden karakterleri sayar 
    #Örn: "AAAAABBB" -> "5A3B"
    #RLE sadece tekrar içeren verilerde etkilidir, karmaşık verilerde boyutu artırabilir

    # Veri girilmeden işlem yapılmaya çalışırsa boş döndür
    if not veri:
        return ""
    
    sikistirilmis_cikti = "" # Sonucu tutacağımız değişken
    sayac = 1 # Her karakter illaki vardır bu yüzden sayaç 0'dan değil 1'den başlar
    
    # 1. indisten başlayarak verinin sonuna kadar döngü kuruyoruz
    for i in range(1, len(veri)):
        # ilk karakterimiz (i), bir önceki karakter ile aynı mı?
        if veri[i] == veri[i-1]:
            sayac += 1 # Aynıysa sayacı 1 arttır
        else:
            # Farklı bir karaktere geçtik.
            # Önceki karakter grubunu (Sayı + Karakter) sonuca ekle.
            sikistirilmis_cikti += str(sayac) + veri[i-1]
            sayac = 1 # Sayacı yeni karakter için yeniden 1 yap 
            
    # Döngü bittiğinde, son kalan grubu da manuel olarak eklemeliyiz.
    # Çünkü döngü, son karakter değişmediği için onu eklemeden biter.
    sikistirilmis_cikti += str(sayac) + veri[-1]
    
    return sikistirilmis_cikti

def rle_decode(sikistirilmis_veri):
    
     # RLE ile sıkıştırılmış veriyi (Encode edilmiş) tekrar orijinal haline döndürür.
     # Verideki sayıları okur, yanındaki karakteri o sayı kadar çoğaltır.
     # Örn: "5A3B" -> "AAAAABBB"
   
    cozulmus_cikti = ""
    sayi_hafizasi = "" 
    for karakter in sikistirilmis_veri:
        if karakter.isdigit():
            # Eğer alınan karakter bir sayıysa, sayı hafızasına ekle. Böylece çok basamaklı sayıları yakalayabiliriz
         
            sayi_hafizasi += karakter
        else:
                    # Eğer sayı hafızası boşsa (hatalı format), varsayılan 1 kabul et
            if sayi_hafizasi == "":
                adet = 1
            else:
                adet = int(sayi_hafizasi)
            
            # Karakteri adet kadar arttırıp sonuca ekle
            cozulmus_cikti += karakter * adet
            
            # Sayı hafızasını sıfırlamalyız çünkü gelcek grup için işler karmaşık olabilir
            sayi_hafizasi = ""
            
    return cozulmus_cikti

def oran_hesapla(orijinal_str, sikistirilmis_str):
    
   # Orijinal veri ile sıkıştırılmış veri arasındaki kazanç oranını hesaplar. Formül: (1 - (Sıkışmış Boyut / Orijinal Boyut)) * 100
        
    uzunluk_ilk = len(orijinal_str)
    uzunluk_son = len(sikistirilmis_str)
    
    if uzunluk_ilk == 0:
        return 0.0
        
    oran = (1 - (uzunluk_son / uzunluk_ilk)) * 100
    return oran


if __name__ == "__main__":
    print(" ")
    print("======RLE VERİ SIKIŞTIRMA VE ÇÖZME ARACI======")
  
    while True:
        print("\nNe yapmak istersiniz?")
        print("1. Veri Sıkıştır (Encode)")
        print("2. Veri Çöz (Decode)")
        print("3. Çıkış (Sistem Kapanır)")
        
        secim = input("Seçiminiz (1/2/3): ")
        
        if secim == '1':
            # SIKIŞTIRMA İŞLEMLERİ
        
            giris = input("\nSıkıştırılacak veriyi girin (Örn: AAAAABBBCCDAA): ")
            
            if len(giris) == 0:
                print("Hata: VERİ GİRİLMEDİ!")
                continue

            sonuc = rle_encode(giris)
            basari_orani = oran_hesapla(giris, sonuc)
            
            print(f"\n-> Orijinal Veri: {giris}")
            print(f"-> Sıkıştırılmış Veri: {sonuc}") 
            print(f"-> Orijinal Boyut: {len(giris)} karakter")
            print(f"-> Yeni Boyut    : {len(sonuc)} karakter")
            
            # Oranı formatlı yazdırır 
            print(f"-> Sıkıştırma Oranı: %{basari_orani: .3f}")
            
            if len(sonuc) < len(giris):
                print("İşlem Başarılı: Veri boyutu küçüldü.")
            else:
                print("HATA!! Veri çok karmaşık olduğundan dolayı boyut küçültülemedi.")

        elif secim == '2':
            # ÇÖZME İŞLEMLERİ
            
            giris = input("\nÇözülecek (Sıkıştırılmış olan) veriyi girin (Örn: 5A3B2C1D2A): ")
            
      
            cozum = rle_decode(giris)
            print(f"\n-> Girdi (Sıkışmış): {giris}")
            print(f"-> Sonuç (Orijinal): {cozum}")
            
        elif secim == '3':
            print("Programdan çıkılıyor.\n SİSTEM KAPANIYOR")
            break
            
        else:
            print("Geçersiz seçim, lütfen tekrar deneyiniz.")
