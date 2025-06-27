# Poultry-Health-Hub-

# Healthy vs Rotten Classifier - Flask App

📁 Project Structure

 # app.py
 # healthy_vs_rotten.h5         # Trained model
 # ipython.html                 # Image prediction UI
 # Readme.txt
 # templates/(blog.html,blog-single.html,index.html, portfolio-details.html)
# static/(assets, forms,uploads)


🧠 Description

This web application allows users to upload an image of food or waste,
and the model classifies it as "Healthy" or "Rotten" using transfer learning (VGG16).

Flask is used as the backend framework and Keras is used for building the deep learning model.

✅ Features:
- Upload image and get instant classification
- View model predictions
- Basic blog and portfolio pages


⚙️ How to Run
---------------------
1. Install dependencies:

    pip install flask tensorflow keras pillow

2. Run the Flask app:

    python app.py

3. Open in browser:

    http://127.0.0.1:5000/ipython


📌 Notes
---------------------
- Make sure `healthy_vs_rotten.h5` is in the root directory.
- Uploaded images will be stored in `/static/uploads/`.
- You can edit `ipython.html` for custom UI changes.


🔧 Model Info
---------------------
- Based on VGG16 (transfer learning)
- Trained on custom dataset with two classes:
    - Healthy
    - Rotten
# project details:
Team ID : LTVIP2025TMID41509

Team Size : 3

Team Leader : Vaddimeyani Ajay Kumar

Team member : Vadlamudi Bavanchandu , Y Lavanya 
