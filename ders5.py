#Çoklu araç seçimi
from google import genai
from google.genai import types

client = genai.Client(api_key="GEMINI API KEY")


def hava_durumu_getir(sehir: str) -> str:
    """Verilen şehrin anlık hava durumunu döner."""
    if sehir.lower() == "sakarya":
        return "18°C, Parçalı Bulutlu"
    return "Veri bulunamadı."


def doviz_kuru_getir(sembol: str) -> str:
    """Belirtilen döviz sembolünün TL karşılığını döner."""
    kurlar = {"usd": "34.20 TL", "eur": "37.50"}
    return kurlar.get(sembol.lower(), "Kur bulunamadı.")

# İKİ fonksiyonu birden tanıtıyoruz
chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        tools=[hava_durumu_getir, doviz_kuru_getir],
    )
)

response = chat.send_message("1 Dolar kaç TL yapıyor?")
print(response.text)

