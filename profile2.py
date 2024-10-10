import PySimpleGUI as sg
sg.theme("DarkTeal1")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",

layout=[[sg.Text("SELAMAT DATANG DI KELAS",

font=("Arial",25))],

[sg.Text("NPM : 2210010459")],
[sg.Text("Nama : Nurqona'ah Hidayah Satyaputri ")],
[sg.Text("Kelas : 5P Regular Banjarmasin ")]
],

size=(500,200),
font=("Times", 18))

window()
window.close()