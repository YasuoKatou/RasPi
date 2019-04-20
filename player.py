#-*- cording: utf-8 -*-

import pygame.mixer
from pathlib import Path
import sys
import time

#print('カレントディレクトリ', Path.cwd())

args = sys.argv
p = Path.cwd() / args[1] / args[2]
#print(p)

# 再生リストの作成
mp3_list = list(p.glob("*.mp3"))
list_num = len(mp3_list)

# mixerモジュールを初期化
pygame.mixer.init()

# １曲目を再生
mp3 = mp3_list.pop(0)
mp3_no = 1
print('({}/{}) {}'.format(mp3_no, list_num, mp3.name))
pygame.mixer.music.load(str(mp3))
pygame.mixer.music.play()
#pygame.mixer.music.set_volume(1.0)

# ２曲目以降を再生待ちリストに設定
#while len(mp3_list) > 0:
#  mp3 = str(mp3_list.pop(0))
#  print(mp3)
#  pygame.mixer.music.queue(mp3)

try:
  scnt = 0
  while scnt < 3600/5:
    time.sleep(5)
    if not pygame.mixer.music.get_busy():
      if len(mp3_list) > 0:
        mp3 = mp3_list.pop(0)
        mp3_no += 1
        print('({}/{}) {}'.format(mp3_no, list_num, mp3.name))
        pygame.mixer.music.load(str(mp3))
        pygame.mixer.music.play()
      else:
        break
except KeyboardInterrupt:
  pass

# 再生を停止する
pygame.mixer.music.stop()
print('stop player')

#[EOF]
