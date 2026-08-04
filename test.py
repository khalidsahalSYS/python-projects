"""import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('WELKOM')],
            [sg.Text('NameUser' ), sg.InputText()],
            [sg.Text('Password '), sg.InputText("")],
            [sg.Button('Ok'), sg.Button('Cancel'),sg.Button('oky admn')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('name user:', values[1]," \n","password²:", values[0])
    
    

window.close()
"""
