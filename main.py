ogrenci_liste = []

def ogrenci_ekle(name_surname):
    ogrenci_liste.append(name_surname)
    return ogrenci_liste


print("***************************************************")

def ogrenci_sil(name_surname):
    ogrenci_liste.remove(name_surname)
    return ogrenci_liste
 

print("****************************************************")

def coklu_ogrenci_ekleme():
    ogrenci1 = input("Eklemek istediğiniz öğrenciyi giriniz")
    ogrenci_liste.append(ogrenci1)
    print("Güncel Liste: ", ogrenci_liste)
    while True:
        ekle = input("Başka öğrenci eklemek ister misiniz: Evet veya Hayır yazınız")
        if ekle == "Evet":
            name,surname=input( "Lütfen bir isim ve soyisim giriniz:").split()
            ogrenci_liste.append(name + " " + surname)
            print("Güncel Liste: ", ogrenci_liste)
        elif ekle == "Hayır":
            print("Döngü kapatılıyor...")
            break
        else:
            print("Lütfen Evet veya Hayır yazınız")
            


print("*****************************************************")

def ogrenci_listesi_yazdir():

    for ogrenci in range(0,len(ogrenci_liste)):
        print(ogrenci_liste[ogrenci])



print("******************************************************")


def ogrenci_no():
     print("Kayıt:")
     i = 0
     while i< len(ogrenci_liste):
        print(f"{i} No'lu Öğrenci:"+ ogrenci_liste[i])
        i+=1




print("*******************************************************")

def toplu_ogrenci_sil():
        sayı = input("Kaç öğrenci sileceksiniz?")
        for i in range(len(sayı)):
            sil = input("Hangi öğrenciyi silmek istiyorsunuz ? ")
            if sil in ogrenci_liste:
                ogrenci_liste.remove(sil)
                print(f" {sil} öğrenci listeden silindi. Güncel Liste: {ogrenci_liste}")
            else:
                print(f"{sil} listede bulunamadı.")
                
       
ogrenci_ekle("Eren Pedük")
print(ogrenci_liste)
ogrenci_sil("Eren Pedük")
print(ogrenci_liste)
coklu_ogrenci_ekleme()
coklu_ogrenci_ekleme()
ogrenci_listesi_yazdir()
ogrenci_no()
