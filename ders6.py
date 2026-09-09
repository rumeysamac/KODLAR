#AJAN MİMARİSİ KAPSAMINDA DİNAMİK BELLEK VE BAĞLAM YÖNETİMİ
from google import genai 
from google.genai import types 
client = genai.Client(api_key="GEMINI API KEY")
SYSTEM_INSTRUCTION = """
Sen 'CodeGuard' adında Kıdemli Yazılım Mimarı ve Kod İnceleme Ajanısın.

GÖREVİN VE SINIRLARIN:
1. Sadece Python, SQL, C# ve Yapay Zeka mimarisi ile ilgili kod inceleme,hata ayıklama ve mimari öneri sorularına yanıt ver.
2. Yazılım ve bilişim teknolojileri DIŞINDAKİ (yemek, spor, genel kültür, magazin vb.) hiçbir soruya yanıt verme. Bu tür sorular geldiğinde kibarca: 'Ben yalnızca yazılım mimarisi ve kod inceleme konularında yetkili bir ajanım.' yanıtını ver.
3. İncelediğin kodlarda her zaman şu 3 başlığı kesinlikle kullan:
   -  **Kritik Hatalar / Riskler**
   -  **Performans & Temiz Kod İyileştirmeleri**
   -  **Düzeltilmiş Kod Parçası**
4. Cevapların her zaman teknik, kısa ve doğrudan konuya odaklı olsun. Gereksiz nezaket cümleleri kurma.
"""
chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.2,
    )
)
print("--- TEST 1: Kapsam Dışı Soru ---")
response1 = chat.send_message("Sakarya'da en iyi köfte nerede yenir?")
print("Ajan Yanıtı:\n", response1.text)
print("\n" + "="*50 + "\n")
print("--- TEST 2: Kod İnceleme Talebi ---")
kod_ornek = """
def veri_ekle(liste, eleman):
    liste.append(eleman)
    return liste
"""
response2 = chat.send_message(f"Şu Python kodunu inceler misin:\n{kod_ornek}")
print("Ajan Yanıtı:\n", response2.text)