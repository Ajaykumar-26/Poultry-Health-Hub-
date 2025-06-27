import numpy as np
import os
import tensorflow as tf
from flask import Flask, render_template, request
from keras.preprocessing.image import load_img

app = Flask(__name__)
model = tf.keras.models.load_model("model.h5")

UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ✅ Ensure folder exists

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def output():
    if 'image' not in request.files:
        return "No file uploaded", 400

    f = request.files['image']
    if f.filename == '':
        return "No selected file", 400

    img_path = os.path.join(UPLOAD_FOLDER, f.filename)
    f.save(img_path)

    img = load_img(img_path, target_size=(224, 224))
    image_array = np.array(img)
    image_array = np.expand_dims(image_array, axis=0)

    pred = np.argmax(model.predict(image_array), axis=1)
    labels = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'salmonella']
    prediction = labels[int(pred)]

    return render_template("result.html", prediction=prediction, image_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)