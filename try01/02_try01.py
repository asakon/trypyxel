import pyxel

class App:
	def __init__(self):
		# アプリの画面サイズ。幅、高さ、キャプション
		pyxel.init(160, 120, caption="Catio")

		# アプリの開始 
		pyxel.run(self.update, self.draw)

	# フレーム処理
	def update(self):
		pyxel.show()

	def draw(self):
		# 画面を色でクリアする
		pyxel.cls(0)


App()