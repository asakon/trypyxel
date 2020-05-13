import pyxel

class App:
	def __init__(self):
		# アプリの画面サイズ。幅、高さ、キャプション
		pyxel.init(160, 120, caption="Catio")

		# load image
		pyxel.image(0).load(0, 0, "assets/cat_16x16.png")

		# アプリの開始 
		pyxel.run(self.update, self.draw)

	# フレーム処理
	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()


	def draw(self):
		# 画面を色でクリアする
		pyxel.cls(7)
		pyxel.text(55, 41, "Catio Brosse", 8)
		# blt(x, y, img, u, v, w, h, [colkey])
		pyxel.blt(61, 66, 0, 0, 0, 16, 16)


App()