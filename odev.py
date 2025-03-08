def dosyaya_yaz_ve_oku():
    
    metin = input("Dosyaya yazmak istediğiniz metni girin: ")

    
    try:
        with open("metin.txt", "w", encoding="utf-8") as dosya:
            dosya.write(metin)
        print("Metin dosyaya yazıldı.")
    except Exception as e:
        print(f"Dosyaya yazma hatası: {e}")
        return

    try:
        with open("metin.txt", "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
        print("\nDosya içeriği:")
        print(icerik)
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except Exception as e:
        print(f"Dosyayı okuma hatası: {e}")

dosyaya_yaz_ve_oku()

def satirlari_yaz_ve_oku():
    satirlar = []
    for i in range(5):
        satir = input(f"{i+1}. satırı girin: ")
        satirlar.append(satir + "\n") 

    
    try:
        with open("satirlar.txt", "w", encoding="utf-8") as dosya:
            dosya.writelines(satirlar)
        print("Satırlar dosyaya yazıldı.")
    except Exception as e:
        print(f"Dosyaya yazma hatası: {e}")
        return

    
    try:
        with open("satirlar.txt", "r", encoding="utf-8") as dosya:
            print("\nDosya içeriği (satır satır):")
            for satir in dosya:
                print(satir, end="") 
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except Exception as e:
        print(f"Dosyayı okuma hatası: {e}")

satirlari_yaz_ve_oku()