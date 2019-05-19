# -*- coding:utf-8 -*-
from pathlib import Path

import logging

_Log = logging.getLogger(__name__)

def makeFileList(root, fext, outFile):
	with Path(outFile).open(mode='w', encoding='utf-8') as f:
		f.write('ver 1.0.0\n')
		# アーティストでループ
		rp = Path(root)
		for a in rp.iterdir():
			if a.is_dir():
				al = len(str(a))
				# アルバムでループ
				f.write('1,{}\n'.format(a.name))
				for ab in a.iterdir():
					f.write('2,{}\n'.format(str(ab)[al+1:]))
					abl = len(str(ab))
					for mf in ab.glob('**/*.' + fext):
						f.write('3,{}\n'.format(str(mf)[abl+1:]))

def readMPList(fp):
	with Path(fp).open(encoding='utf-8') as f:
		for ln in f:
			_Log.debug(ln.strip())

def findFileList(root, fext):
	rp = Path(root)
	# アーティストでループ
	for a in rp.iterdir():
		if a.is_dir():
			al = len(str(a))
			# アルバムでループ
			_Log.debug('【' + a.name + '】')
			for ab in a.iterdir():
				_Log.debug('>' + str(ab)[al+1:])
				abl = len(str(ab))
				for f in ab.glob('**/*.' + fext):
					_Log.debug(str(f)[abl+1:])

def processTime(st, et, cmt):
	tm = et - st
	_Log.info(cmt + str(tm.seconds*1000 + tm.microseconds/1000) + ' ms')

if __name__ == '__main__':
	import datetime
	# コマンドから起動した場合
	#logging.basicConfig(level=logging.DEBUG)
	logging.basicConfig(level=logging.INFO)

	#ファイル一覧を取得する
	st = datetime.datetime.now()
	findFileList(u'/home/pi/usbHDD/music', 'mp3')
	processTime(st, datetime.datetime.now(), '楽曲一覧取得時間 : ')

	#ファイル一覧を作成する
	mpList = u'/home/pi/usbHDD/music/all.list'
	st = datetime.datetime.now()
	makeFileList(u'/home/pi/usbHDD/music', 'mp3', mpList)
	processTime(st, datetime.datetime.now(), '楽曲一覧作成時間 : ')

	st = datetime.datetime.now()
	readMPList(mpList)
	processTime(st, datetime.datetime.now(), '楽曲一覧読込時間 : ')

#[EOF]
