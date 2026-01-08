# BLM101_24360859076_VeliEmreErsoy
24360859076 Veli Emre Ersoy BLM101 Proje Ödevi

Youtube Linki: https://www.youtube.com/watch?v=iVaK_5XFcSE

📦 Run-Length Encoding (RLE) – Python Veri Sıkıştırma Projesi

Bu proje, Run-Length Encoding (RLE) algoritmasını kullanarak metin verilerinin kayıpsız şekilde sıkıştırılması ve tekrar çözülmesini amaçlayan bir Python uygulamasıdır.
Proje, Bilgisayar Mühendisliğine Giriş dersi kapsamında hazırlanmıştır.

📌 Proje Hakkında

Run-Length Encoding (RLE), ardışık tekrar eden karakterleri sayarak daha kısa bir temsil oluşturan basit ve etkili bir kayıpsız veri sıkıştırma algoritmasıdır.
Örnek:
Orijinal Veri: AAAAABBB
RLE Sonucu : 5A3B

Bu proje sayesinde:
Veri temsili ve bit düzeyinde sıkıştırma mantığı öğrenilir
RLE algoritmasının avantaj ve dezavantajları gözlemlenir
Python ile algoritma uygulama pratiği kazanılır

🎯 Projenin Amaçları

-Veri sıkıştırma kavramını uygulamalı olarak göstermek
-RLE algoritmasının çalışma mantığını öğretmek
-Sıkıştırma oranını hesaplayarak verimliliği analiz etmek
-Encode (sıkıştırma) ve Decode (çözme) işlemlerini yapmak

⚙️ Kullanılan Teknolojiler

-Python 3
-Standart Python kütüphaneleri
-Konsol (Terminal) tabanlı kullanıcı arayüzü

🧠 Algoritma Mantığı (RLE)

1)Veri soldan sağa okunur
2)Aynı karakterler sayılır
3)Karakter değiştiğinde:
4)tekrar sayısı + karakter çıktıya eklenir
5)Veri bittiğinde son grup da eklenir

✔️ Başarılı Örnek
AAAAABBBCCCC → 5A3B4C

❌ Başarısız Örnek
ABCDE → 1A1B1C1D1E


⚠️ Not: RLE algoritması, tekrar oranı yüksek verilerde etkilidir, karmaşık verilerde boyutu artırabilir.

🧩 Fonksiyonlar
rle_encode(veri)

-Verilen metni RLE algoritması ile sıkıştırır
-Tekrar eden karakterleri sayar
-Çıktı formatı: Sayı + Karakter

rle_decode(sikistirilmis_veri)

-RLE ile sıkıştırılmış veriyi çözer
-Sayıları okuyarak karakterleri çoğaltır
-Orijinal veriyi geri üretir

oran_hesapla(orijinal_str, sikistirilmis_str)

Sıkıştırma oranını yüzde olarak hesaplar
Formül:
(1 - (Sıkıştırılmış Boyut / Orijinal Boyut)) × 100


🖥️ Programın Çalışma Şekli

Program çalıştırıldığında kullanıcıya bir menü sunar:

1. Veri Sıkıştır (Encode)
2. Veri Çöz (Decode)
3. Çıkış


Kullanıcı seçimine göre:

-Veri sıkıştırılır
-Sıkıştırılmış veri çözülür
-Sıkıştırma oranı hesaplanır

📊 Örnek Çıktı
Orijinal Veri: AAAAABBB
Sıkıştırılmış Veri: 5A3B
Orijinal Boyut: 8 karakter
Yeni Boyut: 4 karakter
Sıkıştırma Oranı: %50.000

👨‍🎓 Proje Bilgileri

Ders: Bilgisayar Mühendisliğine Giriş

Konu: Veri Depolama ve Sıkıştırma Algoritmaları

Algoritma: Run-Length Encoding (RLE)

Dil: Python

✍️ Hazırlayan

Veli Emre Ersoy
Öğrenci No: 24360859076

📚 Kaynaklar

Computer Science – Chapter 1

Data Compression Fundamentals

Run-Length Encoding (RLE) Algorithm

Python Resmi Dokümantasyonu
