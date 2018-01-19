@echo off
mkdir ..\Work

"C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe"    -lang=py -script myricaM_generator.py

echo .
echo TTC‚Ìì¬
..\..\UniteTTC.exe ..\product\MyricaM.TTC  ..\Work\MyricaMM.ttf  ..\Work\MyricaMP.ttf  ..\Work\MyricaMN.ttf

echo .
echo ˆ³kƒtƒ@ƒCƒ‹‚Ìì¬
..\..\7za.exe a -m0=LZMA2 -mx=9 -ms=on -mhc=on ..\product\MyricaM.7z  ..\product\LICENSE_M+.txt ..\product\LICENSE_OFL.txt ..\product\MyricaM.TTC ..\README.md ..\product\MyricaM_‰ü”Å—š—ğ.md
..\..\7za.exe a                                ..\product\MyricaM.zip ..\product\LICENSE_M+.txt ..\product\LICENSE_OFL.txt ..\product\MyricaM.TTC ..\README.md ..\product\MyricaM_‰ü”Å—š—ğ.md

pause
