@echo off
set PATH=%~dp0..\..\cygwin\bin;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\system32\Wbem
set CYGWIN=nodosfilewarning
set HOME=%~dp0
set LANG=C.UTF-8
set TZ=
set DISPLAY=:9.0
set AUTOTRACE=potrace

del ..\..\MyricaSourceTTF\MyricaM.ttf
del ..\..\MyricaSourceTTF\MyricaP.ttf
del ..\..\MyricaSourceTTF\MyricaN.ttf

start /B XWin.exe :9 -multiwindow -nomultimonitors -silent-dup-error

xwin-close.exe -wait
fontforge.exe  -lang=py -script myrica_generator.py
xwin-close.exe -close

echo .
echo TTC�̍쐬
..\..\UniteTTC.exe ..\Myrica.TTC  ..\..\MyricaSourceTTF\MyricaM.ttf  ..\..\MyricaSourceTTF\MyricaP.ttf  ..\..\MyricaSourceTTF\MyricaN.ttf
pause
