#METİN PARÇALAMA (CHUNKS)

def create_chunks(text, chunk_size=7):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)
    return chunks 

doc = "Yapay zeka teknolojileri her geçen gün gelişmeye devam ediyor."
print(create_chunks(doc, chunk_size=4))  


