import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageDraw, ImageFont, ImageTk


def open_file():
    file_path = askopenfile(mode='rb', filetypes=[('PNG File', '*.png')])
    img = Image.open(file_path)
    img_resized = img.resize((200, 200))  # new width & height
    img = img_resized
    b2 = ImageTk.PhotoImage(img)  # using Button
    label1 = tkinter.Label(image=b2)
    label1.image = b2
    label1.grid(row=3, column=0)

    # the watermark
    water_label = Label(text="Your watermark")
    water_label.grid(row=4, column=0)
    text_entry = Entry(width=20)
    text_entry.grid(row=5, column=0, columnspan=2)

    def save():
        message = text_entry.get()

        font = ImageFont.truetype('Montserrat-Italic-VariableFont_wght.ttf', 36)

        img_editable = ImageDraw.Draw(img)
        img_editable.text((15, 15), message,(52, 88, 235), font=font)
        img.show()
        img.save("result.png")
    ok_button = Button(text="submit", command=save)
    ok_button.grid(row=6, column=0)


window = Tk()
window.title("Watermark App")
window.config(padx=10, pady=10)

import_button = Button(window, text='Upload picture', command=lambda: open_file())
import_button.grid(row=0, column=0)

window.mainloop()
