print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP15,board.GP9,board.GP8,board.GP6,board.GP3,board.GP0,board.GP1,board.GP2,board.GP4,board.GP5,board.GP7)
keyboard.row_pins = (board.GP10,board.GP11,board.GP12,board.GP14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

# Layer 0: Physical Layout
#   TG                                             BKSP
#   ESC  Q    W    E    R   T   Y    U    I  O     P
#   TAB  A    S    D    F   G   H    J    K  L     /
#   LSFT Z    X    C    V   B   N    M    ,  .     ENT
#        LCTL LALT LGUI FN  SPC LEFT DOWN UP RIGHT

FN = KC.MO(1)

keyboard.keymap = [
    [# layer 0: Base
        KC.TG(1),  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,     KC.U,     KC.I,    KC.O,       KC.BSPC,
        KC.ESC,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,     KC.J,     KC.K,    KC.L,       KC.P,
        KC.TAB,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,     KC.M,     KC.COMM, KC.DOT,     KC.SLSH,
        KC.LSFT,   KC.LCTL, KC.LALT, KC.LGUI, FN,      KC.SPC,  KC.LEFT,  KC.DOWN,  KC.UP,   KC.RIGHT,   KC.ENT,
    ],
    [# layer 1: Terminal Symbols & CLI Nav
        KC.TRNS,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,    KC.N7,    KC.N8,   KC.N9,      KC.DEL,
        KC.GRV,    KC.MINS, KC.EQL,  KC.LBRC, KC.RBRC, KC.PIPE, KC.SCLN,  KC.QUOT,  KC.BSLS, KC.TILD,    KC.NO,
        KC.F1,     KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,    KC.F8,    KC.F9,   KC.F10,     KC.F12,
        KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.HOME,  KC.PGDN,  KC.PGUP, KC.END,     KC.TRNS,
    ]
]

if __name__ == '__main__':
    keyboard.go()