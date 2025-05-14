import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("🌌 Gravitational Lensing Simulator")

# User controls
strength = st.slider("Gravitational Strength", 0.01, 0.5, 0.15, 0.01)
lens_x = st.slider("Lens X Position", -1.5, 1.5, 0.0, 0.1)
lens_y = st.slider("Lens Y Position", -1.5, 1.5, 0.0, 0.1)

# Grid setup
grid_size = 500
x = np.linspace(-2, 2, grid_size)
y = np.linspace(-2, 2, grid_size)
X, Y = np.meshgrid(x, y)
eps = 0.05
R = np.sqrt((X - lens_x)**2 + (Y - lens_y)**2) + eps

# Lensing distortion
X_lensed = X - strength * (X - lens_x) / R**2
Y_lensed = Y - strength * (Y - lens_y) / R**2

# Background (concentric light wave effect)
background = np.sin(10 * (X_lensed**2 + Y_lensed**2))

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(background, cmap='inferno', origin='lower', extent=(-2, 2, -2, 2))
ax.set_title("Simulated Light Distortion Around a Massive Object")
ax.axis('off')
st.pyplot(fig)