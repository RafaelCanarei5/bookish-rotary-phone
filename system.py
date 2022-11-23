import time
from PySimpleGUI import PySimpleGUI as sg # Did you wanna graphics or not?! So, use this!

font = ("Segoe UI", 18)

sg.theme("DarkTeal7") # The theme incorporates the system style.
layout = [
  [sg.Text("11:38", font = font)],
  [sg.Button("📧", border_width = 0, font = font)],
  [sg.Button("📔", border_width = 0, font = font)]
]

PyWindow = sg.Window("PalmOS", layout)

while True:
  events, values = PyWindow.Read()
  if events == sg.WIN_CLOSED:
    break
