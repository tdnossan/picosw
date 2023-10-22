import time, board, digitalio, usb_hid
from adafruit_hid.keyboard import Keyboard, Keycode

kb = Keyboard(usb_hid.devices)
btn = digitalio.DigitalInOut(board.GP28)
btn.pull = digitalio.Pull.UP # プルアップ抵抗有効化
led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT
press = False

while 1:
    # ボタンが押されたら
    if not(btn.value):
        if not(press):
            press = True
            # LED点灯
            led.value = True
            # キーボード入力
            kb.send(Keycode.F12)
            print("press")
            time.sleep(0.1)
        else:
            print("longpress")
            time.sleep(0.1)
    else:
        #print("release")
        led.value = False
        press = False
    
