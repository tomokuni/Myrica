@echo off
set PATH=%~dp0..\..\cygwin\bin;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\system32\Wbem
set CYGWIN=nodosfilewarning
set HOME=%~dp0
set LANG=C.UTF-8
set TZ=
set DISPLAY=:9.0
set AUTOTRACE=potrace

start /B XWin.exe :9 -multiwindow -nomultimonitors -silent-dup-error

del ..\..\MyricaSourceTTF\Myrica*.*

xwin-close.exe -wait
fontforge.exe  -lang=py -script myrica_generator.py
xwin-close.exe -close

rem echo .
rem echo ÉqÉìÉeÉBÉìÉO
rem ..\..\ttfautohint.exe --hinting-range-min=8 --hinting-range-max=50 --default-script=latn --hinting-limit=200 --increase-x-height=14 --no-info --strong-stem-width=GD ..\..\MyricaSourceTTF\MyricaHMs.ttf ..\..\MyricaSourceTTF\MyricaHM.ttf
rem ..\..\ttfautohint.exe --hinting-range-min=8 --hinting-range-max=50 --default-script=latn --hinting-limit=200 --increase-x-height=14 --no-info --strong-stem-width=GD ..\..\MyricaSourceTTF\MyricaHPs.ttf ..\..\MyricaSourceTTF\MyricaHP.ttf
rem ..\..\ttfautohint.exe --hinting-range-min=8 --hinting-range-max=50 --default-script=latn --hinting-limit=200 --increase-x-height=14 --no-info --strong-stem-width=GD ..\..\MyricaSourceTTF\MyricaHNs.ttf ..\..\MyricaSourceTTF\MyricaHN.ttf
rem del ..\..\MyricaSourceTTF\MyricaH*s.*

echo .
echo TTCÇÃçÏê¨
..\..\UniteTTC.exe ..\Myrica.TTC  ..\..\MyricaSourceTTF\MyricaM.ttf  ..\..\MyricaSourceTTF\MyricaP.ttf  ..\..\MyricaSourceTTF\MyricaN.ttf
rem ..\..\UniteTTC.exe ..\MyricaH.TTC ..\..\MyricaSourceTTF\MyricaHM.ttf ..\..\MyricaSourceTTF\MyricaHP.ttf ..\..\MyricaSourceTTF\MyricaHN.ttf
pause
