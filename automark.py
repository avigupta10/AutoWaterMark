from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file = filedialog.askopenfilenames()  # shows dialog box and return the path

path = list(file)
os.makedirs("D:\\WatermarkedImages", mode=0o666, exist_ok=True)

watermark = str(input("Enter WaterMark Text --> "))

for path in path:
    # Create an Image Object from an Image
    im = Image.open(path)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = watermark

    font = ImageFont.truetype('Adalgisa Personal Use.ttf', 30)
    text_width, text_height = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - text_width - margin
    y = height - text_height - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill=(255, 0, 0, 255))

    head, tail = os.path.split(path)
    print(os.path.join(r"D:\WatermarkedImages", tail))
    # Save watermarked image
    outputfilename = os.path.join(r"D:\WatermarkedImages", tail)
    im.save(outputfilename, "JPEG")
    # im.show()
