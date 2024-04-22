from passwordgenerator import password_generator
import pyperclip
import PySimpleGUI as sg

sg.theme("DarkBrown4")
layout = [
    [sg.Text("Password Generator")],
    [sg.Text("How many characters should the password contain?")],
    [sg.Input(key="passwordLength")],
    [sg.Text("Password type:\n1. Numerical\n2. Alphabetical\n3. Alphanumerical\n4. Alphanumerical + Symbols")],
    [sg.Spin(values=(1,2,3,4),initial_value=1,key="passwordType",size=(10,1))],
    [sg.Button("Confirm", key="Button")]
]

window = sg.Window("Password Generator V1.0", layout)

while True:
   event, values = window.read()
   if event == sg.WINDOW_CLOSED or event == "Exit":
      break
   elif event == "Button":
      global passwordLength
      global passwordType
      passwordLength = values["passwordLength"]
      passwordType = values["passwordType"]
      if passwordLength != int(passwordLength) or passwordType != int(passwordType):
         passwordLength,passwordType = int(passwordLength),int(passwordType)
         if passwordLength < 0 or (passwordType < 1 or passwordType > 4):
            sg.Popup("Out of range. Please try again!")
      password_generator.generatePassword(passwordLength,passwordType)
      window.close()
      updated_layout = [
         [sg.Text(f"Your generated password:\n{password_generator.password}")],
         [sg.Button("Copy", key="Copy")]
      ]
      window = sg.Window("Copy to clipboard?", updated_layout)
   elif event == "Copy":
      try:
         pyperclip.copy(password_generator.password)
         sg.Popup("Copied!")
      except pyperclip.PyperclipException as e:
            sg.Popup(f"Error copying to clipboard: {e}")
   
