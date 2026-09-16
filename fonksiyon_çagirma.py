# FONKSİYON ÇAĞIRMA 

import json 

# GERÇEK PYTHON FONKSİYONLARI (TOOLS)
def urun_fiyati_getir(urun_adi: str) -> dict:
    """Veritabanından ürün fiyatını getirir."""
    veritabani = {"laptop": 35000, "telefon": 25000, "kulaklik": 1500}
    fiyat = veritabani.get(urun_adi.lower())
    if fiyat:
        return {"urun": urun_adi, "fiyat_tl": fiyat, "stokta_var_mi": True}
    return {"hata": "Ürün bulunamadı"}

def hava_durumu_getir(sehir: str) -> dict:
    """API sorgusu simüle ederek şehir hava durumunu getirir."""
    hava_verisi = {"İstanbul": "22°C Parçalı Bulutlu", "sakarya": "19°C Yağmurlu", "ankara": "15°C Açık"}
    durum = hava_verisi.get(sehir.lower())
    if durum:
        return {"sehir": sehir.capitalize(), "durum": durum}
    return{"hata": "Şehir  bulunamadı"}

def hesap_makinesi(islem: str, sayi1: float, sayi2: float) -> dict:
    """Temel matematiksel işlemleri gerçekleştirir."""
    if islem == "toplama":
        sonuc = sayi1 + sayi2
    elif islem == "carpma":
        sonuc = sayi1 * sayi2
    else:
        return {"hata": "Geçersiz İşlem"}
    return {"islem": islem, "sonuc": sonuc}            

FONKSİYON_HARİTASI = {
    "urun_fiyati_getir": urun_fiyati_getir,
    "hava_durumu_getir": hava_durumu_getir,
    "hesap_makinesi": hesap_makinesi
}

# DİNAMİK YÖNLENDİRİCİ
def dinamik_fonksiyon_calistir(model_yaniti: dict) -> dict:
    """
    Modelden gelen JSON ne olursa olsun, doğru fonksiyonu bulur
    ve parametreleriyle çalıştırır.
    """
    fn_adi = model_yaniti.get("function_name")
    parametreler = model_yaniti.get("arguments", {})
    call_id = model_yaniti.get("call_id")

    # Fonksiyon haritada mı kontrol edilen kısım
    if fn_adi in FONKSİYON_HARİTASI:
        hedef_fonksiyon = FONKSİYON_HARİTASI[fn_adi]

    else:
            return {"hata": f"'{fn_adi}' isimli bir fonksiyon sistemde tanımlı değil."}


    fonksiyon_sonucu = hedef_fonksiyon(**parametreler)
        # Json formatına dönüştürme
    return{
            "role": "tool",
            "tool_call_id": call_id,
            "content": json.dumps(fonksiyon_sonucu, ensure_ascii=False)
        }
    

 # FARKLI MODEL YANITLARI İLE TEST ETME
# Senaryo A: Kullanıcı "Sakaryada hava nasıl?" diye sordu
model_yaniti_1 = {
    "call_id": "call_101",
    "function_name": "hava_durumu_getir",
    "arguments": {"sehir": "sakarya"}
}

# Senaryo B: Kullanıcı "25 ile 4'ü çarp" diye sordu
model_yaniti_2 = {
    "call_id": "call_102",
    "function_name": "hesap_makinesi",
    "arguments": {"islem": "carpma", "sayi1": 25, "sayi2": 4}
}

# Senaryo C: Kullanıcı "Kulaklık ne kadar?" diye sordu
model_yaniti_3 = {
    "call_id": "call_103",
    "function_name": "urun_fiyati_getir",
    "arguments": {"urun_adi": "kulaklik"}
}

# ÇIKTILAR
print("--- Senaryo 1 Çıktısı ---")
print(dinamik_fonksiyon_calistir(model_yaniti_1))

print("\n--- Senaryo 2 Çıktısı ---")
print(dinamik_fonksiyon_calistir(model_yaniti_2))

print("\n--- Senaryo 3 Çıktısı ---")
print(dinamik_fonksiyon_calistir(model_yaniti_3))