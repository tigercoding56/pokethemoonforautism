import numpy as np
import pickle

# Activation function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the activation function
def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights with random values
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)

    def forward(self, X):
        # Forward propagation
        self.hidden = sigmoid(np.dot(X, self.weights1))
        self.output = sigmoid(np.dot(self.hidden, self.weights2))
        return self.output

    def backward(self, X, y, learning_rate):
        # Backward propagation
        d_output = (y - self.output) * sigmoid_derivative(self.output)
        d_hidden = np.dot(d_output, self.weights2.T) * sigmoid_derivative(self.hidden)

        # Update weights
        self.weights2 += learning_rate * np.dot(self.hidden.T, d_output)
        self.weights1 += learning_rate * np.dot(X.T, d_hidden)

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, learning_rate)

    def predict(self, X):
        return np.round(self.forward(X))

# Generate training data
X_train = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # Add more training examples here...
])
y_train = np.array([[0], [1]])  # Corresponding labels (0 or 1)

# Initialize and train the neural network
input_size = X_train.shape[1]
hidden_size = 8
output_size = 1

neural_network = NeuralNetwork(input_size, hidden_size, output_size)
neural_network.train(X_train, y_train, epochs=10000, learning_rate=0.1)

# Save the trained model as a pickle file
with open('neural_network.pkl', 'wb') as f:
    pickle.dump(neural_network, f)