# プログラミング用フォント Myrica  
Version 1.008.20140915  
  
  
Myrica （ミリカ）は、フリーなプログラミング用 TrueType フォントです。  
視認性、判別性 が高くなるように、複数のフォントファイルを元に合成しました。
  
  
## フォントの特徴  
多くの特徴をプログラミング用フォント Ricty から継承しています。  
*ラテン文字には「Inconsolata」が適用されます。  
*それ以外の文字には「Mgen+」または「Migu 1M」が適用されます。美しい M+ と視認性の高い日本語文字 (半濁音など) が使用できます。  
*半角文字と全角文字の横幅の比が 1:2 に調整されています。  

Rictyにない特徴  
*ASCII文字はヒンティング付きの Inconsolata から、ヒンティング情報を継承していますので、Windowsでも視認性が良いです。  
*漢字とASCII文字を除く JIS0208 / JIS0213 の文字には、ヒンティング情報を付加しましたので、Windowsでも視認性が良いです。  
  
  
## フォントイメージ  
![Font Image](/Source/FontImageChrome.png)
  
  
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
・ひらがな・カタカナと一部の記号にヒンティングを付加した。(それ以外の漢字等はヒンティングはありません)  
・M+ OUTLINE FONTS 以外のフォントを IPA から 源ノ角ゴシック に変更して再配布可能とした。  
・アスタリスク(*) を含む幾つかを好みのオリジナルな字形に変更した。  
  
  
## グリフの構成  
プログラミング用に文字が判別しやすいように考慮しています。

(1)ASCII文字(0x21-0x7E) を「Inconsolata」で置換えました。  
  さらに以下の変更を行っています。  
  ・r にセリフ付き (Inconsolata に内包されているグリフで置換え)  
  ・D にクロスバー付き (Inconsolata に内包されているグリフで置換え)  
  ・| が破断線 (Inconsolata に内包されているグリフで置換え)  
  ・"'`,.:; が大きめに作られている (修正した)  
※Inconsolata: 「Top 10 Programming Fonts」や「プログラミング時に最適なフォント『Inconsolata』」などで高い評価を受けているサンセリフ体等幅欧文フォント  
  
  
(2)ASCII文字以外は「Mgen+」をベースとしました。  
※Mgen+: 「M+ OUTLINE FONTS」と「源ノ角ゴシック」をベースとして作成された日本語フォント  
  
  
さらに、一部の文字は他の文字に置き換えています。  
(3)「Migu」由来の文字への置換え。  
※Migu: 「M+ OUTLINE FONTS」をベースに改良された視認性の高い日本語文字を含むフォント  
  ・半濁点（ぱぴぷぺぽパピプペポ の右上の円）を大きくして、濁点と判別しやすく。  
  ・「カ力 エ工 ロ口 ー一 ニ二」（カタカナ・漢字）の区別。  
  ・ ～〜（FULLWIDTH TILDE・WAVE DASH）の区別。  
  ・αβなど一部のギリシャ文字を全角に。  
  ・φЯなど一部のキリル文字を全角に。  
  ・±×÷√‰§†‡¶などの記号を全角に。  
  
  
(4)「オリジナル」な文字への置換え  
  ・0x002a   * : astarisk  
  ・0x006c   l : small letter l  
  ・0x2013   – : en dash –  
  ・0x2014   — : em dash —  
  
  
## ライセンスと著作権について  
「SIL OPEN FONT LICENSE Version 1.1」と「Apache 2.0 License」のデュアルライセンスです。
  
・ASCII文字は、Inconsolata と同じ SIL OPEN FONT LICENSE Version 1.1 のもとで使用することができます。  
・ASCII文字以外 は、Megn+ と同じ Apache 2.0 License のもとで使用することができます。  
・ただし、使用や埋め込み・改変を行った結果、使用したのが M+ OUTLINE FONTS 由来の文字グリフのみだった場合は、より要件が少ない M+ FONT LICENSE を適用することができます。  
  
SIL OPEN FONT LICENSE Version 1.1 の内容は、アーカイブに同梱の LICENSE_OFL.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/SIL_Open_Font_License_1.1  
  
Apache 2.0 License の内容は、アーカイブに同梱の LICENSE_Apache.txt に記載されています。  
この日本語訳は、以下から参照することができます。  
http://sourceforge.jp/projects/opensource/wiki/licenses%2FApache_License_2.0  
  
M+ OUTLINE FONTS のグリフは、同梱のファイル LICENSE_M+.txt に記載された自由なM+ FONTS LICENSE に基づき使用しています  
  
  
・Myrica は、M+ OUTLINE FONTS にないグリフを源ノ角ゴシックで補い、ASCII文字をInconsolataで置換えたフォントです。  
・フォントデータに含まれる、源ノ角ゴシック由来の文字グリフの著作権は Adobe が所有しています。  
・フォントデータに含まれる、M+ OUTLINE FONTS 由来の文字グリフの著作権は M+ FONTS PROJECT が所有しています。  
・フォントデータに含まれる、Inconsolata 由来の文字グリフの著作権は Raph Levien, Cyreal が所有しています。  
  
  
## M+ 由来の文字について  
---- Mgen+ の README より抜粋 ----  
> このバージョンでは、M+ OUTLINE FONTS 2014 年 8 月 3 日時点での CVS 版をベースとしています。  
> TESTFLIGHT-058 の漢字に加え、新たに制作された以下の漢字を含んでいます。  
>  
> 瘴嬲嫐娶夥埒嚼嚥臙讌叭釟冪匍匐僥潛僭譖獰湜懿點鈞繼爀璇騫勳粱岺岑邙玟泮悳乭儺攤柰  
> 璨娜拏贊讚鑽瓚盡儘燼贐賣囮皺鄒猜睛蜻闢  
>  
> M+ 由来の漢字グリフは 4,859 字がこのフォントに収録されており、それ以外の漢字は源ノ角ゴシックがベースとなっています。  
  
  
## 名前の由来  
・Mgen+ 作者の MM氏  
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
  
Mgen+  
http://jikasei.me/font/mgenplus/  
  
源ノ角ゴシック (Source Hans Sans)  
http://store1.adobe.com/cfusion/store/html/index.cfm?store=OLS-JP&event=displayFontPackage&code=1967  
  
Migu  
http://mix-mplus-ipa.sourceforge.jp/migu/  
  
Inconsolata  
https://www.google.com/fonts/specimen/Inconsolata  
  
Ricty  
https://github.com/yascentur/Ricty  
  
  
## 改版履歴  
  
#### Version 1.008.20140915  
  
・漢字とASCII文字を除く JIS0208 / JIS0213 の文字に、ヒンティング情報を付加  
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
