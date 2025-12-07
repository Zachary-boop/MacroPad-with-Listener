import board
from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.D4,
    cdc=True,
    consumer_control=True,
    keyboard=True,
    midi=False,
    mouse=False,
    storage=False,
    usb_id=('Cegep de Sherbrooke - TGE', 'MacroPad'),
)

import usb_hid
usb_hid.disable()
