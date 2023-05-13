import secrets
import string

import PySimpleGUI as sg


def generate_password(length, include_symbols):
    alphabet = string.ascii_letters + string.digits
    if include_symbols:
        alphabet += string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

sg.theme('DefaultNoMoreNagging') # テーマの設定

layout = [
    [sg.Text('Length:'), sg.Spin([_ for _ in range(4, 201)], initial_value=16, size=(5, 1))],
    [sg.Checkbox('Include Symbols', default=True)],
    [sg.Button('Generate'), sg.Button('Exit')],
    [sg.Text('Password:'), sg.InputText(key='-PASSWORD-', size=(30, 1))]
]

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    window['-PASSWORD-'].update(generate_password(int(values[0]), values[1]))

window.close()
