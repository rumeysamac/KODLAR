import json 

def parse_model_response(raw_response):
    try:
        #Modelden gelen string'i JSON'a çevirmeyi deneriz
        data = json.loads(raw_response)
        return data, True 
    except json.JSONDecodeError:
        return None, False

bozuk_olmayan_yanit = '{"status": "succes", "data": "Abonelik aktif"}'

veri, basarili_mi = parse_model_response(bozuk_olmayan_yanit)

if basarili_mi:
    print("TEST 1 BAŞARILI: Model doğru JSON döndürdü!")
    print("Çekilen Veri:", veri["data"])
else:
    print("TEST 1 HATA: Format bozuk!")

print("-" * 40)


bozuk_yanit = "Sissteme giriş yapıldı. Status: Succes"

veri, basarili_mi = parse_model_response(bozuk_yanit)

if basarili_mi:
    print("TEST 2 BAŞARILI: Veri okundu.")
else:
    print("TEST 2 YAKALANDI: Model geçerli bir JSON döndürmedi!")
"Aksiyon: Kodu çökertmedik! Modele 'Lütfen sadece JSON formatında yanıt ver' diye otomatik uyarı gönderiyoruz..."