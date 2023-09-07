import numpy as np
import pickle
import pygame
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
# Load the trained model from the pickle file
with open('neural_network.pkl', 'rb') as f:
    neural_network = pickle.load(f)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((320, 320))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Grid dimensions
GRID_SIZE = 16
PIXEL_SIZE = 20
GRID_PADDING = 2

# Initialize the grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Function to update the grid based on user input
def update_grid(pos):
    x = pos[0] // (PIXEL_SIZE + GRID_PADDING)
    y = pos[1] // (PIXEL_SIZE + GRID_PADDING)
    grid[y, x] = 1 - grid[y, x]

# Function to draw the grid on the screen
def draw_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(
                x * (PIXEL_SIZE + GRID_PADDING),
                y * (PIXEL_SIZE + GRID_PADDING),
                PIXEL_SIZE,
                PIXEL_SIZE
            )
            if grid[y, x] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

# Normalize the input
def normalize_input(grid):
    return grid / 255.0

# Make predictions
def predict_output(grid):
    normalized_input = normalize_input(grid)
    prediction = neural_network.predict(normalized_input.flatten().reshape(1, -1))
    return prediction[0]

# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                update_grid(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                prediction = predict_output(grid)
                print("Prediction:", prediction)
    
    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()