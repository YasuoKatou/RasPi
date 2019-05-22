# -*- coding:utf-8 -*-
from pathlib import Path
import shutil

_root_user_play_list = Path.cwd() / 'test'
_root_player = Path.cwd()
_ext_playlist = 'playlist'
_play_info = 'play.info'

#print(_root_player)

def _checkPlayListFiles(fn):
	'''
	再生待ちおよび再生中のプレイリストの存在を確認する
	確認するファイルが再生待ちのみ存在する場合、
	再生待ちから削除する。
	'''
	# 再生中プレイリストを確認
	p = Path(_root_player / fn)
	if not p.exists():
		print('再生中プレイリストがない')
		# 再生中プレイリストが無い時、
		# 再生待ちのプレイリストを削除
		p = Path(_root_user_play_list / fn)
		if p.exists():
			print('再生待ちのプレイリストを削除')
			p.unlink()
		return False
	# 再生待ちプレイリストを確認
	p = Path(_root_user_play_list / fn)
	if p.exists():
		return True
	return False

def _cleanPlayList(p):
	'''
	指定フォルダ内のプレイリストを全て削除する
	'''
	path = Path(p)
	print('clean up play list at ' + path.name)
	cnt = 0
	for i in path.glob('*.' + _ext_playlist):
		i.unlink()
		print('removed ' + i.name)
		cnt += 1
	print('clean up play list files ('+str(cnt)+')')

def _updatePlayListNo(pinf):
	'''
	再生情報ファイルを更新(上書き)する.
	'''
	pinf[2] = str(int(pinf[2]) + 1)
	p = Path(_root_player / _play_info)
	with p.open(mode='w', encoding='utf-8') as f:
		f.write('\n'.join(pinf))
	

def _nextPlayList(pinf):
	'''
	次の再生情報を取得する.
	'''
	# 再生中のプレイリストを読む
	p = Path(_root_player / pinf[1])
	with p.open(encoding='utf-8') as f:
		b = f.read()
	ml = b.strip().split('\n')
	# 再生中プレイリストに残があるか確認
	no = int(pinf[2])
	if len(ml) > no:
		# 再生残がある場合、戻り値に次の曲を設定
		r = ml[no]
		# 再生情報ファイルの更新
		_updatePlayListNo(pinf)
		return r
	else:
		p = Path(_root_user_play_list / pinf[1])
		p.unlink()
		print('no more play at ' + pinf[1])
		return None

def _copyPlayList():
	'''
	プレイリストを再生中プレイリストコピーする.
	'''
	# 再生中プレイリストを全て削除
	_cleanPlayList(_root_player)

	# 再生待ちプレイリストを確認
	p = Path(_root_user_play_list)
	pl = sorted(p.glob('*.' + _ext_playlist))
	if len(pl) == 0:
		# 再生待ちプレイリストが無い
		print('再生待ちプレイリストが無い')
		return None

	# 再生待ちを再生中プレイリストにコピー
	src = pl[0]
	shutil.copy2(src, _root_player)

	# 再生情報ファイルの初期化
	fn = Path(src).name
	p = Path(_root_player / fn)
	with p.open(encoding='utf-8') as f:
		b = f.read()
	ml = b.strip().split('\n')
	p = Path(_root_player / _play_info)
	with p.open(mode='w', encoding='utf-8') as f:
		f.write('\n'.join(['play information', fn, '1']))
	return ml[0]

def checkPlayList():
	'''
	プレイリストの確認を行う
	'''
	# 再生情報ファイルを確認
	p = Path(_root_player / _play_info)
	if p.exists():
		# 再生情報ファイルを読む
		with p.open(encoding='utf-8') as f:
			b = f.read()
		pinf = b.strip().split('\n')
		print(pinf)
		if _checkPlayListFiles(pinf[1]):
			# 再生中プレイリストありの場合、
			# 次の曲を決定
			r = _nextPlayList(pinf)
			if r:
				return r
			return _copyPlayList()
		else:
			return _copyPlayList()
	else:
		print('再生情報ファイルが無い')
		# 再生情報ファイルが無い場合、再生待ちプレイリストを確認
		return _copyPlayList()

if __name__ == '__main__':
	print('>>> start check play list')
	r = checkPlayList()
	print('next : ' + str(r))

#[EOF]
