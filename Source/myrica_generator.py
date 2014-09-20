#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Author: Tomokuni SEKIYA
#
# This script is for generating ``myrica'' font
#
# * Inconsolata : Inconsolata-Regular.ttf : 1.013 (Google Fonts)
# * (original)  : ReplaceParts.ttf        : 1.005.20140905
# * Mgen+       : mgenplus-1m-regular.ttf : 1.058.20140808 (20140828)
# * Migu        : migu-1m-regular.ttf     : 2013.0617 (20130617)
#
#基本的には以下のように構成されます。
#・英数字記号は、Inconsolata-Regular.ttf 
#・他の文字は、mgenplus-1m-regular.ttf
#・一部の漢字(力工口一二)を除くJIS208/JIS213の文字は、circle-mplus-1m-regular.ttf 由来の文字に置換え
#    目的：・半濁点（ぱぴぷぺぽパピプペポ の右上の円）を大きくして、濁点と判別しやすく
#          ・「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別
#          ・～〜（FULLWIDTH TILDE・WAVE DASH）の区別
#          ・αβなど一部のギリシャ文字、φЯなど一部のキリル文字を全角に
#          ・±×÷√‰§†‡¶などの記号を全角に
#

# version
newfont_version      = "1.009.20140920"
newfont_sfntRevision = 0x00010000

# flag
scalingDownIfWidth_flag = True

# set font name
newfontM  = ("../../MyricaSourceTTF/MyricaM.ttf", "MyricaM", "Myrica M", "Myrica Monospace")
newfontP  = ("../../MyricaSourceTTF/MyricaP.ttf", "MyricaP", "Myrica P", "Myrica Proportional")
newfontN  = ("../../MyricaSourceTTF/MyricaN.ttf", "MyricaN", "Myrica N", "Myrica Narrow")

# set ascent and descent (line width parameters)
newfont_ascent  = 840
newfont_descent = 184
newfont_em = newfont_ascent + newfont_descent

newfont_winAscent   = 840
newfont_winDescent  = 170
newfont_typoAscent  = newfont_winAscent
newfont_typoDescent = -newfont_winDescent
newfont_typoLinegap = 0
newfont_hheaAscent  = newfont_winAscent
newfont_hheaDescent = -newfont_winDescent
newfont_hheaLinegap = 0

# source file
srcfontIncosolata   = "../../MyricaSourceTTF/Inconsolata-Regular.ttf"
srcfontMgenplus     = "../../MyricaSourceTTF/mgenplus-1m-regular.ttf"
srcfontMigu         = "../../MyricaSourceTTF/migu-1m-regular.ttf"
srcfontReplaceParts = "ReplaceParts.ttf"
srcfontHintingParts = "HintingParts.ttf"

# define
generate_flags = ('opentype', 'PfEd-lookups', 'TeX-table')
panoseBase = (2, 11, 5, 9, 2, 2, 3, 2, 2, 7)

########################################
# setting
########################################

import copy
import os
import sys
import shutil
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

def rng(start, end):
    return range(start, end + 1)

def flatten(iterable):
    it = iter(iterable)
    for e in it:
        if isinstance(e, (list, tuple)):
            for f in flatten(e):
                yield f
        else:
            yield e

def select(font, *codes):
    font.selection.none()
    selectMore(font, codes)

def selectMore(font, *codes):
    flat = flatten(codes)
    for c in flat:
        if isinstance(c, (unicode, )):
            font.selection.select(("more",), ord(c))
        else:
            font.selection.select(("more",), c)

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

def scalingDownIfWidth(font, if_width):
    for glyph in font.glyphs():
        if glyph.width == if_width:
            glyph.transform(matRescale(if_width / 2, 0, 0.91, 0.91))
            glyph.width = if_width

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

def autoHintAndInstr(font, *codes):
    removeHintAndInstr(font, codes)
    font.autoHint()
    font.autoInstr()

def removeHintAndInstr(font, *codes):
    select(font, codes)
    for glyph in font.selection.byGlyphs:
        if glyph.isWorthOutputting() == True:
            glyph.manualHints = False
            glyph.ttinstrs = ()
            glyph.dhints = ()
            glyph.hhints = ()
            glyph.vhints = ()

def copyTti(srcFont, dstFont):
    for glyphName in dstFont:
        dstFont.setTableData('fpgm', srcFont.getTableData('fpgm'))
        dstFont.setTableData('prep', srcFont.getTableData('prep'))
        dstFont.setTableData('cvt',  srcFont.getTableData('cvt'))
        dstFont.setTableData('maxp', srcFont.getTableData('maxp'))
        copyTtiByGlyphName(srcFont, dstFont, glyphName)

def copyTtiByGlyphName(srcFont, dstFont, glyphName):
    try:
        dstGlyph = dstFont[glyphName]
        srcGlyph = srcFont[glyphName]
        if srcGlyph.isWorthOutputting() == True and dstGlyph.isWorthOutputting() == True:
            dstGlyph.manualHints = True
            dstGlyph.ttinstrs = srcFont[glyphName].ttinstrs
            dstGlyph.dhints = srcFont[glyphName].dhints
            dstGlyph.hhints = srcFont[glyphName].hhints
            dstGlyph.vhints = srcFont[glyphName].vhints
    except TypeError:
        pass

def setFontProp(font, fontInfo):
    font.fontname   = fontInfo[1]
    font.familyname = fontInfo[2]
    font.fullname   = fontInfo[3]
    font.weight = "Book"
    font.copyright =  "Copyright (c) 2006-2012 Raph Levien (Inconsolata)\n"
    font.copyright += "Copyright (c) 2013 M+ FONTS PROJECT (M+)\n"
    font.copyright += "Copyright (c) 2013 itouhiro (Migu)\n"
    font.copyright += "Copyright (c) 2014 MM (Mgen+)\n"
    font.copyright += "Copyright (c) 2014 Adobe Systems Incorporated. (NotoSansJP)\n"
    font.copyright += "Licenses:\n"
    font.copyright += "SIL Open Font License Version 1.1 "
    font.copyright += "(http://scripts.sil.org/ofl)\n"
    font.copyright += "Apache License, Version 2.0 "
    font.copyright += "(http://www.apache.org/licenses/LICENSE-2.0)"
    font.version = newfont_version
    font.sfntRevision = newfont_sfntRevision
    font.sfnt_names = (('English (US)', 'UniqueID', fontInfo[2]), )
    #('Japanese', 'PostScriptName', fontInfo[2]), 
    #('Japanese', 'Family', fontInfo[1]), 
    #('Japanese', 'Fullname', fontInfo[3]), 

    font.hasvmetrics = True
    font.head_optimized_for_cleartype = True

    font.os2_panose = panoseBase
    font.os2_vendor = "M+"
    font.os2_version = 1

    font.os2_winascent       = newfont_winAscent
    font.os2_winascent_add   = 0
    font.os2_windescent      = newfont_winDescent
    font.os2_windescent_add  = 0
    font.os2_typoascent      = newfont_typoAscent
    font.os2_typoascent_add  = 0
    font.os2_typodescent     = -newfont_typoDescent
    font.os2_typodescent_add = 0
    font.os2_typolinegap     = newfont_typoLinegap
    font.hhea_ascent         = newfont_hheaAscent
    font.hhea_ascent_add     = 0
    font.hhea_descent        = -newfont_hheaDescent
    font.hhea_descent_add    = 0
    font.hhea_linegap        = newfont_hheaLinegap


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
fRp = fontforge.open( srcfontReplaceParts )

# modify em
fRp.em  = newfont_em
fRp.ascent  = newfont_ascent
fRp.descent = newfont_descent

# post-process
fRp.selection.all()
fRp.round()

#fRp.generate("/modReplaceParts.ttf", '', generate_flags)

########################################
# modified Mgen+ 1m
########################################

print
print "Open " + srcfontMgenplus
fMg = fontforge.open( srcfontMgenplus )

# modify em
fMg.em  = newfont_em
fMg.ascent  = newfont_ascent
fMg.descent = newfont_descent

# modify
print "modify"

# scaling down
if scalingDownIfWidth_flag == True:
    print "While scaling, wait a little..."
    scalingDownIfWidth(fMg, newfont_em)

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

# modify
print "modify"

# 全角 brackets （）［］｛｝＜＞
srcTarget = (0x0028, 0x0029, 0x005b, 0x005d, 0x007b, 0x007d, 0x003c, 0x003e)
dstTarget = (0xff08, 0xff09, 0xff3b, 0xff3d, 0xff5b, 0xff5d, 0xff1c, 0xff1e)
copyAndPaste(fMi, srcTarget, fMi, dstTarget)
setWidth(fMi, newfont_em)
centerInWidth(fMi)

# scaling down
if scalingDownIfWidth_flag == True:
    print "While scaling, wait a little..."
    scalingDownIfWidth(fMi, newfont_em)

#fMi.generate("/modMigu.ttf", '', generate_flags)

########################################
# create MyricaM
########################################
fMm = fIn

print
print "Build " + newfontM[0]

# pre-process
setFontProp(fMm, newfontM)

# marge ReplaceParts
print "marge ReplaceParts"
# 文字の置換え
target = (
    0x002a,  # * : astarisk
    0x006c,  # l : small letter l
    0x2013,  # – : en dash –
    0x2014)  # — : em dash —
copyAndPaste(fRp, target, fMm, target)

# marge Mgen+ 1m
print "marge Mgen+ 1m"
# マージ
fMm.mergeFonts( srcfontMgenplus )
fMm.os2_unicoderanges = fMg.os2_unicoderanges
fMm.os2_codepages = fMg.os2_codepages
# ルックアップテーブルの置換え
for l in fMg.gsub_lookups:
    if (l in fMm.gsub_lookups) == False:
        fMm.importLookups(fMg, l)
for l in fMm.gsub_lookups:
    if l.startswith(fMg.fontname + "-") == True:
        fMm.removeLookup(l)

# marge Migu 1m
print "marge Migu 1m"
# 文字の置換え
target = (
    # JIS X 0208 ひらがな（83字）
    list(u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん"),
    # JIS X 0208 カタカナ（86字）
    list(u"ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ"),
    # JIS X 0208 仮名又は漢字に準じるもの（10字）
    list(u"ヽヾゝゞ〃仝々〆〇ー"),
    # JIS X 0208 和字間隔、記述記号（19字）
    list(u"　、。，．・：；？！―‐／＼～∥｜…‥"),
    # JIS X 0208 ダイアクリティカルマーク（8字）
    list(u"゛゜´｀¨＾￣＿"),
    # JIS X 0208 括弧記号（22字）
    list(u"‘’“”（）〔〕［］｛｝〈〉《》「」『』【】"),
    # JIS X 0208 学術記号（45字）
    list(u"＋－±×÷＝≠＜＞≦≧∞∴♂♀∈∋⊆⊇⊂⊃∪∩∧∨￢⇒⇔∀∃∠⊥⌒∂∇≡≒≪≫√∽∝∵∫∬"),
    # JIS X 0208 単位記号（11字）
    list(u"°′″℃￥＄￠￡％Å‰"),
    # JIS X 0208 一般記号（32字）
    list(u"＃＆＊＠§☆★○●◎◇◆□■△▲▽▼※〒→←↑↓〓♯♭♪†‡¶◯"),
    # JIS X 0208 数字（10字）
    list(u"０１２３４５６７８９"),
    # JIS X 0208 ラテン文字（52字）
    list(u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"),
    # JIS X 0208 ギリシャ文字（48字）
    list(u"ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω"),
    # JIS X 0208 キリル文字（66字）
    list(u"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
    # JIS X 0213 に登録されているNEC特殊文字記号
    list(u"①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ㍉㌔㌢㍍㌘㌧㌃㌶㍑㍗㌍㌦㌣㌫㍊㌻㎜㎝㎞㎎㎏㏄㎡〝〟№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍻㍾㍽㍼∮∟⊿"),
    # JIS X 0213 に登録されているIBM拡張文字記号
    list(u"ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ￤＇＂"),
    # その他(JIS以外)のNEC特殊文字記号
    list(u"∑"),
    # UNICODE に含まれる JIS 以外のひらかな・カタカナ
    list(u"ゔゕゖゟヷヸヹヺヿ゙゚゠"),
    # JIS X 0201 (ANK) 半角英数字記号 (ASCII文字 0x21-0x7E は除く)
    list(u"､｡･ｰﾞﾟ｢｣ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｬｭｮｯ"),
    # 半濁点（ぱぴぷぺぽパピプペポ の右上の円）を大きくして、濁点と判別しやすく
    list(u"ぱぴぷぺぽパピプペポ"), # 上記との重複あり
    # 「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別
    list(u"カ力エ工ロ口ー一ニ二"), # 上記との重複あり
    # ～〜（FULLWIDTH TILDE・WAVE DASH）の区別
    list(u"～〜"),) # 上記との重複あり
    # αβなど一部のギリシャ文字を全角に   : 上記で選択済み
    # φЯなど一部のキリル文字を全角に     : 上記で選択済み
    # ±×÷√‰§†‡¶などの記号を全角に : 上記で選択済み
copyAndPaste(fMi, target, fMm, target)

# post-process
fMm.selection.all()
fMm.round()

# generate
print "Generate " + newfontM[0]
fMm.generate(newfontM[0], '', generate_flags)

# marge HinthingParts
if os.path.exists( srcfontHintingParts ) == True:
    print "marge HintingParts"
    shutil.copyfile(newfontM[0], "../../MyricaSourceTTF/MyricaM_NoHint.ttf")
    fHp = fontforge.open( srcfontHintingParts )

    #property
    setFontProp(fHp, newfontM)

    # modify em
    fHp.em  = newfont_em
    fHp.ascent  = newfont_ascent
    fHp.descent = newfont_descent

    # delete
    for glyph in fHp.glyphs():
        if glyph.unicode <= 0:
            select(fHp, glyph.glyphname)
            fHp.clear()

    # marge
    fHp.mergeFonts( newfontM[0] )
    fHp.os2_unicoderanges = fMm.os2_unicoderanges
    fHp.os2_codepages = fMm.os2_codepages
    # ルックアップテーブルの置換え
    for l in fMm.gsub_lookups:
        if (l in fHp.gsub_lookups) == False:
            fHp.importLookups(fMm, l)
    for l in fHp.gsub_lookups:
        if l.startswith(fMm.fontname + "-") == True:
            fHp.removeLookup(l)

    # generate
    print "Generate " + newfontM[0] + " with Hinting"
    fHp.generate(newfontM[0], '', generate_flags)

fMm.close()
fRp.close()
fMg.close()
fMi.close()

########################################
# create MyricaP
########################################
print
print "Build " + newfontP[0]
fMp = fontforge.open( newfontM[0] )

# pre-process
fMp.fontname   = newfontP[1]
fMp.familyname = newfontP[2]
fMp.fullname   = newfontP[3]
fMp.sfnt_names = (('English (US)', 'UniqueID', newfontP[2]), )

panose = list(fMp.os2_panose)
panose[3] = 0
fMp.os2_panose = tuple(panose)

# modify
print "modify"

# 半角
hankaku = (100,)
# 全角
zenkaku = (50,)

# 全文字の幅の自動設定
fMp.selection.all()
for glyph in fMp.selection.byGlyphs:
    #print glyph.glyphname + ", code " + str(glyph.unicode) + ", width " + str(glyph.width)
    if glyph.width == newfont_em:         # 全角文字
        setAutoWidthGlyph(glyph, hankaku[0])
    else:                                 # 半角文字
        bb = glyph.boundingBox()
        nw = (bb[2] - bb[0]) + zenkaku[0] * 2
        if glyph.width > nw:
            setAutoWidthGlyph(glyph, zenkaku[0])

# 半角数字は幅固定で中央配置
select(fMp, rng(0x0030,0x0039))   # 0-9
setWidth(fMp, 490)
centerInWidth(fMp)

# post-process
fMp.selection.all()
fMp.round()

# generate
print "Generate " + newfontP[0]
fMp.generate(newfontP[0], '', generate_flags)

fMp.close()

########################################
# create MyricaN
########################################
print
print "Build " + newfontN[0]
fMn = fontforge.open( newfontM[0] )

# pre-process
fMn.fontname   = newfontN[1]
fMn.familyname = newfontN[2]
fMn.fullname   = newfontN[3]
fMn.sfnt_names = (('English (US)', 'UniqueID', newfontN[2]), )

panose = list(fMn.os2_panose)
panose[3] = 0
fMn.os2_panose = tuple(panose)

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
fMn.selection.all()
for glyph in fMn.selection.byGlyphs:
    #print glyph.glyphname + ", code " + str(glyph.unicode) + ", width " + str(glyph.width)
    glyph.ttinstrs = ()
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
select(fMn, rng(0x0030,0x0039))   # 0-9
setWidth(fMn, 400)
centerInWidth(fMn)

# post-process
fMn.selection.all()
fMn.round()

# generate
print "Generate " + newfontN[0]
fMn.generate(newfontN[0], '', generate_flags)

fMn.close()
