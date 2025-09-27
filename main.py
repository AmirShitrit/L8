import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# true slope & intercept
n = 1000               # number of points
mu_x, mu_y = 0.0, 0.0  # means
sigma_x, sigma_y = 1.0, 2.0  # standard deviations

x = rng.normal(mu_x, sigma_x, n)
y = rng.normal(mu_y, sigma_y, n)

data = np.column_stack((x, y))  # shape (n, 2)# shape (1000,2)

# Means of x and y
x_mean = np.mean(data[:, 0])
y_mean = np.mean(data[:, 1])

# Least-squares slope and intercept
numerator = np.sum((data[:, 0] - x_mean)*(data[:, 1] - y_mean))
denominator = np.sum((data[:, 0] - x_mean) ** 2)

a = numerator / denominator
b = y_mean - a * x_mean

# Plot
plt.figure(figsize=(6, 6))
x1 = np.linspace(data[:,0].min(), data[:,0].max(), 100)
y1 = a * x1 + b
plt.plot(x1, y1, 'b-', linewidth=2)
plt.scatter(data[:, 0], data[:, 1], s=10, alpha=0.6, c='red')
plt.title("Random Points in 2D Plane")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
