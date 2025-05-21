import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tkinter import *
from tkinter import Canvas, Button
from PIL import Image, ImageGrab
import numpy as np

# load model
model = keras.models.load_model('digit_recognizer.h5')
print(model.summary())

# make canvas
width = 16
height = 16
pixel_size = 16
canvas_size = 448

app = Tk()
app.geometry(f'{canvas_size}x{canvas_size}')


def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw(event):
    global lasx, lasy
    #canvas.create_line((lasx, lasy, event.x, event.y), fill='red')
    pixel_x = (lasx // pixel_size) * pixel_size
    pixel_y = (lasy // pixel_size) * pixel_size

    canvas.create_rectangle((pixel_x , pixel_y, pixel_x + pixel_size, pixel_y + pixel_size), outline='white', fill='white')
    lasx, lasy = event.x, event.y


def save(widget, filename):
    x=app.winfo_rootx()+widget.winfo_x()
    y=app.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)


def reset():
    canvas.delete("all")
    l.config(text="Predicted Number:", font=("Courier", 14))
    l2.config(text="Accuracy: ", font=("Courier", 14))
    l3.config(text="2nd Predicted Number:", font=("Courier", 8))

def predict_digit(image_path):
    save(canvas, "predict_image.png")
    img = Image.open(image_path)

    #resize image to 28x28 pixels
    img = img.resize((28,28))

    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1,28,28,1)
    img = img/255.0
    img = 1 - img


    #predicting
    res = model.predict([img])[0]
    print("Predicted Digit:", np.argmax(res))
    print("Accuracy:", max(res))
    l.config(text="Predicted Digit: " + str(np.argmax(res)), font=("Courier", 14))
    l2.config(text="Accuracy: " + str(max(res)), font=("Courier", 14))
    values, indices = tf.nn.top_k(res, 2)
    p = tf.stop_gradient(indices[1])
    print(p)
    l3.config(text="2nd Predicted Digit: " + str(np.argmax(p)), font=("Courier", 8))


top = Frame(app)
bottom = Frame(app)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


# save_button = Button(app, text="Save Image", width=10, height=2, command=lambda: save(canvas, "canvas_image.png"))
# save_button.pack(side=LEFT, padx=5, pady=10)

reset_button = Button(app, text="Reset Canvas", width=10, height=2, command=reset)
reset_button.pack(side=LEFT, padx=5, pady=5)

compare_button = Button(app, text="Compare", width=10, height=2, command=lambda: predict_digit("predict_image.png"))
compare_button.pack(side=LEFT, padx=5, pady=5)

compare_button.pack(in_=top, side=LEFT)
reset_button.pack(in_=top, side=LEFT)
# save_button.pack(in_=top, side=LEFT)


canvas = Canvas(app, bg='black')
canvas.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)
#canvas = Canvas(app, bg='black')
#canvas.pack(anchor='nw')

#print(os.path.abspath("saved_images"))

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw)


l = Label(app, text = "Predicted Number: ")
l2 = Label(app, text = "Accuracy: ")
l3 = Label(app, text = "2nd Predicted Number: ")
l.config(font =("Courier", 14))
l2.config(font =("Courier", 14))
l3.config(font =("Courier", 8))
l.pack()
l2.pack()
l3.pack()


app.mainloop()

# TODO
# make accuracy higher
