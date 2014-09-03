#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Author: Tomokuni SEKIYA
#
# This script is for generating ``myrica'' font
#
# * Inconsolata : Inconsolata-Regular.ttf : 1.013 (Google Fonts)
# * (original)  : ReplaceParts.ttf        : 1.000.20140825
# * Mgen+       : mgenplus-1m-regular.ttf : 1.058.20140808 (20140828)
# * Migu        : migu-1m-regular.ttf     : 2013.0617 (20130617)
#
#以下のように構成されます。
#・英数字記号は、Inconsolata-Regular.ttf と ReplaceParts.ttf
#・他の文字は、mgenplus-1m-regular.ttf
#・一部の文字は、circle-mplus-1m-regular.ttf
#    対象：・半濁点（ぱぴぷぺぽパピプペポ の右上の円）を大きくして、濁点と判別しやすく
#          ・「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別
#          ・～〜（FULLWIDTH TILDE・WAVE DASH）の区別
#          ・αβなど一部のギリシャ文字、φЯなど一部のロシア文字を全角に
#          ・×÷±などの数学記号を全角に
#

# version
newfont_version      = "1.002.20140903"
newfont_sfntRevision = 0x00010000

# flag
scalingDownIfWidth_flag = True

# set font name
newfontM  = ("../../MyricaSourceTTF/MyricaM.ttf",   "MyricaM",  "Myrica M",  "Myrica Monospace")
newfontP  = ("../../MyricaSourceTTF/MyricaP.ttf",   "MyricaP",  "Myrica P",  "Myrica Proportional")
newfontN  = ("../../MyricaSourceTTF/MyricaN.ttf",   "MyricaN",  "Myrica N",  "Myrica Narrow")

#newfontHM = ("../../MyricaSourceTTF/MyricaHMs.ttf", "MyricaHM", "MyricaH M", "MyricaH Monospace")
#newfontHP = ("../../MyricaSourceTTF/MyricaHPs.ttf", "MyricaHP", "MyricaH P", "MyricaH Proportional")
#newfontHN = ("../../MyricaSourceTTF/MyricaHNs.ttf", "MyricaHN", "MyricaH N", "MyricaH Narrow")

# set ascent and descent (line width parameters)
newfont_ascent  = 840
newfont_descent = 184
newfont_em = newfont_ascent + newfont_descent

# source file
srcfontIncosolata   = "../../MyricaSourceTTF/Inconsolata-Regular.ttf"
srcfontMgenplus     = "../../MyricaSourceTTF/mgenplus-1m-regular.ttf"
srcfontMigu         = "../../MyricaSourceTTF/migu-1m-regular.ttf"
srcfontReplaceParts = "ReplaceParts.ttf"

# define
generate_flags = ('opentype', 'PfEd-lookups', 'TeX-table')
panoseBase = (2, 11, 5, 9, 2, 2, 3, 2, 2, 7)

########################################
# setting
########################################

import copy
import os
import sys
import fontforge
import psMat

# 縦書きのために指定する
fontforge.setPrefs('CoverageFormatsAllowed', 1)
# 大変更時に命令を消去 0:オフ 1:オン
fontforge.setPrefs('ClearInstrsBigChanges', 0)
# TrueType命令をコピー 0:オフ 1:オン
fontforge.setPrefs('CopyTTFInstrs', 1)

########################################
# pre-process
########################################

print 
print 
print "myrica generator " + newfont_version
print 
print "This script is for generating 'myrica' font"
print 
if os.path.exists( srcfontIncosolata ) == False:
    print "Error: " + srcfontIncosolata + " not found"
    sys.exit( 1 )
if os.path.exists( srcfontReplaceParts ) == False:
    print "Error: " + srcfontReplaceParts + " not found"
    sys.exit( 1 )
if os.path.exists( srcfontMgenplus ) == False:
    print "Error: " + srcfontMgenplus + " not found"
    sys.exit( 1 )
if os.path.exists( srcfontMigu ) == False:
    print "Error: " + srcfontMigu + " not found"
    sys.exit( 1 )

########################################
# define function
########################################
def matRescale(origin_x, origin_y, scale_x, scale_y):
    return psMat.compose(
        psMat.translate(-origin_x, -origin_y), psMat.compose(
        psMat.scale(scale_x, scale_y), 
        psMat.translate(origin_x, origin_y)))

def matMove(move_x, move_y):
    return psMat.translate(move_x, move_y)

def flatten(iterable):
    it = iter(iterable)
    for e in it:
        if isinstance(e, (list, tuple)):
            for f in flatten(e):
                yield f
        else:
            yield e

def rng(start, end):
    return range(start, end + 1)

def scalingDownIfWidth(font, if_width):
    for glyph in font.glyphs():
        if glyph.width == if_width:
            glyph.transform(matRescale(if_width / 2, 0, 0.91, 0.91))
            glyph.width = if_width

def copyAndPaste(srcFont, srcCodes, dstFont, dstCodes):
    select(srcFont, srcCodes)
    srcFont.copy()
    select(dstFont, dstCodes)
    dstFont.paste()

def copyAndPasteInto(srcFont, srcCodes, dstFont, dstCodes, pos_x, pos_y):
    select(srcFont, srcCodes)
    srcFont.copy()
    select(dstFont, dstCodes)
    dstFont.transform(matMove(-pos_x, -pos_y))
    dstFont.pasteInto()
    dstFont.transform(matMove(pos_x, pos_y))

def select(font, *codes):
    font.selection.none()
    selectMore(font, codes)

def selectMore(font, *codes):
    flat = flatten(codes)
    for c in flat:
        font.selection.select(("more",), c)

def centerInWidth(font):
    for glyph in font.selection.byGlyphs:
        w  = glyph.width
        wc = w / 2
        bb = glyph.boundingBox()
        bc = (bb[0] + bb[2]) / 2
        glyph.transform(matMove(wc - bc, 0))
        glyph.width = w

def setWidth(font, width):
    for glyph in font.selection.byGlyphs:
        glyph.width = width

def setAutoWidthGlyph(glyph, separation):
    bb = glyph.boundingBox()
    bc = (bb[0] + bb[2]) / 2
    nw = (bb[2] - bb[0]) + separation * 2
    wc = nw / 2
    glyph.transform(matMove(wc - bc, 0))
    glyph.width = nw

########################################
# modified Inconsolata
########################################

print
print "Open " + srcfontIncosolata
fIn = fontforge.open( srcfontIncosolata )

# modify
print "modify"
# 拡大 "'`
select(fIn, 0x0022, 0x0027, 0x0060)
fIn.transform(matRescale(250, 600, 1.15, 1.15))
setWidth(fIn, 1000 / 2)

# 拡大 ,.:;
select(fIn, 0x002c, 0x002e, 0x003a, 0x003b)
fIn.transform(matRescale(250, 0, 1.15, 1.15))
setWidth(fIn, 1000 / 2)

# 移動 +-<>=
select(fIn, 0x002b, 0x002d, 0x003c, 0x003e, 0x003d)
fIn.transform(matMove(0, -80))
setWidth(fIn, 1000 / 2)

# 移動 ~
select(fIn, 0x007e)
fIn.transform(matMove(0, 120))

# 移動 ()
select(fIn, 0x0028, 0x0029)
fIn.transform(matMove(0, 78))

# 移動 []
select(fIn, 0x005b, 0x005d)
fIn.transform(matMove(0, 44))

# 移動 {}
select(fIn, 0x007b, 0x007d)
fIn.transform(matMove(0, 99))

# | -> broken | (Inconsolata's glyph)
copyAndPaste(fIn, 0x00a6, fIn, 0x007c)

# D -> D of Eth (D with cross-bar)
copyAndPaste(fIn, 0x0110, fIn, 0x0044)

# r -> r of serif (Inconsolata's unused glyph)
copyAndPaste(fIn,  65548, fIn, 0x0072)

# 必要文字(半角英数字記号)だけを残して削除 # 
select(fIn, rng(0x0021, 0x007E))
fIn.selection.invert()
fIn.clear()

# modify em
fIn.em  = newfont_em
fIn.ascent  = newfont_ascent
fIn.descent = newfont_descent

setWidth(fIn, newfont_em / 2)

#fIn.generate("/modIncosolata.ttf", '', generate_flags)

########################################
# modified ReplaceParts
########################################

print
print "Open " + srcfontReplaceParts
fPa = fontforge.open( srcfontReplaceParts )

# modify em
fPa.em  = newfont_em
fPa.ascent  = newfont_ascent
fPa.descent = newfont_descent

# post-process
fPa.selection.all()
fPa.round()

#fPa.generate("/modReplaceParts.ttf", '', generate_flags)

########################################
# modified Mgen+ 1m
########################################

print
print "Open " + srcfontMgenplus
fMg = fontforge.open( srcfontMgenplus )

## modify em
#fMg.em  = newfont_em
#fMg.ascent  = newfont_ascent
#fMg.descent = newfont_descent
#
#fMg.generate("/modMgenplus.ttf", '', generate_flags)

########################################
# modified Migu 1m
########################################

print
print "Open " + srcfontMigu
fMi = fontforge.open( srcfontMigu )

# modify em
fMi.em  = newfont_em
fMi.ascent  = newfont_ascent
fMi.descent = newfont_descent

#fMi.generate("/modMigu.ttf", '', generate_flags)

########################################
# create MyricaM
########################################
fRm = fIn

print
print "Build " + newfontM[0]

# pre-process
fRm.fontname   = newfontM[1]
fRm.familyname = newfontM[2]
fRm.fullname   = newfontM[3]
fRm.weight = "Book"
fRm.copyright =  "Copyright (c) 2006-2012 Raph Levien (Inconsolata)\n"
fRm.copyright += "Copyright (c) 2013 itouhiro (Circle M+)\n"
fRm.copyright += "Copyright (c) 2013 M+ FONTS PROJECT (M+)\n"
fRm.copyright += "Copyright (c) 2014 MM (Mgen+)\n"
fRm.copyright += "Copyright (c) 2014 Adobe Systems Incorporated. (NotoSansJP)\n"
fRm.copyright += "Licenses:\n"
fRm.copyright += "SIL Open Font License Version 1.1 "
fRm.copyright += "(http://scripts.sil.org/ofl)\n"
fRm.copyright += "Apache License, Version 2.0 "
fRm.copyright += "(http://www.apache.org/licenses/LICENSE-2.0)"
fRm.version = newfont_version
fRm.sfntRevision = newfont_sfntRevision
fRm.sfnt_names = (('English (US)', 'UniqueID', newfontM[2]), )
fRm.head_optimized_for_cleartype = True

fRm.os2_panose = panoseBase
fRm.os2_vendor = fMg.os2_vendor
fRm.os2_version = 1

fRm.os2_winascent = newfont_ascent
fRm.os2_winascent_add = 0
fRm.os2_windescent = newfont_descent
fRm.os2_windescent_add = 0
fRm.os2_typoascent = newfont_ascent
fRm.os2_typoascent_add = 0
fRm.os2_typodescent = -newfont_descent
fRm.os2_typodescent_add = 0
fRm.os2_typolinegap
fRm.hhea_ascent = newfont_ascent
fRm.hhea_ascent_add = 0
fRm.hhea_descent = -newfont_descent
fRm.hhea_descent_add = 0
fRm.hhea_linegap = 0

# marge ReplaceParts
print "marge ReplaceParts"
target = (
    0x002a,  # * : astarisk
    0x0030,  # 0 : zero
    0x006c,  # l : small letter l
    0x2013,  # – : en dash –
    0x2014)  # — : em dash —
copyAndPaste(fPa, target, fRm, target)

# marge Mgen+ 1m
print "marge Mgen+ 1m"
fRm.mergeFonts( srcfontMgenplus )
fRm.os2_unicoderanges = fMg.os2_unicoderanges
fRm.os2_codepages = fMg.os2_codepages
for l in fMg.gsub_lookups:
    if (l in fRm.gsub_lookups) == False:
        fRm.importLookups(fMg, l)
for l in fRm.gsub_lookups:
    if l.startswith(fMg.fontname + "-") == True:
        fRm.removeLookup(l)

# marge Migu 1m
print "marge Migu 1m"
target = (
    # 半濁点（ぱぴぷぺぽパピプペポ の右上の円）を大きくして、濁点と判別しやすく
    (0x3071, 0x3074, 0x3077, 0x307A, 0x307D, 0x30D1, 0x30D4, 0x30D7, 0x30DA, 0x30DD),
    # 「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別
    (0x30AB, 0x529B, 0x30A8, 0x5DE5, 0x30ED, 0x53E3, 0x30FC, 0x4E00, 0x30CB, 0x4E8C),
    # ～〜（FULLWIDTH TILDE・WAVE DASH）の区別
    (0xFF5E, 0x301C),
    # αβなど一部のギリシャ文字、φЯなど一部のロシア文字を全角に
    (rng(0x0391, 0x03a9), rng(0x03b1, 0x03c9)),
    (0x0401, rng(0x0410, 0x044F), 0x0451))
copyAndPaste(fMi, target, fRm, target)

# modify
print "modify"

# scaling down
if scalingDownIfWidth_flag == True:
    print "While scaling, wait a little..."
    scalingDownIfWidth(fRm, newfont_em)


# 全角 comma and period ，．
select(fRm, 0xff0c, 0xff0e)
fRm.transform(matMove(280, 0))
fRm.transform(matRescale(512, 0, 1.54, 1.54))
setWidth(fRm, newfont_em)

# 全角 colon and semicolon ：；
copyAndPaste    (fRm, 0xff0c, fRm, 0xff1b)
copyAndPasteInto(fRm, 0xff0e, fRm, 0xff1b, 0, 410)
copyAndPaste    (fRm, 0xff0e, fRm, 0xff1a)
copyAndPasteInto(fRm, 0xff0e, fRm, 0xff1a, 0, 410)
select(fRm, 0xff1b, 0xff1a)

# 全角 brackets （）［］｛｝＜＞
srcTarget = (0x0028, 0x0029, 0x005b, 0x005d, 0x007b, 0x007d, 0x003c, 0x003e)
dstTarget = (0xff08, 0xff09, 0xff3b, 0xff3d, 0xff5b, 0xff5d, 0xff1c, 0xff1e)
copyAndPaste(fRm, srcTarget, fRm, dstTarget)
fRm.transform(matMove(256, 0))
setWidth(fRm, newfont_em)

# post-process
fRm.selection.all()
fRm.round()

print "Generate " + newfontM[0]
fRm.generate(newfontM[0], '', generate_flags)

#print "Generate " + newfontHM[0]
#fRm.fontname   = newfontHM[1]
#fRm.familyname = newfontHM[2]
#fRm.fullname   = newfontHM[3]
#fRm.sfnt_names = (('English (US)', 'UniqueID', newfontHM[2]), )
#fRm.generate(newfontHM[0], '', generate_flags)

fPa.close()
fMg.close()
fMi.close()

########################################
# create MyricaP
########################################
print
print "Build " + newfontP[0]
fRp = fontforge.open( newfontM[0] )

# pre-process
fRp.fontname   = newfontP[1]
fRp.familyname = newfontP[2]
fRp.fullname   = newfontP[3]
fRp.sfnt_names = (('English (US)', 'UniqueID', newfontP[2]), )

panose = list(fRp.os2_panose)
panose[3] = 0
fRp.os2_panose = tuple(panose)

# modify
print "modify"

# 半角
hankaku = (100,)
# 全角
zenkaku = (50,)

# 全文字の幅の自動設定
fRp.selection.all()
for glyph in fRp.selection.byGlyphs:
    #print glyph.glyphname + ", code " + str(glyph.unicode) + ", width " + str(glyph.width)
    if glyph.width == newfont_em:         # 全角文字
        setAutoWidthGlyph(glyph, hankaku[0])
    else:                                 # 半角文字
        bb = glyph.boundingBox()
        nw = (bb[2] - bb[0]) + zenkaku[0] * 2
        if glyph.width > nw:
            setAutoWidthGlyph(glyph, zenkaku[0])

# 半角数字は幅固定で中央配置
select(fRp, rng(0x0030,0x0039))   # 0-9
setWidth(fRp, 490)
centerInWidth(fRp)

# post-process
fRp.selection.all()
fRp.round()

print "Generate " + newfontP[0]
fRp.generate(newfontP[0], '', generate_flags)

#print "Generate " + newfontHP[0]
#fRp.fontname   = newfontHP[1]
#fRp.familyname = newfontHP[2]
#fRp.fullname   = newfontHP[3]
#fRp.sfnt_names = (('English (US)', 'UniqueID', newfontHP[2]), )
#fRp.generate(newfontHP[0], '', generate_flags)

fRp.close()

########################################
# create MyricaN
########################################
print
print "Build " + newfontN[0]
fRn = fontforge.open( newfontM[0] )

# pre-process
fRn.fontname   = newfontN[1]
fRn.familyname = newfontN[2]
fRn.fullname   = newfontN[3]
fRn.sfnt_names = (('English (US)', 'UniqueID', newfontN[2]), )

panose = list(fRn.os2_panose)
panose[3] = 0
fRn.os2_panose = tuple(panose)

# modify
print "modify"

# 半角英数
heisu = (0.85, 1.00, 50, (rng(0x0030,0x0039), rng(0x0041,0x005A), rng(0x0061,0x007A)))
# 半角記号
hkigo = (0.85, 1.00, 50, (rng(0x0021,0x002F), rng(0x003A,0x0040), rng(0x005B,0x0060), rng(0x007B,0x007E)))
# 全角かな
zkana = (0.50, 1.00, 50, rng(0x3041,0x31FF))
# 半角かな
hkana = (0.85, 1.00, 50, rng(0xFF66,0xFF9F))
# その他の全角文字
zetc  = (0.60, 1.00, 50)
# その他の半角文字
hetc  = (0.85, 1.00, 50)

# 拡大縮小 と 幅の自動設定
fRn.selection.all()
for glyph in fRn.selection.byGlyphs:
    #print glyph.glyphname + ", code " + str(glyph.unicode) + ", width " + str(glyph.width)
    glyph.ttinstrs = ""
    if glyph.unicode in zkana[3]:           # 全角かな
        glyph.transform(matRescale(0, 0, zkana[0], zkana[1]))
        setAutoWidthGlyph(glyph, zkana[2])
    elif glyph.width == newfont_em:         # その他の全角文字
        glyph.transform(matRescale(0, 0, zetc[0],  zetc[1]))
        setAutoWidthGlyph(glyph, zetc[2])
    else:                                   # 半角文字
        glyph.transform(matRescale(0, 0, hetc[0],  hetc[1]))
        bb = glyph.boundingBox()
        nw = (bb[2] - bb[0]) + hetc[2] * 2
        if glyph.width > nw:
            setAutoWidthGlyph(glyph, hetc[2])

# 半角数字は幅固定で中央配置
select(fRn, rng(0x0030,0x0039))   # 0-9
setWidth(fRn, 400)
centerInWidth(fRn)

# post-process
fRn.selection.all()
fRn.round()

print "Generate " + newfontN[0]
fRn.generate(newfontN[0], '', generate_flags)

#print "Generate " + newfontHN[0]
#fRn.fontname   = newfontHN[1]
#fRn.familyname = newfontHN[2]
#fRn.fullname   = newfontHN[3]
#fRn.sfnt_names = (('English (US)', 'UniqueID', newfontHN[2]), )
#fRn.generate(newfontHN[0], '', generate_flags)

fRn.close()
