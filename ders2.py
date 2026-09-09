#RAG Bağlam Besleme
from google import genai
from google.genai import types 

client = genai.Client(api_key="GEMINI API KEY")


baglam_metni = "Proje başlangıç tarihi 17.07.2027"

kullanici_sorusu = "Projenin başlangıç tarihi nedir?"


kombine_prompt = f"""
Aşağıdaki BAGLAM metnini kullanarak soruyu cevapla.and

BAGLAM:
{baglam_metni}

SORU:
{kullanici_sorusu}
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=kombine_prompt,
    config=types.GenerateContentConfig(
        temperature=0.0,   #Deterministik çıktı
        system_instruction="Sadece verilen metne sadık kal. Metinde yoksa 'Bu bilgi verilen belgede yer almamaktadır' de.",
    ),
)
print(response.text)