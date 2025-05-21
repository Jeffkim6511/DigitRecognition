Digit Recognizer is a program that determines the number written on the canvas.

CNN model was created using tensorflow and consists of 4 conv2d layers and 
model was fitted using the mnist dataset from
keras. Model was trained 11 times with a batch-size of 64. Model is then 
saved and loaded to the application. To alter
and change model, alter Model.py file. 

Application loads main model and predicts written number based on the canvas 
drawing. Canvas can be reset and predicted
using the buttons above and predicted number as well as accuracy and second 
most likely number is outputted. UI was 
created using Tkinter and Pillow is used to save canvas image and change 
picture to be 28x28. 
