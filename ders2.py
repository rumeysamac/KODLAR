import re 

class BasitRAGYonetici:
    def __init__(self, parca_boyutu=80, ortasik_payi=20):
        self.parca_boyutu = parca_boyutu
        self.ortasik_payi = ortasik_payi
        self.veritabanı = []

    def metni_temizle_ve_kelimelere_ayir(self, metin: str) -> set:
        """Noktalama işaretlerini kaldırır, küçük harfe çevirir ve kelime kümesi döner."""
        temiz = re.sub(r'[^\w\s]', '', metin.lower())
        return set (temiz.split())

    def dokuman_yukle(self, dokuman: str):
        """Metni parçalara böler ve örtüşme ile kaydeder."""
        baslangic = 0
        metin_uzunlugu = len(dokuman) 

        while baslangic < metin_uzunlugu:
            bitis = baslangic + self.parca_boyutu
            parca = dokuman[baslangic:bitis].strip()
            self.veritabanı.append(parca)

            baslangic += (self.parca_boyutu - self.ortastik_payi) 

    def en_alakali_parcayi_bul(self, sorgu: str) -> str:
        """Sorgu kelimeleri ile parçalar arasındaki ortak kelime sayısını hesaplar."""
        sorgu_kelimeleri = self.metni_temizle_ve_kelimelere_ayir(sorgu)

        en_iyi_parca = ""
        en_yüksek_skor = -1

        for parca in self.veritabanı:
            parca_kelimeleri = self.metni_temizle_ve_kelimelere_ayir(parca)
            # İki metin arasındaki ortak kelime sayısı 
            ortak_kelimeler =len(sorgu_kelimeleri.intersection(parca_kelimeleri))

            if ortak_kelimeler > en_yüksek_skor:
                en_yüksek_skor = ortak_kelimeler
                en_iyi_parca = parca

        return en_iyi_parca

    def baglamli_istem_hazırla(self, sorgu: str) -> str:
        """Aranan parçayı bulur ve LLM'e verilecek nihai istemi (prompt) üretir."""
        bulunan_baglam = self.en_alakali_parcayi_bul(sorgu)


        istem = f"""Aşağıdaki BAĞLAM bilgisini kullanarak soruyu cevapla.

BAĞLAM:
{bulunan_baglam}

SORU:
{sorgu}

CEVAP:"""
        return istem

# ÇALIŞTIRMA VE TESTİ
if __name__ == "__main":
    rag = BasitRAGYonetici(parca_boyutu=100, ortasik_payi=20)

    ornek_dokuman = (
        "Cengiz Baba Chatbot projesi Streamlit ve FastAPI kullanılarak geliştirilmiştir."
        "Veritabanı olarak ChromaDB kullanılmıştır. Projede Cengiz Kurtoğlu şarkı sözleri"
        "üzerinde RAG mimarisi kurulmuştur. Kullanıcı sorularına bu veritabanı üzerinden cevap verilir."   
    )    

    rag.dokuman_yukle(ornek_dokuman)
    soru = "Projede hangi veritabanı kullanılmıştır?"
    hazir_prompt = rag.baglamli_istem_hazırla(soru)

    print(hazir_prompt)