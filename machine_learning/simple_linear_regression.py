import numpy as np
import matplotlib.pyplot as plt

# Original data
x = np.array([50, 80, 120])
y = np.array([300, 450, 600])

# Data normalization
x_max = max(x)
y_max = max(y)
x = x / x_max
y = y / y_max

# Parameter initialization
w = 0
b = 0


def predict(x, w, b):
    return w * x + b


def cost_function(x, y, w, b):
    m = len(x)
    sum_error = sum((predict(x[i], w, b) - y[i]) ** 2 for i in range(m))
    return sum_error / m


def gradient(x, y, w, b, alpha):
    m = len(x)
    dw = sum((predict(x[i], w, b) - y[i]) * x[i] for i in range(m)) / m
    db = sum((predict(x[i], w, b) - y[i]) for i in range(m)) / m
    w -= alpha * dw
    b -= alpha * db
    return w, b


def train(x, y, w, b, alpha, epochs):
    for i in range(epochs):
        w, b = gradient(x, y, w, b, alpha)
        if i % 10000 == 0:
            print(f"Iteration {i}: Error = {cost_function(x, y, w, b):.6f}")
    return w, b

# Training with a smaller alpha


w, b = train(x, y, w, b, alpha=0.01, epochs=100000)

# Denormalization
size = 80
normalized_size = size / x_max  # Normalize size before passing to the function

predicted_price = predict(normalized_size, w, b) * y_max  #  Denormalize the price

print(f"For a house of {size} square meters, the predicted price is {predicted_price:.3f} thousand")

# Plotting the graph
plt.scatter(x * x_max, y * y_max, color='red', label="Original Data")  

# Denormalize points

x_reg = np.linspace(min(x), max(x), 100)  # Normalized values for the line
y_reg = predict(x_reg, w, b) * y_max  # Denormalize prediction
plt.plot(x_reg * x_max, y_reg, color='blue', label="Linear Regression")  # Denormalize the line
plt.xlabel("Size (m²)")
plt.ylabel("Price (thousand)")
plt.legend()
plt.show()

