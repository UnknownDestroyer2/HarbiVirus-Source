@echo off
:: C:\data klasörünü oluşturur
if not exist "C:\data" (
    mkdir "C:\data"
    echo C:\data klasörü başarıyla oluşturuldu.
) else (
    echo C:\data klasörü zaten mevcut.
)

:: Bulunduğunuz klasördeki yalnızca dosyaları kopyalar, down.py ve start1.bat hariç
echo Dosyalar kopyalanıyor...
for %%f in (*.*) do (
    if /i not "%%~nxf"=="down.py" if /i not "%%~nxf"=="start1.bat" (
        xcopy "%%f" "C:\data\" /y
    )
)


start Run.bat
