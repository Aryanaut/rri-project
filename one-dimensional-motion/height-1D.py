import matplotlib.pyplot as plt
import numpy as np

# Setting up graph
fig, ax = plt.subplots()

# Constants
g = 9.8

u = int(input("Initial Velocity: "))
t = int(input("Time period: "))

# Setting initial variables

h = 0
t0 = 0
xCoords = [0]
yCoords = [0]

while h >= 0:
    xCoords.append(t0)
    h = (u * t0) + (0.5 * g * (t0 ** 2))
    yCoords.append(h)
    t0 += 1

ax.plot(xCoords, yCoords)
plt.show()