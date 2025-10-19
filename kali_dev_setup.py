#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import logging
import shutil
from pathlib import Path
from typing import List

log_file = "kali_dev_setup.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

class Colors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_header(message: str):
    header = f"===== {message} ====="
    logging.info(header)
    print(f"\n{Colors.HEADER}{Colors.BOLD}{header}{Colors.ENDC}")

def run_command(command: str) -> bool:
    logging.info(f"Komut çalıştırılıyor: {command}")
    print(f"\n{Colors.OKCYAN}▶️  Çalıştırılıyor: {command}{Colors.ENDC}")
    try:
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding='utf-8', errors='replace'
        )
        for line in process.stdout:
            print(line, end='')
            logging.info(line.strip())
        process.wait()
        
        if process.returncode != 0:
            error_msg = f"Hata: Komut '{command}' {process.returncode} koduyla başarısız oldu."
            logging.error(error_msg)
            print(f"\n{Colors.FAIL}❌ {error_msg}{Colors.ENDC}")
            return False
            
    except Exception as e:
        error_msg = f"Komut çalıştırılırken bir istisna oluştu: {e}"
        logging.critical(error_msg)
        print(f"\n{Colors.FAIL}❌ {error_msg}{Colors.ENDC}")
        return False
        
    success_msg = f"Başarıyla tamamlandı: {command}"
    logging.info(success_msg)
    print(f"\n{Colors.OKGREEN}✅ {success_msg}{Colors.ENDC}")
    return True

def main():
    if os.geteuid() != 0:
        logging.critical("Bu betik root yetkileriyle çalıştırılmalıdır.")
        print(f"{Colors.FAIL}Lütfen 'sudo python3 {sys.argv[0]}' komutunu kullanın.{Colors.ENDC}")
        sys.exit(1)

    logging.info("Kali Linux Minimal Geliştirici Kurulum Betiği Başlatıldı.")
    print(f"{Colors.BOLD}Tüm çıktılar aynı zamanda '{log_file}' dosyasına kaydedilmektedir.{Colors.ENDC}")

    if not all(shutil.which(cmd) for cmd in ["apt-get", "git", "pip3"]):
        error_msg = "Kritik komutlar (apt-get, git, pip3) bulunamadı. Betik durduruluyor."
        logging.critical(error_msg)
        print(f"{Colors.FAIL}{error_msg}{Colors.ENDC}")
        sys.exit(1)

    os.environ['DEBIAN_FRONTEND'] = 'noninteractive'

    print_header("Aşama 1: Sistem Güncelleniyor")
    if not run_command("apt-get update"): sys.exit(1)
    if not run_command("apt-get full-upgrade -y"): sys.exit(1)

    print_header("Aşama 2: Temel Geliştirici Paketleri Kuruluyor")
    apt_packages = [
        "build-essential",
        "git",
        "curl",
        "wget",
        "python3-pip",
        "python3-venv",
        "htop",
        "net-tools",
        "libgfortran5",
        "libatlas-base-dev",
        "liblapack-dev",
        "python3-dev"
    ]
    if not run_command(f"apt-get install -y {' '.join(apt_packages)}"): sys.exit(1)
    
    print_header("Aşama 3: Gerekli Python (pip) Paketleri Kuruluyor")
    pip_packages = [
        "requests",
        "beautifulsoup4",
        "scapy",
        "pwntools",
        "colorama"
    ]
    if not run_command(f"pip3 install --upgrade pip"): sys.exit(1)
    if not run_command(f"pip3 install {' '.join(pip_packages)} --break-system-packages"): sys.exit(1)

    print_header("Aşama 4: Örnek GitHub Kütüphaneleri Klonlanıyor")
    tools_dir = Path("/opt/tools")
    tools_dir.mkdir(exist_ok=True)
    
    git_repos = {
        "https://github.com/carlospolop/PEASS-ng.git": "PEASS-ng",
        "https://github.com/SecureAuthCorp/impacket.git": "impacket",
    }
    
    for url, name in git_repos.items():
        dest_path = tools_dir / name
        if not dest_path.exists():
            if not run_command(f"git clone {url} {dest_path}"):
                logging.warning(f"{name} klonlanamadı. Devam ediliyor.")
        else:
            logging.warning(f"Dizin zaten mevcut, klonlama atlanıyor: {dest_path}")
            print(f"{Colors.WARNING}Uyarı: Dizin zaten mevcut, atlanıyor: {dest_path}{Colors.ENDC}")

    print_header("Aşama 5: Sistem Temizliği")
    if not run_command("apt-get autoremove -y"): sys.exit(1)
    if not run_command("apt-get clean"): sys.exit(1)

    print_header("MİNİMAL GELİŞTİRİCİ ORTAMI KURULUMU TAMAMLANDI!")
    logging.info("Tüm işlemler başarıyla tamamlandı.")
    print(f"{Colors.OKGREEN}{Colors.BOLD}Sisteminiz güncellendi ve GitHub projelerini denemek için hazır.{Colors.ENDC}")
    print(f"{Colors.OKCYAN}Örnek kütüphaneleri şurada bulabilirsiniz: '{tools_dir}'{Colors.ENDC}")
    print(f"{Colors.WARNING}İhtiyaç duyduğunuz özel bir aracı (örn: nmap) 'sudo apt-get install nmap' komutuyla manuel olarak kurabilirsiniz.{Colors.ENDC}")

if __name__ == "__main__":
    main()
