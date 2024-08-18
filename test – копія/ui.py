import customtkinter
import code
from PIL import *

def button_callback():
    print("кнопка кликнута")

app = customtkinter.CTk()
app.geometry("400x150")
button_image = customtkinter.CTkImage(Image.open("microphone.png.png"), size=(26,26))
button = customtkinter.CTkButton(app, text="кликни", command=button_callback,image=button_image)
button.pack(padx=20, pady=20)


textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0","")
textbox.pack(padx = 20, pady = 20)

app.mainloop()