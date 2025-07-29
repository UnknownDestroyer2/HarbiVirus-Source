@echo off
color a
cls
echo Do you really want to run this virus? Y/N
set /p choice=Choice: 

if /i "%choice%"=="Y" (
    call HarbiVirus.bat
    color 04
    
) else if /i "%choice%"=="N" (
    color a1
    timeout 1
    cls
    color b1
    timeout 1
    cls
    color c2
    timeout 1
    cls
    color 53
    timeout 1
    cls
    color 14
    timeout 1
    cls
    color 04
    timeout 1
    cls
    cls
    echo Goodbye
    echo Press Enter to leave.   
    pause >nul
    
    exit
) else (
    echo Invalid choice. Please enter Y or N next time!
    timeout 3
    exit
)
