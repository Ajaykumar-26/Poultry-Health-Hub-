import tensorflow as tf
import numpy as np

# Dummy dataset (100 images of 224x224 RGB with 4 classes)
X = np.random.rand(100, 224, 224, 3)
y = np.random.randint(0, 4, size=(100,))

# Define your class labels
classes = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

# Create a simple CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(classes), activation='softmax')  # 4 output classes
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model on dummy data
model.fit(X, y, epochs=3)

# Save the model
model.save('model.h5')
print("✅ Model saved as model.h5")
