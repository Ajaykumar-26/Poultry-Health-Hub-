# PoultryGuard – A Deep Learning-Powered Web App for Poultry Disease Prediction using Transfer Learning.

# PoultryGuard 🐔  
### A Deep Learning Odyssey in Poultry Disease Detection via Transfer Learning

This project is about creating a smart web application that can analyze an image of a chicken and predict the disease it might have. We use **Transfer Learning**, a powerful technique in **Artificial Intelligence**, to build a model trained on poultry images.

---

## 🚀 Features

- 🧠 **Transfer Learning** using MobileNetV2 / ResNet50
- 🐓 **Detects multiple poultry diseases**, e.g., Newcastle, Salmonella, Coccidiosis, etc.
- 🖼 Upload an image and get instant predictions
- 📊 Displays prediction result with confidence score
- 💻 Web interface built with Flask + HTML/CSS + Bootstrap
- 💾 Trained model saved as `poultry_model.h5`

---

## 🛠 Project Development Workflow

### 📁 1. Dataset Collection & Preparation
The dataset is organized in folders for each disease:

dataset/
├── Coccidiosis/
├── Salmonella/
├── Newcastle/
├── Marek/
├── Healthy/

yaml
Copy
Edit

- Each folder contains images labeled by disease.
- Data is cleaned and resized to 224x224 pixels.
- Augmentations used: rotation, flipping, zoom.

---

### 🧹 2. Preprocessing
- Images normalized to [0, 1] scale.
- 80-20 split between training and validation.
- Augmentation applied using Keras `ImageDataGenerator`.

---

### 🧠 3. Model Building
We use **Transfer Learning** with a pre-trained CNN model:

python
base_model = MobileNetV2(include_top=False, input_shape=(224,224,3), weights='imagenet')
Custom dense layers added.

Compiled with Adam, categorical_crossentropy, and accuracy.

# 📈 4. Model Evaluation
Accuracy & loss graphs plotted.

Confusion matrix + classification report generated.

Tested with unseen poultry images.

💾 5. Model Saving
python
Copy
Edit
model.save("poultry_model.h5")
🌐 Web App Preview
# Project Lead: Vaddimeyani Ajaykumar
# Team ID : LTVIP2025TMID41509
# Team members : Vadlamudi Bavanchandu Y Lavanya
# Email : Ajaykumarv2609@gmail.com
# Smart Bridge Internship: https://apsche.smartinternz.com/ Developed as part of the Smart Bridge Artificial Intelligence and Machine learning Internship Program
# Demolink: https://drive.google.com/file/d/1pTcaClWY4CO2W57iC9vSlfgwn-49IzAe/view?usp=drivesdk
Developed as part of the Smart Bridge AI Internship Program.
⚙ Installation
git clone https://github.com/yourusername/PoultryGuard.git
cd PoultryGuard

# Create environment
conda create -n poultryguard python=3.9
conda activate poultryguard

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
