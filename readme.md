# ✏️ Digit Recognizer

Digit Recognizer is a desktop application that identifies handwritten digits drawn on a canvas and predicts the number using a trained Convolutional Neural Network (CNN) model.

---

## 🚀 Overview

This project combines machine learning with a graphical user interface to provide a simple and interactive way to test handwritten digit recognition. The backend model is built using **TensorFlow** and trained on the **MNIST dataset**, while the frontend interface is developed using **Tkinter**.

---

## 🧠 How It Works

1. **Draw a Digit**  
   Users draw a digit (0–9) on the provided canvas using the mouse.

2. **Preprocessing**  
   The drawing is saved using **Pillow**, converted to grayscale, resized to 28x28 pixels, and reshaped to match the model's input requirements.

3. **Prediction**  
   The model is loaded from a saved file and used to predict:
   - The most likely digit
   - The associated confidence
   - The second most likely digit

4. **Reset and Predict**  
   - `Reset` button clears the canvas.
   - `Predict` button triggers prediction.

---

## 🧱 Tech Stack

- **Frontend**: Tkinter (Python GUI library)
- **Backend**: TensorFlow with Keras
- **Image Processing**: Pillow (PIL fork)

---

## 🧪 Model Details

- **Architecture**: Convolutional Neural Network (CNN)
- **Layers**: 4 `Conv2D` layers
- **Dataset**: [MNIST dataset](https://keras.io/api/datasets/mnist/) from Keras
- **Training**:
  - Batch size: 64
  - Trained over: 11 epochs
- **Storage**:
  - Model is saved using TensorFlow’s `.save()` functionality
  - Loaded dynamically in the application

---

## 🔄 Modifying the Model

To retrain or modify the CNN architecture:
1. Open the `Model.py` file.
2. Adjust the model layers, compile settings, or training parameters.
3. Retrain the model with the MNIST dataset or your own data.
4. Save the updated model to be used in the application.

---

## 🖥️ Running the Application

### 📦 Prerequisites

Ensure you have Python 3.x installed and the following packages:
- bash
- pip install tensorflow pillow
- Tkinter is included with most Python installations. If not, install it via your system’s package manager.

▶️ Launch

Run the main application file:

python app.py

📸 Features

    🖌 Interactive Canvas
    Draw digits directly with the mouse.

    📤 Image Preprocessing
    Automatically converts canvas drawing to 28x28 grayscale image.

    🔍 Accurate Predictions
    Shows top prediction, prediction confidence, and the second-highest probability digit.

    🧼 Reset Capability
    Easily clear the canvas to try a new digit.

📁 File Structure

.
├── app.py            # Main application file with UI logic
├── Model.py          # Contains CNN model architecture and training code
├── saved_model/      # Directory containing the trained model
├── utils.py          # Optional: preprocessing and helper functions

🎓 Educational Purpose

This project was built for learning and demonstration purposes. It illustrates how deep learning models can be integrated with simple user interfaces to create interactive applications.
📄 License

This project is licensed for educational and personal use only.
Commercial use and redistribution are not permitted.
🙌 Acknowledgments

    MNIST Handwritten Digits Dataset

    TensorFlow

    Tkinter

    Pillow (PIL Fork)
