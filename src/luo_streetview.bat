@echo off
setlocal

:: --- ASETUKSET ---
set VIDEO_FILE=video.mp4
set OUTPUT_DIR=street_view_projekti
set "DEFAULT_INTERVAL=2"
:: -----------------

echo.
echo ========================================
echo  GoPro Street View Automaatio
echo ========================================
echo.

:: UUSI OSA: Kysytaan kuvavali kayttajalta
echo Syota kuvien otantavali sekunteina.
set /p FRAME_INTERVAL="Vali (oletus on %DEFAULT_INTERVAL%): "

:: UUSI OSA: Jos kayttaja ei syota mitaan, kaytetaan oletusarvoa
if not defined FRAME_INTERVAL set "FRAME_INTERVAL=%DEFAULT_INTERVAL%"

echo.

:: Tarkista riippuvuudet
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo VIRHE: FFmpeg ei loytynyt. Asenna se ja lisaa se PATH-ymparistomuuttujaan.
    goto :eof
)
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo VIRHE: Python ei loytynyt. Asenna Python 3.
    goto :eof
)

:: MUOKATTU: Asetukset naytetaan sen jalkeen, kun kayttaja on antanut arvon
echo Kaytetaan asetuksia:
echo   - Video: %VIDEO_FILE%
echo   - Kuvavali: %FRAME_INTERVAL% sekuntia
echo   - Tuloshakemisto: %OUTPUT_DIR%
echo.

:: Tyhjenna ja luo tuloshakemisto
if exist "%OUTPUT_DIR%" (
    echo Poistetaan vanha tuloshakemisto...
    rmdir /s /q "%OUTPUT_DIR%"
)
mkdir "%OUTPUT_DIR%"
mkdir "%OUTPUT_DIR%\frames"

:: 1. Pilko video kuviksi FFmpeg:lla
echo Vaihe 1/3: Pilkotaan videota kuviksi...
ffmpeg -i "%VIDEO_FILE%" -vf "fps=1/%FRAME_INTERVAL%" -hide_banner -loglevel error "%OUTPUT_DIR%\frames\frame_%%04d.jpg"
if %errorlevel% neq 0 (
    echo VIRHE: FFmpeg epaonnistui kuvien luomisessa.
    goto :eof
)
echo Valmis.

:: 2. Prosessoi data Pythonilla
echo Vaihe 2/3: Yhdistetaan sijaintidata ja lasketaan suuntimat (yaw)...
python prosessoi_data.py --video "%VIDEO_FILE%" --interval %FRAME_INTERVAL% --outputdir "%OUTPUT_DIR%"
if %errorlevel% neq 0 (
    echo VIRHE: Python-skripti epaonnistui.
    goto :eof
)
echo Valmis.

:: 3. Kopioi web-tiedostot
echo Vaihe 3/3: Kopioidaan web-tiedostot tuloshakemistoon...
copy index.html "%OUTPUT_DIR%\index.html" >nul
copy arrow-forward.svg "%OUTPUT_DIR%\arrow-forward.svg" >nul
copy arrow-backward.svg "%OUTPUT_DIR%\arrow-backward.svg" >nul
echo Valmis.

echo.
echo ==========================================================
echo  PROSESSI VALMIS!
echo  Avaa tiedosto "%OUTPUT_DIR%\index.html" selaimessasi.
echo ==========================================================
echo.

endlocal
