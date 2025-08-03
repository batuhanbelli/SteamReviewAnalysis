# Steam Yorum İndirme Aracı (Steam Review Extractor)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

Kullanıcıların Steam'deki herhangi bir oyun için, istedikleri dilde ve sayıda yorumu, seçtikleri veri sütunlarıyla birlikte temiz bir CSV dosyası olarak indirmelerini sağlayan bir masaüstü uygulaması.


![Uygulama Ekran Görüntüsü](images/screenshot.png) 

---


###  Özellikler

* **Dinamik Veri Çekme:** Herhangi bir Steam oyununun linkini yapıştırarak yorumları çekme.
* **Özelleştirilebilir Veri Miktarı:** Çekilecek sayfa sayısını belirleyerek indirilecek yorum miktarını kontrol etme.
* **Çoklu Dil Desteği:** Yorumları belirli bir dilde (İngilizce, Türkçe, Almanca vb.) veya tüm dillerde indirme seçeneği.
* **Esnek Sütun Seçimi:** İhtiyaç duyulan veri sütunlarını (yazar, oynama süresi, yorum metni vb.) arayüz üzerinden seçme.
* **Temiz Çıktı:** Seçilen verileri doğrudan analizde kullanılabilecek, temiz bir `.csv` dosyası olarak kaydetme.
* **Kullanıcı Dostu Arayüz:** `CustomTkinter` ile oluşturulmuş modern ve kolay kullanımlı bir masaüstü uygulaması.

---

###  Kullanılan Teknolojiler

Bu proje aşağıdaki teknolojiler ve kütüphaneler kullanılarak geliştirilmiştir:

* **Python:** Ana programlama dili.
* **CustomTkinter:** Modern ve kullanıcı dostu arayüz tasarımı için.
* **Pandas:** Verileri işlemek, filtrelemek ve CSV olarak kaydetmek için.
* **Requests:** Steam Web API'sine HTTP istekleri göndermek için.

---

###  Kurulum ve Başlangıç

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.


#### Kurulum Adımları

1.  **Projeyi Klonlayın:**
    ```sh
    git clone [https://github.com/](https://github.com/)[SENİN-GITHUB-KULLANICI-ADIN]/[PROJE-ADI].git
    ```

2.  **Proje Klasörüne Gidin:**
    ```sh
    cd [PROJE-ADI]
    ```

3.  **Gerekli Kütüphaneleri Yükleyin:**
    Proje için gerekli tüm kütüphaneler `requirements.txt` dosyasında listelenmiştir. Aşağıdaki komut ile hepsini tek seferde kurabilirsiniz.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Uygulamayı Çalıştırın:**
    ```sh
    python main.py 
    ```
    *(`main.py` yerine kendi ana dosyanızın adını yazın)*

---

###  Kullanım

1.  Uygulamayı çalıştırın.
2.  İlgili alana Steam Web API anahtarınızı girin.
3.  Analiz etmek istediğiniz oyunun Steam mağaza linkini yapıştırın.
4.  Kaç sayfa yorum çekmek istediğinizi belirtin.
5.  Yorumların hangi dilde olmasını istediğinizi seçin.
6.  İndirmek istediğiniz veri sütunlarını işaretleyin.
7.  "Veriyi Çek ve İndir" butonuna tıklayın.
8.  Açılan pencerede dosyayı kaydetmek istediğiniz konumu ve dosya adını seçin.

---

###  Gelecekteki Geliştirmeler

* [ ] Veri çekme işlemi tamamlandığında temel analizleri (pozitif/negatif oranı, kelime bulutu vb.) doğrudan uygulama içinde gösterme.
* [ ] `PyInstaller` gibi araçlarla projeyi tek tıklamayla çalıştırılabilen bir `.exe` dosyasına dönüştürme.
* [ ] Yorumları oynama süresine göre filtreleme seçeneği ekleme (örn: Sadece 10 saatten fazla oynamış olanların yorumlarını indir).

---
