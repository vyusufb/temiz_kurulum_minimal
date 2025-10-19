# Kali Linux Geliştirici Ortamı Kurulum Betiği (Kali Dev Setup)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Shell Script](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white)

Bu proje, temiz bir Kali Linux kurulumunu hızlıca bir geliştirme ortamına dönüştürmek için tasarlanmış bir Python betiği içerir. Betik, özellikle siber güvenlik alanındaki GitHub projelerini klonlamak, derlemek ve test etmek için gerekli olan temel araçları ve kütüphaneleri otomatik olarak kurar.

## 🎯 Amaç

Kali Linux, yüzlerce sızma testi aracıyla birlikte gelir. Ancak, sistemini sadece GitHub'dan indirilen projeleri test etmek veya siber güvenlik alanında kod geliştirmek için kullanmak isteyenler için bu araçların çoğu gereksizdir ve disk alanı kaplar.

Bu betik, Kali'yi "şişkinlikten" arındırarak aşağıdaki hedeflere hizmet eder:
* **Minimalizm:** Sadece kod derlemek ve çalıştırmak için gerekli olan temel paketleri kurar.
* **Hız:** Gereksiz araçları kurmayarak kurulum süresini önemli ölçüde kısaltır.
* **Otomasyon:** Tek bir komutla tüm güncelleme, paket kurulumu ve sistem temizliği işlemlerini yapar.
* **Sağlamlık:** Hata kontrolü, detaylı loglama ve otomasyon dostu komutlar (`apt-get`) kullanarak güvenilir bir kurulum süreci sunar.

## ✨ Özellikler

* **Sistem Güncelleme:** `apt-get update` ve `apt-get full-upgrade` komutlarıyla sistemi en son sürüme günceller.
* **Temel Geliştirici Araçları:** `build-essential`, `git`, `python3-pip`, `python3-venv`, `curl` gibi temel geliştirme ve derleme araçlarını kurar.
* **Gerekli Python Kütüphaneleri:** `requests`, `pwntools`, `scapy` gibi siber güvenlik projelerinde sıkça kullanılan Python paketlerini `pip` ile yükler.
* **Otomatik ve Etkileşimsiz:** `DEBIAN_FRONTEND=noninteractive` ortam değişkeni sayesinde kurulum sırasında kullanıcıdan herhangi bir girdi beklemez.
* **Detaylı Loglama:** Tüm işlemleri ve komut çıktılarını `kali_dev_setup.log` adlı bir dosyaya kaydederek hata ayıklamayı kolaylaştırır.
* **Temizlik:** Kurulum tamamlandıktan sonra `apt-get autoremove` ve `apt-get clean` komutlarıyla gereksiz paketleri ve önbelleği temizleyerek disk alanı kazandırır.

## 🛠️ Neler Kuruluyor?

### APT Paketleri:
* `build-essential`: C/C++ derleyicileri ve kütüphaneleri.
* `git`: Versiyon kontrol sistemi.
* `python3-pip` / `python3-venv`: Python paket ve sanal ortam yöneticileri.
* `curl` / `wget`: Veri transferi ve dosya indirme araçları.
* `htop` / `net-tools`: Sistem izleme ve temel ağ araçları.
* Projeler için genel bağımlılıklar (`libgfortran5`, `python3-dev` vb.).

### Pip Paketleri:
* `requests`: HTTP istekleri için.
* `beautifulsoup4`: HTML ve XML ayrıştırma.
* `scapy`: Ağ paketi oluşturma ve analizi.
* `pwntools`: CTF ve exploit geliştirme kütüphanesi.
* `colorama`: Renkli terminal çıktıları için.

## 🚀 Kullanım

**Ön Koşul:** Temiz ve yeni kurulmuş bir Kali Linux sistemi.

1.  **Betiği İndirin:**
    Proje deposunu klonlayın veya `kali_dev_setup.py` dosyasını doğrudan indirin.
    ```bash
    git clone [PROJE_URLSİ]
    cd [PROJE_DİZİNİ]
    ```
    veya
    ```bash
    wget https://[DOĞRUDAN_DOSYA_URLSİ]/kali_dev_setup.py
    ```

2.  **Çalıştırma İzni Verin:**
    Betiği çalıştırılabilir hale getirin.
    ```bash
    chmod +x kali_dev_setup.py
    ```

3.  **Betiği `sudo` ile Çalıştırın:**
    Betik, sistem genelinde kurulum yapacağı için yönetici (root) yetkileri gerektirir.
    ```bash
    sudo ./kali_dev_setup.py
    ```
    veya
    ```bash
    sudo python3 kali_dev_setup.py
    ```

Betiğin çalışması tamamlandığında, terminalde ve `kali_dev_setup.log` dosyasında tüm adımların detaylarını görebilirsiniz.

## 🔧 Özelleştirme

Betiği kendi ihtiyaçlarınıza göre kolayca düzenleyebilirsiniz. `kali_dev_setup.py` dosyasını bir metin düzenleyici ile açarak:
* `apt_packages` listesine yeni APT paketleri ekleyebilir/çıkarabilirsiniz.
* `pip_packages` listesine yeni Python kütüphaneleri ekleyebilir/çıkarabilirsiniz.

Made bu vyusufb
