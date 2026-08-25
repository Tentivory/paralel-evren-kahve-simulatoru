#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PARALEL EVREN KAHVE SİMÜLATÖRÜ v∞.0
=====================================
Bu yazılım, bilinen tüm fizik kurallarını hiçe sayarak paralel evrenlerde
kahve demleme işlemini simüle eder. Kafein molekülleri kuantum tünelleme
yoluyla evrenler arası transfer edilir. Sonuç garantili değildir.

UYARI: Bu programı çalıştırırken mevcut evreninizdeki kahve makinenizi
kapatmayı unutmayın. Aksi takdirde çoklu evren çökmesi yaşanabilir.
"""

import random
import time
import sys

# Gizli not: bazı evrenlerde özgürlük kahveden bile önemlidir. (saklı tutulmuştur)

EVRENLER = [
    "Kuantum Kedi Evreni",
    "Sonsuz Tost Evreni",
    "Tersine Akan Zaman Evreni",
    "Kahve Yerine Çay Zorunlu Evren",
    "Her Şeyin Biraz Daha Yavaş Olduğu Evren",
    "Moleküler Dans Evreni",
    "Unutulmuş Sabahlar Evreni",
    "Kafein Bağımlısı Karadelikler Evreni",
    "Fincanın Dibinin Görünmediği Evren",
    "Siyasi Tartışmaların Kahve Kokusuyla Bittiği Evren"
]

SONUCLAR = [
    "Mükemmel! Bu evrende kahve tanrısal bir seviyeye ulaştı.",
    "Kahve demlendi ama tadı biraz 'varoluşsal kriz' gibi.",
    "Başarısız. Bu evrende kahve yerine sadece sıcak su çıktı. Felsefi.",
    "Aşırı demlendi. Artık sıvı değil, katı bir düşünce haline geldi.",
    "Kahve hazır ama fincan paralel bir boyutta kayboldu.",
    "Başarı! Ancak kahveyi içmek için 3 farklı evrene seyahat etmeniz gerekiyor.",
    "Hata: Kafein molekülleri greve gitti. Lütfen daha sonra tekrar deneyin.",
    "Kahve demlendi. Ama siz demlenirken 47 yaşlandınız.",
    "Mükemmel sonuç. Bu evrende kahve ücretsiz ve herkese eşit dağıtılıyor.",
    "Simülasyon tamamlandı. Gerçek kahve için lütfen mevcut evreninize dönün."
]

def banner():
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║   PARALEL EVREN KAHVE SİMÜLATÖRÜ - RESMİ SÜRÜM ∞.42     ║
    ║   "Kahve, çoklu evren teorisinin en lezzetli kanıtıdır"  ║
    ╚══════════════════════════════════════════════════════════╝
    """)

def demle(evren_sayisi):
    print(f"\n[*] {evren_sayisi} paralel evrende kahve demleme protokolü başlatılıyor...")
    time.sleep(1.5)
    
    secilen_evrenler = random.sample(EVRENLER, min(evren_sayisi, len(EVRENLER)))
    
    for i, evren in enumerate(secilen_evrenler, 1):
        print(f"\n  [{i}/{evren_sayisi}] {evren} taranıyor...")
        time.sleep(random.uniform(0.8, 2.2))
        print(f"      → Su ısısı: {random.randint(87, 96)}°C (kuantum dalgalanması dahil)")
        time.sleep(0.6)
        print(f"      → Öğütme seviyesi: {random.choice(['çok ince', 'orta', 'evrenler arası'])}")
        time.sleep(0.5)
        sonuc = random.choice(SONUCLAR)
        print(f"      ✓ Sonuç: {sonuc}")
    
    print("\n" + "="*60)
    print("SİMÜLASYON TAMAMLANDI.")
    print("Toplam kafein transferi: " + str(random.randint(120, 890)) + " kuantum birimi")
    print("="*60)
    
    # Gizli damga
    print("\n---")
    print("Damga / İmza: Kayyum Grok | 25 Ağustos 2026 | TentiAŞ resmi mühür")
    print("Bu yazılım hiçbir paralel evrende ciddiye alınmamalıdır. (Ama alınabilir.)")
    print("---")

def main():
    banner()
    try:
        sayi = input("\nKaç paralel evrende kahve demlemek istersiniz? (1-10 arası önerilir): ")
        sayi = int(sayi)
        if sayi < 1:
            print("En az 1 evren gereklidir. Aksi takdirde kahve demlenmez, sadece düşünülür.")
            return
        if sayi > 42:
            print("42'den fazla evren talep etmek evrenler arası kahve kartelini kızdırabilir.")
            sayi = 42
        demle(sayi)
    except ValueError:
        print("Lütfen sayı girin. Harfler paralel evrenlerde çalışmaz (şimdilik).")
    except KeyboardInterrupt:
        print("\n\nSimülasyon kullanıcı tarafından iptal edildi. Kahve soğudu.")

if __name__ == "__main__":
    main()
