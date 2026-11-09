
# ADIM 1

# 1.1 Tuple oluşturma
branslar = ("Yazılım", "Tasarım", "Pazarlama")

# 1.2 Boş öğrenci listesi
tum_ogrenciler = []


# ADIM 2

# 2.1 ve 2.2 Öğrenci ekleme ve strip() kullanma

isim1 = " Ahmet ".strip()
tum_ogrenciler.append([isim1, ["Yazılım"]])

isim2 = " Zeynep ".strip()
tum_ogrenciler.append([isim2, ["Tasarım"]])

isim3 = " Mehmet ".strip()
tum_ogrenciler.append([isim3, ["Pazarlama"]])


# ADIM 3

# 3.1 Listenin başına Başkan ekleme
tum_ogrenciler.insert(0, ["Başkan", ["Yazılım"]])

# 3.2 Toplam öğrenci sayısı
print("Toplam Kayıtlı Öğrenci Sayısı:", len(tum_ogrenciler))


# ADIM 4

# 4.1 İstediğiyle ayrılan öğrenciyi silme
tum_ogrenciler.remove(["Zeynep", ["Tasarım"]])

# 4.2 Son öğrenciyi listeden çıkarma
cikan_ogrenci = tum_ogrenciler.pop()

print("Sistemden en son çıkan öğrenci:", cikan_ogrenci[0])


# ADIM 5

# 5.1 Burak Tan öğrencisini ekleme
tum_ogrenciler.append(["Burak Tan", ["Tasarım"]])

# 5.2 Geçici alfabetik sıralama
gecici_liste = sorted(tum_ogrenciler)

print("Geçici alfabetik liste:", gecici_liste)

# Orijinal listenin değişmediğini gösterme
print("Orijinal liste:", tum_ogrenciler)

# 5.3 Kalıcı alfabetik sıralama
tum_ogrenciler.sort()

print("Kalıcı alfabetik liste:", tum_ogrenciler)
