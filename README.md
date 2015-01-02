# プログラミング用フォント Myrica  
Myrica （ミリカ）は、フリーなプログラミング用 TrueType フォントです。  
視認性、判別性 が高くなるように、複数のフォントファイルを元に合成/修正しました。

フォントファイルだけが必要な場合は、Myrica.7z ファイルだけを取得するとダウンロードサイズが小さくて便利です。



## フォントの特徴  
多くの特徴をプログラミング用フォント Ricty から継承しています。  

* ASCII文字は「Inconsolata」が適用されます。  
* それ以外の文字には「源真ゴシック」が適用されます。  
* 半角文字と全角文字の横幅の比が 1:2 に調整されています。  
* 視認性の高い日本語文字 (半濁音など) が使用できます。  

#### Rictyにない特徴  
以下の文字にはヒンティング情報がありますので、Windowsでもクッキリしています。  

* ASCII文字はヒンティング付きの Inconsolata から、ヒンティング情報を継承しています。  
* 平仮名と片仮名はにもヒンティング情報を付加しています。  



## フォントイメージ  
![Font Image](/Source/FontImage.png)


## フォント構成  

* ### Myrica.ttc
　　　以下の３フォントをパッケージしたファイルです。  

* ### MyricaM
　　　等幅フォントです。プログラミング用に作成しました。  

* ### MyricaP
　　　なんちゃってプロポーショナルフォントです。  
　　　グリフはそのままに、文字の左右スペースを削り、プロポーショナル文字っぽく作成しました。  
　　　ただし、数字(0-9)は幅固定しています。  

* ### MyricaN
　　　幅を狭くしたフォントです。一定幅で多くの文字を表示できるように作成しました。  
　　　グリフは、半角文字:68%、全角かな文字:65%、その他の全角文字:60% に縮小し、  
　　　文字の左右スペースを削り、プロポーショナル文字っぽく作成しました。  
　　　ただし、数字(0-9)は幅固定しています。  



## 頒布元  

Myrica の最新版は、以下のサイトで頒布しています。  

GitHub
https://github.com/munotoki/Myrica



## フォントの作成経緯  
このフォントは、プログラミング用フォント Ricty に感銘を受けて、作成したものです。  

Ricty はとても素晴らしいフォントですが、幾つかの不満点がありました。  

* ヒンティングされていないので、環境によっては半角英数字が潰れてしまい判別しにくくなる場合がある。  
* M+ OUTLINE FONTS 以外の日本語フォントが IPA 由来のため、Inconsolata との合成フォントが再配布できない。  
* アスタリスク(*) の字形が好みではない。  

これらに関して、以下のように解決したのが、本フォント Myrica です。  

* ヒンティング付きの Inconsolata を使用し、ヒンティングを消さないように合成した。  
* アスタリスク(*) を含む幾つかを好みのオリジナルな字形に変更した。  
* ASCII文字以外は 源真ゴシック を元に合成した。  



## グリフの構成  
プログラミング用に文字が判別しやすいように考慮しています。

ASCII文字(0x21-0x7E) を「Inconsolata」で置換え、さらに以下の変更を行っています。  
※Inconsolata: 「Top 10 Programming Fonts」や「プログラミング時に最適なフォント『Inconsolata』」などで高い評価を受けているサンセリフ体等幅欧文フォント  

* r にセリフ付き (Inconsolata に内包されている別のグリフで置換え)  
* D にクロスバー付き (Inconsolata に内包されている別のグリフで置換え)  
* | が破断線 (Inconsolata に内包されている別のグリフで置換え)  
* "'`,.:; を大きめに修正  


ASCII文字以外は「源真ゴシック」をベースとしました。  
※源真ゴシック: 「源ノ角ゴシック」をベースとして作成された日本語フォント  


一部の文字を修正しました。  

* 0x002a   * : astarisk (オリジナル)  
* 0x006c   l : small letter l (オリジナル)  
* 0x2013   – : en dash – (Ricty を参考に)  
* 0x2014   — : em dash — (Ricty を参考に)  
* 「ぱぴぷぺぽパピプペポ」の半濁点を大きくして、濁点と判別しやすく。(Migu を参考に)  
* 「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別。(Migu を参考に)  
*  「～〜」（FULLWIDTH TILDE・WAVE DASH）の区別。(Migu を参考に)  



## ライセンスと著作権について  
「SIL OPEN FONT LICENSE Version 1.1」と「Apache 2.0 License」のデュアルライセンスです。

* ASCII文字は、Inconsolata と同じ SIL OPEN FONT LICENSE Version 1.1 のもとで使用することができます。  
* ASCII文字以外 は、源真ゴシック と同じ Apache 2.0 License のもとで使用することができます。  
* 源真ゴシック の一部に M+ OUTLINE FONTS 由来の文字グリフが含まれています。  

SIL OPEN FONT LICENSE Version 1.1 の内容は、アーカイブに同梱の LICENSE_OFL.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/SIL_Open_Font_License_1.1  

Apache 2.0 License の内容は、アーカイブに同梱の LICENSE_Apache.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/licenses%2FApache_License_2.0  

M+ OUTLINE FONTS のグリフは、同梱のファイル LICENSE_M+.txt に記載された自由なM+ FONTS LICENSE に基づき使用しています  


* Myrica は、Inconsolata と 源真ゴシック を合成したフォントです。  
* フォントデータに含まれる、Inconsolata 由来の文字グリフの著作権は Raph Levien, Cyreal が所有しています。  
* フォントデータに含まれる、源ノ角ゴシック由来の文字グリフの著作権は Adobe が所有しています。  
* 源ノ角ゴシックに含まれる、M+ OUTLINE FONTS 由来の文字グリフの著作権は M+ FONTS PROJECT が所有しています。  



## 名前の由来  
それぞれの作者の頭文字から Myrica と命名しました。  

* 源真ゴシック 作者の MM氏  
* Ricty 作者の Yusa 氏  
* Inconsolata 作者の Raph Levien 氏  
* Migu 作者の itouhiro 氏  
* M+ 作者の coz 氏  
* 源の角ゴシック 作者の Adobe Systems Software Ireland Ltd.  



## 改変元  

Myrica は、以下のフォントを直接または間接的に合成、参照して制作しました。  
素晴らしいフリーフォントの制作に関わる全ての方に深くお礼申し上げます。  

* Ricty  
https://github.com/yascentur/Ricty  

* Inconsolata  
https://www.google.com/fonts/specimen/Inconsolata  

* 源真ゴシック  
http://jikasei.me/font/genshin/  

* M+ OUTLINE FONTS  
http://mplus-fonts.sourceforge.jp/  

* 源ノ角ゴシック (Source Hans Sans)  
http://store1.adobe.com/cfusion/store/html/index.cfm?store=OLS-JP&event=displayFontPackage&code=1967  

* Migu  
http://mix-mplus-ipa.sourceforge.jp/migu/  



## 改版履歴  

#### Version 2.003.20150102  

* 日本語フォントのベースを源真ゴシック(極細)に変更  
　　Inconsolata : Inconsolata-Regular.ttf (1.013 Google Fonts)  
　　源柔ゴシック : GenJyuuGothic-Monospace-Light.ttf (1.058.20140828)  
　　源真ゴシック : GenShinGothic-Monospace-ExtraLight.ttf (1.058.20140828)  

* 全角ひらかな/カタカナ以外のベースを源真ゴシック(極細)に変更  

#### Version 2.002.20141230  

* 日本語フォントのベースを源真ゴシックに変更  
　　Inconsolata : Inconsolata-Regular.ttf (1.013 Google Fonts)  
　　源柔ゴシック : GenJyuuGothic-Monospace-Light.ttf (1.058.20140828)  
　　源真ゴシック : GenShinGothic-Monospace-Light.ttf (1.058.20140828)  

* Inconsolata をベースとした文字の改変  
　　「 + - = ~ <> () [] {} | 」の文字の位置を調整    

* 全角ひらかな/カタカナのベースを源柔ゴシック、それ以外を源真ゴシックに変更  

#### Version 2.001.20141221  

　　若干だが、ひらがな/カタカナ の好みが源の角ゴシック系だった  
　　日本語部分が印刷時に文字が太くて文字が判別しにくいため、ベースのフォントを細字に変更  
　　細字にしただけだと、画面での表示が貧弱だったため、水平方向に太字化  

* 日本語フォントのベースを源柔ゴシックに変更  
　　Inconsolata : Inconsolata-Regular.ttf (1.013 Google Fonts)  
　　源柔ゴシック : GenJyuuGothic-Monospace-Light.ttf (1.058.20140828)  

* Inconsolata をベースとした文字の改変  
　　「 * l – — 」の文字をオリジナルに変更  
　　「 | D r 」の文字を Inconsolata に内包されている別のグリフで置換え   
　　「 + - = ~ 」の文字の位置を変更    
　　「 " ' ` , . : ; 」の文字を拡大   

* 源柔ゴシック をベースとした文字の改変  
　　ASCII文字以外を水平方向に太字化(weight:10)  
　　「ぱぴぷぺぽパピプペポ」の半濁点を大きく  
　　「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別  
　　「～〜」（FULLWIDTH TILDE・WAVE DASH）の区別  
　　ひらかな/カタカナへのヒント情報の付加

#### Version 1.012.20141102  

* Mgen+ をベースとした最終版
　　Inconsolata : Inconsolata-Regular.ttf (1.013 Google Fonts)  
　　Mgen+       : mgenplus-1m-regular.ttf (1.058.20140808 (20140828)  
　　Migu        : migu-1m-regular.ttf (2013.0617 (20130617)  

* 改変内容  
　　「 * l – — 」の文字をオリジナルに変更  
　　「 | D r 」の文字を Inconsolata に内包されている別のグリフで置換え   
　　「 + - = ~ 」の文字の位置を変更    
　　「 " ' ` , . : ; 」の文字を拡大   
　　ASCII文字以外を水平方向に太字化(weight:10)  
　　「ぱぴぷぺぽパピプペポ」の半濁点を大きく  
　　「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別  
　　「～〜」（FULLWIDTH TILDE・WAVE DASH）の区別  
　　ひらかな/カタカナへのヒント情報の付加