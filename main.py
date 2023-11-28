import tkinter as tk
import random
from PIL import Image, ImageTk

def generate_key(input_number):
    key = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    shift_direction = 1

    for i in range(4):
        block = ''.join(random.choices(characters, k=5))
        key += block
        if i < 3:
            key += '-'

        shift = int(input_number % 10)
        input_number //= 10
        block = list(block)
        for j in range(shift):
            if shift_direction == 1:
                block = [block[-1]] + block[:-1]
            else:
                block = block[1:] + [block[0]]
        key += ''.join(block) 
        shift_direction *= -1 

    return key

root = tk.Tk()
root.title("Keygen")
root.geometry("450x400")

background_image = Image.open("bg_pic.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(root, text="Введите трехзначное число:")
label.pack()
entry = tk.Entry(root)
entry.pack()
result_label = tk.Label(root, text="")
result_label.pack()

def generate_button_click():
    try:
        input_number = int(entry.get())
        if 100 <= input_number <= 999:
            key = generate_key(input_number)
            result_label.config(text="Сгенерированный ключ: " + key)
        else:
            result_label.config(text="Пожалуйста, введите трехзначное число.")
    except ValueError:
        result_label.config(text="Пожалуйста, введите корректное число.")

generate_button = tk.Button(root, text="Сгенерировать", command=generate_button_click)
generate_button.pack()

root.mainloop()