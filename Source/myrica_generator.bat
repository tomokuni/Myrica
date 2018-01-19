@echo off
mkdir ..\Work

"C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe"  -lang=py -script myrica_generator.py

echo .
echo TTC‚Ìì¬
..\..\UniteTTC.exe ..\product\Myrica.TTC  ..\Work\MyricaM.ttf  ..\Work\MyricaP.ttf  ..\Work\MyricaN.ttf

echo .
echo ˆ³kƒtƒ@ƒCƒ‹‚Ìì¬
..\..\7za.exe a -m0=LZMA2 -mx=9 -ms=on -mhc=on ..\product\Myrica.7z  ..\product\LICENSE_M+.txt ..\product\LICENSE_OFL.txt ..\product\Myrica.TTC ..\README.md ..\product\Myrica_‰ü”Å—š—ğ.md
..\..\7za.exe a                                ..\product\Myrica.zip ..\product\LICENSE_M+.txt ..\product\LICENSE_OFL.txt ..\product\Myrica.TTC ..\README.md ..\product\Myrica_‰ü”Å—š—ğ.md

pause
