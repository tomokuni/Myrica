# プログラミング用フォント Myrica  
Myrica （ミリカ）は、フリーなプログラミング用 TrueType フォントです。  
視認性、判別性 が高くなるように、複数のフォントファイルを元に合成/修正しました。  


## フォントの特徴  
多くの特徴をプログラミング用フォント Ricty から継承しています。  

* ASCII文字は「Inconsolata」が適用されます。  
* それ以外の文字には「源真ゴシック」または「Mgen+」が適用されます。  
* 半角文字と全角文字の横幅の比が 1:2 に調整されています。  
* 視認性の高い日本語文字 (半濁音など) が使用できます。  

#### Rictyにない特徴  
以下の文字にはヒンティング情報がありますので、Windowsでもクッキリしています。  

* ASCII文字はヒンティング付きの Inconsolata から、ヒンティング情報を継承しています。  
* 平仮名と片仮名にもヒンティング情報を付加しています。  



## フォントイメージ  
![Font Image](/Source/myrica_FontImage.png)  



## フォント構成 / 配布ファイル  

### Myrica.ttc  
ASCII文字は Inconsolata、それ以外の文字は 源真ゴシック をベースとした以下の３フォントをパッケージしたファイルです。
* 7z圧縮版　約4MB https://github.com/tomokuni/Myrica/raw/master/product/Myrica.7z  
* zip圧縮版　約9MB https://github.com/tomokuni/Myrica/raw/master/product/Myrica.zip  
  
###### Myrica M  
* 等幅フォントです。プログラミング用に作成しました。  

###### Myrica P  
* なんちゃってプロポーショナルフォントです。  
グリフは、全角かな文字:90%、その他の全角文字:95% に縮小し、文字の左右スペースを削り、プロポーショナル文字っぽく作成しました。  
ただし、数字(0-9)は幅固定しています。  

###### Myrica N  
* 幅を狭くしたフォントです。一定幅で多くの文字を表示できるように作成しました。  
グリフは、半角文字:68%、全角かな文字:55%、その他の全角文字:60% に縮小し、文字の左右スペースを削り、プロポーショナル文字っぽく作成しました。  
ただし、数字(0-9)は幅固定しています。  

### MyricaM.ttc  
ASCII文字は Inconsolata、それ以外の文字は Mgen+ をベースとした以下の３フォントをパッケージしたファイルです。  
* 7z圧縮版　約4MB https://github.com/tomokuni/Myrica/raw/master/product/MyricaM.7z  
* zip圧縮版　約9MB https://github.com/tomokuni/Myrica/raw/master/product/MyricaM.zip  
  
###### MyricaM M  
###### MyricaM P  
###### MyricaM N  



## 頒布元  

Myrica の最新版は、以下のサイトで頒布しています。  

プログラミングフォント Myrica  
http://myrica.estable.jp/  



## フォントの作成経緯  
このフォントは、プログラミング用フォント Ricty に感銘を受けて、作成したものです。  

Ricty はとても素晴らしいフォントですが、幾つかの不満点がありました。  

* ヒンティングされていないので、環境によっては半角英数字が潰れてしまい判別しにくくなる場合がある。  
* M+ OUTLINE FONTS 以外の日本語フォントが IPA 由来のため、Inconsolata との合成フォントが再配布できない。  
* アスタリスク(*) の字形が好みではない。  

これらに関して、以下のように解決したのが、本フォント Myrica です。  

* ヒンティング付きの Inconsolata を使用し、ヒンティングを消さないように合成した。  
* ASCII文字以外は 源真ゴシック または Mgen+ を元に合成した。  
* アスタリスク(*) を含む幾つかを好みのオリジナルな字形に変更した。  



## グリフの構成  
プログラミング用に文字が判別しやすいように考慮しています。

ASCII文字(0x21-0x7E) を「Inconsolata」で置換え、さらに以下の変更を行っています。  
※Inconsolata: 「Top 10 Programming Fonts」や「プログラミング時に最適なフォント『Inconsolata』」などで高い評価を受けているサンセリフ体等幅欧文フォント  

* r にセリフ付き (Inconsolata に内包されている別のグリフで置換え)  
* D にクロスバー付き (Inconsolata に内包されている別のグリフで置換え)  
* | が破断線 (Inconsolata に内包されている別のグリフで置換え)  


ASCII文字以外は「源真ゴシック」または「Mgen+」をベースとしました。  
※源真ゴシック: 「源ノ角ゴシック」をベースとして作成された日本語フォント  
※Mgen+: 「M+ OUTLINE FONTS」をベースとして作成された日本語フォント  


一部の文字を修正しました。  

* "'`,.:; を大きめに補正  
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
* ASCII文字以外 は、源真ゴシック/Mgen+ と同じ Apache 2.0 License のもとで使用することができます。  
* 源真ゴシック/Mgen+ には M+ OUTLINE FONTS 由来の文字グリフが含まれています。  

SIL OPEN FONT LICENSE Version 1.1 の内容は、アーカイブに同梱の LICENSE_OFL.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/SIL_Open_Font_License_1.1  

Apache 2.0 License の内容は、アーカイブに同梱の LICENSE_Apache.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/licenses%2FApache_License_2.0  

M+ OUTLINE FONTS のグリフは、同梱のファイル LICENSE_M+.txt に記載された自由なM+ FONTS LICENSE に基づき使用しています  


* Myrica は、Inconsolata と 源真ゴシック を合成したフォントです。  
* MyricaM は、Inconsolata と Mgen+ を合成したフォントです。  
* フォントデータに含まれる、Inconsolata 由来の文字グリフの著作権は Raph Levien, Cyreal が所有しています。  
* フォントデータに含まれる、源ノ角ゴシック由来の文字グリフの著作権は Adobe が所有しています。  
* 源真ゴシック/Mgen+に含まれる、M+ OUTLINE FONTS 由来の文字グリフの著作権は M+ FONTS PROJECT が所有しています。  



## 名前の由来  
それぞれの作者の頭文字から Myrica と命名しました。  

* 源真ゴシック/Mgen+ 作者の MM氏  
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

* 源真ゴシック、源柔ゴシック、Mgen+  
http://jikasei.me/font/  

* M+ OUTLINE FONTS  
http://mplus-fonts.sourceforge.jp/  

* 源ノ角ゴシック (Source Hans Sans)  
http://store1.adobe.com/cfusion/store/html/index.cfm?store=OLS-JP&event=displayFontPackage&code=1967  

* Migu  
http://mix-mplus-ipa.sourceforge.jp/migu/  


## [Myrica 改版履歴](product/Myrica_改版履歴.md "Myrica 改版履歴")  

## [MyricaM 改版履歴](product/MyricaM_改版履歴.md "MyricaM 改版履歴")  
