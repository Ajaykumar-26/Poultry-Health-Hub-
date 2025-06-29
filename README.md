# PoultryGuard – A Deep Learning-Powered Web App for Poultry Disease Prediction using Transfer Learning.
# https://ornate-puppy-6f0f00.netlify.app/
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

💾 5. Model Saving model.save("poultry_model.h5")
# 📂 Project Structure The project directory (C:poultry detect/) is organized as follows:
transfer learning-based classification of poultry diseases for enhanced/

app.py

trained_model.h5

static/(Assets,forms,uplods)

templates/(index.html, result.html)

dataset/(Train,Test,Val,etc. folders)

model/(Classification Report)

README.md

🚀 How to Run the Application Ensure all setup steps are completed (prerequisites and installation).
Place your trained model file (trained_model.h5) directly in the C:\poultary health hub, next to app.py.
Generate the Interactive Project Overview HTML: Run the conversion script to create templates/README_interactive_overview.html:
python convert_readme.py

Open Google colab,
Navigate to your project's root directory:
cd C:\poultry detect 

Activate your google collab :
run the code and get the expexted output 

Start the Flask application:
python app.py
You should see output similar to this, indicating the server is running and the model loaded:

✅ Model loaded successfully from C:\poultry health hub\trained_model.h5
Serving Flask app 'app'
Debug mode: on
Running on all addresses (0.0.0.0)
Running on http://127.0.0.1:5000/
Running on http://YOUR_LOCAL_IP:5000 Press CTRL+C to quit

💻 Usage Once the Flask application is running, open your web browser:
poultry detect Classification Tool:
Go to http://127.0.0.1:5000/ (for access from your local machine).
If running on 0.0.0.0, others on your same local network can access it using your computer's local IP address.
On the page, click "Choose File", select a blood cell image (JPEG or PNG), and click "Classify Image" to see the prediction.
Interactive Project Overview (README):
Go to http://127.0.0.1:5000/project-overview in your browser.
This page provides a comprehensive, interactive overview of the project's details, features, and technical aspects.

# Project Lead: Vaddimeyani Ajaykumar
# Team ID : LTVIP2025TMID41509
# Team members : Vadlamudi Bavanchandu ,Y Lavanya
# Email : Ajaykumarv2609@gmail.com
# Smart Bridge Internship: https://apsche.smartinternz.com/ Developed as part of the Smart Bridge Artificial Intelligence and Machine learning Internship Program
# Demolink: https://drive.google.com/file/d/1pTcaClWY4CO2W57iC9vSlfgwn-49IzAe/view?usp=drivesdk
Developed as part of the Smart Bridge AI Internship Program.
⚙ Installation
git clone https://github.com/Ajaykumar-26/Poultry-Health-Hub-/tree/main?tab=readme-ov-file
cd PoultryGuard

# Create environment
conda create -n poultryguard python=3.9
conda activate poultryguard

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
