# ラズパイ + pygame.mixer でmp3を再生

## 使い方
```
$ python3 player.py {アーティスト} {アルバム}
```
* {アーティスト} / {アルバム} 配下のmp3ファイルを順次再生します
* mp3の再生が終了するとプログラムも終了します
* ラズパイからは、イヤホンジャック経由で出力されます

## キュー対応
参考にさせて頂いたさいとでは、再生時間からsleep時間を決定しているようでした。本プログラムでは、pygame.mixer.music.get_busy を使って再生の終了を一定周期で監視するようにしました。

## 今後の展開
* 検討中（１アルバムごとにプログラムの起動が必要で、面倒と思っています）


#### 参考にさせて頂いたサイト
* [Raspberry Piで音楽(wav/mp3)ファイルを再生する方法 python編](https://qiita.com/Nyanpy/items/cb4ea8dc4dc01fe56918)
* [pygame.mixer.music](http://westplain.sakuraweb.com/translate/pygame/Music.cgi)
* [raspberry pi(raspbian)で「pygame.mixer.music.queue」が動かない話](http://indigo-heron.hatenablog.com/entry/2017/02/02/092029)