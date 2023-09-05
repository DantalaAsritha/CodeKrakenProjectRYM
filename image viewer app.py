import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.photo = photo

window = tk.Tk()
window.title("Image Viewer")
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()
image_label = tk.Label(window)
image_label.pack()
window.mainloop()
