# MACROPAD Hotkeys: Code test for Cory
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
#from bitmap_font_forkawesome_icons import microchip, python, terminal # issue does not display

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Coding',          # Application name
    'macros' : [                # List of button macros...
        
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'x', [Keycode.ESCAPE]),
        (0x002888, 'run code', [Keycode.F5]),
        (0x000000, '', []),

        # 2nd row ----------
        (0x100010, 'goto', [Keycode.F12]),
        (0x100018, 'rename', [Keycode.CONTROL, 'r', Keycode.CONTROL, 'r']),
        (0x100012, 'find', [Keycode.CONTROL, 'f']),
        
        # 3rd row ----------
        (0x002000, 'save', [Keycode.CONTROL, 's']),
        (0x045020, '+ class', [Keycode.CONTROL, Keycode.SHIFT, 'a']),
        (0x000000, '', []),
        
        # 4th row ----------
        (0x841123, 'Copy', [Keycode.CONTROL, 'c']), # copy
        (0x855668, 'Paste', [Keycode.CONTROL, 'v']), # paste
        (0x404222, '< Undo', [Keycode.CONTROL, 'z']), # undo?
        
        # Encoder button ---
        (0x000000, '', []) #
    ]
}
