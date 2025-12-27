# Import all the IOs of your board
import board
import busio

# KMK imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.oled import OLED
from kmk.modules.rgb import RGB

# Main keyboard instance
keyboard = KMKKeyboard()

# ========= Macros =========
macros = Macros()
keyboard.modules.append(macros)

# ========= Define Pins =========
# Direct-wired 2x2 matrix
PINS = [board.GP1, board.GP2, board.GP4, board.GP3]

# Initialize KeysScanner with direct pins
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # Adjust if your switches are active HIGH
)

# ========= Keymap =========
# 2x2 layout:
# SW1 SW2
# SW3 SW4
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]  # KMK treats each pin as a “button” in this mode
]

# ========= OLED =========
i2c = busio.I2C(board.GP6, board.GP29)  # SCL, SDA
oled_ext = OLED(i2c=i2c, width=128, height=32)
keyboard.modules.append(oled_ext)

# Function to display text
def oled_show(oled):
    oled.fill(0)
    oled.text("RP2040 Macropad", 0, 0, 1)
    oled.show()

oled_ext.draw = oled_show

# ========= RGB =========
rgb_ext = RGB(
    pixel_pin=board.GP7,
    num_pixels=2,
    brightness=0.47,  # 120/255
    auto_write=True
)
keyboard.modules.append(rgb_ext)

# Start the keyboard
if __name__ == '__main__':
    keyboard.go()
