import pyxel

pyxel.init(160, 120)

# フレーム処理
def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

# 描画処理
def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)