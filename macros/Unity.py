# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT
#
# Unity Game Engine Shortcuts: by Cory Fabian

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

blue = 0x0037ff
purple = 0x008000FF
red = 0xff1100
grey = 0x575757
off = 0x0

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Unity Engine',    # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (purple, '7', ['7']),
        (red, '8', ['8']),
        (blue, '9', ['9']),
        # 2nd row ----------
        (grey, '4', ['4']),
        (0x0, '5', ['5']),
        (0x202000, '6', ['6']),
        # 3rd row ----------
        (0x202000, '1', ['1']),
        (0x202000, '2', ['2']),
        (0x202000, '3', ['3']),
        # 4th row ----------
        (0x002020, 'Prev', [Keycode.PAGE_UP]),
        (0x000000, '', []),
        (0x002020, 'Next', [Keycode.PAGE_DOWN]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
