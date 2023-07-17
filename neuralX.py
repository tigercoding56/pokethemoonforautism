import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

# Load data from CSV file
#data = np.loadtxt("input_output_pairs.csv", delimiter=",")
#X = data[:, 0:2]  # Input data
#Y = data[:, 2:4]  # Output data
X = np.array([[2, 1], [4, 2], [5, 3], [5, 3]])
Y = np.array([[1], [2], [3], [4]])
# Define the neural network architecture
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(2, activation='linear'))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X, Y, epochs=1000, batch_size=10)

# Test the model on a new input
x_new = np.array([[0.5, 0.3]])
y_new = model.predict(x_new)
print(f"Input: {x_new}, Output: {y_new}")