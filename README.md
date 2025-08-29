# Spam Mesaj Tespit Edici 🚨

Bu proje, makine öğrenmesi kullanarak e-posta veya mesajların spam olup olmadığını tespit eden bir Python uygulamasıdır.

## 🎯 Özellikler

- E-posta/mesaj metnini spam veya normal (ham) olarak sınıflandırma
- Metin temizleme ve ön işleme
- TF-IDF vektörizasyonu
- Lojistik Regresyon modeli
- Interaktif konsol arayüzü

## 🛠️ Gereksinimler

- Python 3.8+
- pandas
- numpy
- scikit-learn
- regex

## 🚀 Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/Semihkulekcioglu/Email_spam_detection.git
cd Email_spam_detection
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## 💻 Kullanım

1. Programı çalıştırın:
```bash
python Spam_Tespit_Edici.py
```

2. İstendiğinde test etmek istediğiniz mesaj metnini girin
3. Program metni analiz edip spam olup olmadığını belirtecektir
4. Çıkmak için 'q' tuşuna basın

## 📊 Model Performansı

Model, test verisi üzerinde yüksek doğruluk oranı ile çalışmaktadır. Detaylı performans metrikleri program çalıştırıldığında konsola yazdırılmaktadır.

## 📝 Veri Seti

Proje, spam_ham_dataset.csv veri setini kullanmaktadır. Bu veri seti spam ve normal e-posta örneklerini içermektedir.

## 🤝 Katkıda Bulunma

1. Bu repoyu forklayın
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: XYZ'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Bir Pull Request oluşturun

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.

---
[English README](README_EN.md)
