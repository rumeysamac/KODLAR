#MESSAGES LİSTESİ İLE HAFIZA VE BAĞLAM YÖNETİMİ
messages = [
    {
        "role":"system",
        "content": "Sen yardımcı bir asistansın. Kullanıcının adı: Rümeysa.",
    }
]
def add_user_message(user_input):
    messages.append({"role": "user", "content": user_input})


def trim_memory(messages_list, max_messages=5):
    if len(messages_list) > max_messages:
        #0. eleman kalır,son mesajlar korunur
        return [messages_list[0]] + messages_list[-(max_messages - 1) :]
    return messages_list


add_user_message("Mert Hakan Yandaş.")
add_user_message("Barış Alper Yılmaz.")
add_user_message("Demba Ba.")
add_user_message("Pascal Nouma.")
add_user_message("Atiba Huntchinson.")
add_user_message("Süleyman Seba.")

print("--- BUDAMAN ÖNCEKİ HAFIZA (Toplam 7 Eleman) ---")
print(f"Eleman Sayısı: {len(messages)}")

temizlenmis_hafiza = trim_memory(messages, max_messages=5)

print("\n---Eleman Sayısı: {len(temizlenmis_hafiza)}")
print(f"Eleman Sayısı: {len(temizlenmis_hafiza)}")

print("\n--- MODELE GÖNDERİLECEK SON LİSTE ---")
for item in temizlenmis_hafiza:
    print(item)
