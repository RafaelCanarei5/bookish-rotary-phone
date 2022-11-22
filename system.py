import time
from PySimpleGUI import PySimpleGUI as SG # Did you wanna graphics or not?! So, use this!

font = ("Candara", 12)

SG.theme("DarkTeal7") # The theme incorporates the system style.
layout = [
  [SG.Text(time.ctime, font = font)],
  [SG.Button("📧", border_width = 0)]
]

PyWindow = SG.Window("PalmOS", layout)

while True:
  events, values = PyWindow.Read()
  if events == SG.WIN_CLOSED:
    break
