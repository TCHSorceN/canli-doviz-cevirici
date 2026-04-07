import requests


def doviz_cevir():
    print("\n--- Canlı Döviz Dönüştürücü ---")

    baslangic = input("Hangi birimden? (Örn: USD, EUR, GBP): ").upper()
    hedef = input("Hangi birime? (Örn: TRY): ").upper()
    miktar = float(input("Miktar girin: "))

    url = f"https://api.exchangerate-api.com/v4/latest/{baslangic}"

    try:
        cevap = requests.get(url)
        veri = cevap.json()

        kur = veri["rates"][hedef]
        sonuc = miktar * kur

        print(f"\n✅ {miktar} {baslangic} = {sonuc:.2f} {hedef}")
        print(f"📈 Güncel Kur: 1 {baslangic} = {kur} {hedef}")

    except Exception as hata:
        print(f"❌ Bir hata oluştu: {hata}")


doviz_cevir()