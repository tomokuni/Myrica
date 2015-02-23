#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Author: Tomokuni SEKIYA
#
# This script is font expander
#

# source file
srcfont = "GenShinGothic-Monospace-ExtraLight-Validate.ttf"

# out file
outfont = "GenShinGothic-Monospace-ExtraLight-BoldH15V1.ttf"

# define
generate_horizontal = 15
generate_vertical   = 1
generate_flags = ('opentype', 'PfEd-lookups', 'TeX-table')

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
fontforge.setPrefs('ClearInstrsBigChanges', 1)
# TrueType命令をコピー 0:オフ 1:オン
fontforge.setPrefs('CopyTTFInstrs', 0)

########################################
# pre-process
########################################

print 
print 
print "This script is font expander"
print 
if os.path.exists( srcfont ) == False:
    print "Error: " + srcfont + " not found"
    sys.exit( 1 )

########################################
# define function
########################################
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
    for glyph in font.selection.byGlyphs:
        if glyph.isWorthOutputting() == False:
            font.selection.select(("less",), glyph)

def selectExistAll(font):
    font.selection.none()
    for glyphName in font:
        if font[glyphName].isWorthOutputting() == True:
            font.selection.select(("more",), glyphName)


########################################
# bold
########################################

print
print "Open " + srcfont
fSrc = fontforge.open( srcfont )

contour = fontforge.contour()
contour.moveTo(-generate_horizontal,  generate_vertical)
contour.lineTo( generate_horizontal,  generate_vertical)
contour.lineTo( generate_horizontal, -generate_vertical)
contour.lineTo(-generate_horizontal, -generate_vertical)
contour.lineTo(-generate_horizontal,  generate_vertical)
contour.closed = True

# modify
print "bold"
# 拡大
for glyphName in fSrc:
    if fSrc[glyphName].isWorthOutputting() == True:
        if fSrc[glyphName].unicode < 10000:
            print "bold : code 0u" + ('%x' % fSrc[glyphName].unicode) + "(" + str(fSrc[glyphName].unicode) +  ")" + ", " + fSrc[glyphName].glyphname
            fSrc[glyphName].stroke("polygonal", contour, ('removeinternal'))
fSrc.generate(outfont, '', generate_flags)

for glyphName in fSrc:
    if fSrc[glyphName].isWorthOutputting() == True:
        if fSrc[glyphName].unicode >= 10000 and fSrc[glyphName].unicode < 20000:
            print "bold : code 0u" + ('%x' % fSrc[glyphName].unicode) + "(" + str(fSrc[glyphName].unicode) +  ")" + ", " + fSrc[glyphName].glyphname
            fSrc[glyphName].stroke("polygonal", contour, ('removeinternal'))
fSrc.generate(outfont, '', generate_flags)

for glyphName in fSrc:
    if fSrc[glyphName].isWorthOutputting() == True:
        if fSrc[glyphName].unicode >= 20000 and fSrc[glyphName].unicode < 30000:
            print "bold : code 0u" + ('%x' % fSrc[glyphName].unicode) + "(" + str(fSrc[glyphName].unicode) +  ")" + ", " + fSrc[glyphName].glyphname
            fSrc[glyphName].stroke("polygonal", contour, ('removeinternal'))
fSrc.generate(outfont, '', generate_flags)

for glyphName in fSrc:
    if fSrc[glyphName].isWorthOutputting() == True:
        if fSrc[glyphName].unicode >= 30000 and fSrc[glyphName].unicode < 40000:
            print "bold : code 0u" + ('%x' % fSrc[glyphName].unicode) + "(" + str(fSrc[glyphName].unicode) +  ")" + ", " + fSrc[glyphName].glyphname
            fSrc[glyphName].stroke("polygonal", contour, ('removeinternal'))
fSrc.generate(outfont, '', generate_flags)

for glyphName in fSrc:
    if fSrc[glyphName].isWorthOutputting() == True:
        if fSrc[glyphName].unicode >= 40000 and fSrc[glyphName].unicode < 50000:
            print "bold : code 0u" + ('%x' % fSrc[glyphName].unicode) + "(" + str(fSrc[glyphName].unicode) +  ")" + ", " + fSrc[glyphName].glyphname
            fSrc[glyphName].stroke("polygonal", contour, ('removeinternal'))
fSrc.generate(outfont, '', generate_flags)

for glyphName in fSrc:
    if fSrc[glyphName].isWorthOutputting() == True:
        if fSrc[glyphName].unicode >= 50000:
            print "bold : code 0u" + ('%x' % fSrc[glyphName].unicode) + "(" + str(fSrc[glyphName].unicode) +  ")" + ", " + fSrc[glyphName].glyphname
            fSrc[glyphName].stroke("polygonal", contour, ('removeinternal'))
fSrc.generate(outfont, '', generate_flags)

fSrc.close()
