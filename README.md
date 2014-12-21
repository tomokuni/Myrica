# プログラミング用フォント Myrica  
Version 2.001.20141221  
フォントファイルだけが必要な場合は、Myrica.7z ファイルを取得してください。
  
  
Myrica （ミリカ）は、フリーなプログラミング用 TrueType フォントです。  
視認性、判別性 が高くなるように、複数のフォントファイルを元に合成しました。
  
  
## フォントの特徴  
多くの特徴をプログラミング用フォント Ricty から継承しています。  
*ASCII文字は「Inconsolata」が適用されます。  
*それ以外の文字には「源柔ゴシック」が適用されます。  
*半角文字と全角文字の横幅の比が 1:2 に調整されています。  
*視認性の高い日本語文字 (半濁音など) が使用できます。  
  
Rictyにない特徴  
*ASCII文字はヒンティング付きの Inconsolata から、ヒンティング情報を継承していますので、Windowsでもクッキリしています。  
  
  
## フォントイメージ  
![Font Image](/Source/FontImage.png)
  
  
## フォント構成  
  
・Myrica.ttc ： 以下の３フォントをパッケージしたファイルです。  
  
・MyricaM ： 等幅フォントです。プログラミング用に作成しました。  
  
・MyricaP ： なんちゃってプロポーショナルフォントです。  
　　　グリフはそのままに、文字の左右スペースを削り、プロポーショナル文字っぽく作成しました。  
　　　ただし、数字(0-9)は幅固定していますので、エクセルで数値表示しても、桁がずれません。  
  
・MyricaN ： 幅を狭くしたフォントです。一定幅で多くの文字を表示できるように作成しました。  
　　　グリフは、半角文字:85%、全角ひらがなカタカナ:50%、その他の全角文字:60% に縮小し、  
　　　文字の左右スペースを削り、プロポーショナル文字っぽく作成しました。  
　　　ただし、数字(0-9)は幅固定していますので、エクセルで数値表示しても、桁がずれません。  
  
  
## 頒布元  

Myrica の最新版は、以下のサイトで頒布しています。  

GitHub
https://github.com/munotoki/Myrica


## フォントの作成経緯  
このフォントは、プログラミング用フォント Ricty に感銘を受けて、作成したものです。  
  
Ricty はとても素晴らしいフォントですが、幾つかの不満点がありました。  
・ヒンティングされていないので、環境によっては半角英数字が潰れてしまい判別しにくくなる場合がある。  
・M+ OUTLINE FONTS 以外の日本語フォントが IPA 由来のため、Inconsolata との合成フォントが再配布できない。  
・アスタリスク(*) の字形が好みではない。  
  
これらに関して、以下のように解決したのが、本フォント Myrica です。  
・ヒンティング付きの Inconsolata を使用し、ヒンティングを消さないように合成した。  
・アスタリスク(*) を含む幾つかを好みのオリジナルな字形に変更した。  
・ASCII文字以外は 源柔ゴシック を元に合成した。  
  
  
## グリフの構成  
プログラミング用に文字が判別しやすいように考慮しています。

(1)ASCII文字(0x21-0x7E) を「Inconsolata」で置換えました。  
  さらに以下の変更を行っています。  
  ・r にセリフ付き (Inconsolata に内包されているグリフで置換え)  
  ・D にクロスバー付き (Inconsolata に内包されているグリフで置換え)  
  ・| が破断線 (Inconsolata に内包されているグリフで置換え)  
  ・"'`,.:; が大きめに作られている (修正した)  
※Inconsolata: 「Top 10 Programming Fonts」や「プログラミング時に最適なフォント『Inconsolata』」などで高い評価を受けているサンセリフ体等幅欧文フォント  
  
  
(2)ASCII文字以外は「源柔ゴシック」をベースとしました。  
※源柔ゴシック: 「源ノ角ゴシック」をベースとして作成された丸ゴシック化した日本語フォント  
  
  
一部の文字を改変しています。  
(3)「オリジナル」な文字への置換え  
  ・0x002a   * : astarisk  
  ・0x006c   l : small letter l  
  ・0x2013   – : en dash –  
  ・0x2014   — : em dash —  
  ・半濁点（ぱぴぷぺぽパピプペポ の右上の円）を大きくして、濁点と判別しやすく。  
  ・「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別。  
  ・ ～〜（FULLWIDTH TILDE・WAVE DASH）の区別。  
  ※半濁点 や カタカナ・漢字、 FULLWIDTH TILDE・WAVE DASH の区別は、Miguフォント を参考にさせて頂きました。
  
  
## ライセンスと著作権について  
「SIL OPEN FONT LICENSE Version 1.1」と「Apache 2.0 License」のデュアルライセンスです。
  
・ASCII文字は、Inconsolata と同じ SIL OPEN FONT LICENSE Version 1.1 のもとで使用することができます。  
・ASCII文字以外 は、源柔ゴシック と同じ Apache 2.0 License のもとで使用することができます。  
・源柔ゴシック の一部に M+ OUTLINE FONTS 由来の文字グリフが含まれています。  
  
SIL OPEN FONT LICENSE Version 1.1 の内容は、アーカイブに同梱の LICENSE_OFL.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/SIL_Open_Font_License_1.1  
  
Apache 2.0 License の内容は、アーカイブに同梱の LICENSE_Apache.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/licenses%2FApache_License_2.0  
  
M+ OUTLINE FONTS のグリフは、同梱のファイル LICENSE_M+.txt に記載された自由なM+ FONTS LICENSE に基づき使用しています  
  
  
・Myrica は、Inconsolata と 源柔ゴシック を合成したフォントです。  
・フォントデータに含まれる、Inconsolata 由来の文字グリフの著作権は Raph Levien, Cyreal が所有しています。  
・フォントデータに含まれる、源ノ角ゴシック由来の文字グリフの著作権は Adobe が所有しています。  
・源ノ角ゴシックに含まれる、M+ OUTLINE FONTS 由来の文字グリフの著作権は M+ FONTS PROJECT が所有しています。  
  
  
## 名前の由来  
・源柔ゴシック 作者の MM氏  
・Ricty 作者の Yusa 氏  
・Inconsolata 作者の Raph Levien 氏  
・Migu 作者の itouhiro 氏  
・M+ 作者の coz 氏  
・源の角ゴシック 作者の Adobe Systems Software Ireland Ltd.  
それぞれの作者の頭文字から Myrica と命名しました。  
  
  
## 改変元  
  
Myrica は、以下のフォントを直接または間接的に合成、参照して制作しました。  
素晴らしいフリーフォントの制作に関わる全ての方に深くお礼申し上げます。  
  
M+ OUTLINE FONTS  
http://mplus-fonts.sourceforge.jp/  
  
源柔ゴシック  
http://jikasei.me/font/genjyuu/  
  
源ノ角ゴシック (Source Hans Sans)  
http://store1.adobe.com/cfusion/store/html/index.cfm?store=OLS-JP&event=displayFontPackage&code=1967  
  
Migu  
http://mix-mplus-ipa.sourceforge.jp/migu/  
  
Inconsolata  
https://www.google.com/fonts/specimen/Inconsolata  
  
Ricty  
https://github.com/yascentur/Ricty  
  
  
## 改版履歴  
  
#### Version 2.001.20141221  
  
・日本語フォントのベースを源柔ゴシックに変更  
  
#### Version 1.012.20141102  
  
・()<>[]{} の縦位置に違和感があったので調整  
  
#### Version 1.011.20140924  
  
・ASCII文字以外の文字サイズを見直し  
　　ASCII文字とそれ以外の文字のバランスが悪かったので調整  
  
#### Version 1.010.20140921  
  
・ASCII文字以外のヒンティングを見直し  
　　ASCII文字は Inconsolata のヒンティング情報を継承  
  
#### Version 1.009.20140920  
  
・ASCII文字以外のヒンティングを12ポイントで見やすいように見直し  
　　ASCII文字は Inconsolata のヒンティング情報を継承  
  
#### Version 1.008.20140915  
  
・ひらがな・カタカナ と一部の記号に、ヒンティング情報を付加  
　　ASCII文字は Inconsolata のヒンティング情報を継承  
  
#### Version 1.007.20140910  
  
・ひらがな/カタカナの一部の文字にヒンティングを付与  
一部の文字は FontForge による「ヒンティングあり」の方が綺麗に見えたから  
　　対象： おかがこごただてでとどねむゔギテナヮワヲヷヺ゙゚゛゜  
  
#### Version 1.006.20140909  
  
・Inconsolata 由来の一部の文字のヒンティングを再設定  
Inconsolata 由来の文字で移動や拡大した字に対して、継承元のヒンティングの影響により意図した位置に表示されていなかったため  
　　対象： "'`,.:;+-<>=~()[]{}!?  

・ひらがな/カタカナの一部の文字にヒンティングを付与  
一部の文字は FontForge による「ヒンティングあり」の方が綺麗に見えたから  
　　対象： うぱぴぷぺぽらりるイウザジタダヅデパピプペホポミラリ  
  
#### Version 1.005.20140905  
  
・一部の文字を全角に修正  
　　対象： №∥  
  
#### Version 1.004.20140904  
  
・一部の文字を全角に修正  
　　対象： ↑↓  
  
#### Version 1.003.20140904  
  
・一部の文字を全角に修正  
　　対象： ±×÷√‰§†‡¶´¨‘’“”°′″  
  
#### Version 1.002.20140903  
  
・；(全角セミコロン), ：(全角コロン), ．(全角ピリオド) のグリフが崩れていたのを修正  
  
#### Version 1.001.20140829  
  
・Mgen+ のバージョンアップに伴う更新  
・以下のファイルを元に合成  
　　Inconsolata : Inconsolata-Regular.ttf : 1.013 (Google Fonts)  
　　Mgen+       : mgenplus-1m-regular.ttf : 1.058.20140808 (20140828)  
　　Migu        : migu-1m-regular.ttf     : 2013.0617 (20130617)  
  
#### Version 1.000.20140825  
  
・初回リリース  
・以下のファイルを元に合成  
　　Inconsolata : Inconsolata-Regular.ttf : 1.013 (Google Fonts)  
　　Mgen+       : mgenplus-1m-regular.ttf : 1.058.20140808 (20140808)  
　　Migu        : migu-1m-regular.ttf     : 2013.0617 (20130617)  
