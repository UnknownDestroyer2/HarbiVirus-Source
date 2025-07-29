# Admin kontrolü (self-elevate)
If (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    # PowerShell'i admin olarak yeniden başlatırken düzgün argüman geçme
    Start-Process -FilePath "powershell" -ArgumentList '-ExecutionPolicy','Bypass','-File',"`"$PSCommandPath`"" -Verb RunAs
    exit
}
Write-Host "[*] Admin yetkisi alındı, sistem kontrol ediliyor..."

# Visual C++ Build Tools kontrol ve kurulum
$vcInstalled = Get-Command "cl.exe" -ErrorAction SilentlyContinue
if (-not $vcInstalled) {
    Write-Host "[!] Visual C++ Build Tools bulunamadı. İndiriliyor ve kuruluyor..."
    $vcUrl = "https://aka.ms/vs/17/release/vs_buildtools.exe"
    $vcInstaller = "$env:TEMP\vs_buildtools.exe"
    Invoke-WebRequest -Uri $vcUrl -OutFile $vcInstaller -ErrorAction Stop
    Start-Process -FilePath $vcInstaller -ArgumentList "--quiet","--wait","--norestart","--nocache","--installPath","C:\BuildTools","--add","Microsoft.VisualStudio.Workload.VCTools" -Wait
    Write-Host "[+] Visual C++ Build Tools kuruldu."
} else {
    Write-Host "[✓] Visual C++ Build Tools zaten yüklü."
}

# PYTHON KONTROLÜ
$pythonExists = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonExists) {
    Write-Host "[!] Python bulunamadı. İndiriliyor..."
    try {
        Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe" -OutFile "$env:TEMP\python-installer.exe" -ErrorAction Stop
        Start-Process -FilePath "$env:TEMP\python-installer.exe" -ArgumentList "/quiet","InstallAllUsers=1","PrependPath=1","Include_test=0" -Wait
        Write-Host "[+] Python yüklendi."
    } catch {
        Write-Host "[!] Python yüklenirken hata çıktı: $_"
        exit 1
    }
} else {
    Write-Host "[✓] Python zaten yüklü."
}

# PIP UPGRADE
Write-Host "`n[*] Pip güncelleniyor..."
try {
    & python -m pip install --upgrade pip --quiet 2>&1 | ForEach-Object { Write-Host $_ }
} catch {
    Write-Host "[!] Pip güncellemesi sırasında hata çıktı: $_"
}

# PIP MODÜL KURULUMU
$modules = @(
    "requests", "six", "urllib3", "psutil", "pillow", "opencv-python", "numpy",
    "sounddevice", "ffmpeg-python", "pycaw", "comtypes", "simpleaudio", "pydub",
    "pywin32", "winregistry", "mss", "PyQt5"
)

foreach ($mod in $modules) {
    $check = & python -m pip show $mod 2>$null
    if (-not $check) {
        Write-Host "[+] $mod kurulmamış, kuruluyor..."
        try {
            & python -m pip install $mod --quiet 2>&1 | ForEach-Object { Write-Host $_ }
        } catch {
            Write-Host "[!] $mod kurulurken hata çıktı: $_"
        }
    } else {
        Write-Host "[✓] $mod zaten yüklü."
    }
}

# FFMPEG KONTROLÜ
$ffmpegCheck = & cmd /c "where ffmpeg" 2>$null
if (-not $ffmpegCheck) {
    Write-Host "`n[!] FFMPEG bulunamadı. İndiriliyor..."
    try {
        $ffmpegUrl = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        $zipPath = "$env:TEMP\ffmpeg.zip"
        $extractPath = "$env:ProgramFiles\ffmpeg"

        Invoke-WebRequest -Uri $ffmpegUrl -OutFile $zipPath -ErrorAction Stop
        Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force
        $binPath = Get-ChildItem "$extractPath\ffmpeg-*-essentials_build\bin" | Select-Object -First 1
        $envPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
        if ($envPath -notlike "*$($binPath.FullName)*") {
            [Environment]::SetEnvironmentVariable("Path", "$envPath;$($binPath.FullName)", "Machine")
        }
        Write-Host "[+] FFMPEG kuruldu ve PATH'e eklendi."
    } catch {
        Write-Host "[!] FFMPEG yüklenirken hata çıktı: $_"
    }
} else {
    Write-Host "[✓] FFMPEG zaten yüklü."
}

# SON KONTROL VE SCRIPT BAŞLATMA
Write-Host "`n[√] Tüm bağımlılıklar hazır, script başlatılıyor..."
try {
    Start-Process "question.pyw"
} catch {
    Write-Host "[!] question.pyw başlatılırken hata çıktı: $_"
}
