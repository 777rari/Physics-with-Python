#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:17:48 2024

@author: Isaac

"""

from vpython import *
import numpy as np

# Constants
G = 6.674e-11  # Gravitational constant
M = 10  # Mass of the ring in kg
radius = 1  # Radius of the ring in meters
segments = 100  # Number of segments to divide the ring into
segment_mass = M / segments  # Mass of each segment

# User input for point mass location
x = float(input("X coordinate of point mass (meters): "))
y = float(input("Y coordinate of point mass (meters): "))
z = float(input("Z coordinate of point mass (meters): "))

# Scene setup
#scene = canvas()

# Create the ring
ring_points = []
for i in range(segments):
    theta = 2 * np.pi * i / segments
    pos = vector(radius * np.cos(theta), radius * np.sin(theta), 0)
    point = sphere(pos=pos, radius=0.02, color=color.white)
    ring_points.append(point)

# Point mass
point_mass = sphere(pos=vector(x, y, z), radius=0.05, color=color.red)

# Calculate force
force_vector = vector(0, 0, 0)
for point in ring_points:
    r = point_mass.pos - point.pos
    force_magnitude = G * segment_mass / mag2(r)
    force_vector += norm(r) * force_magnitude

# Display force
force_arrow = arrow(pos=point_mass.pos, axis=force_vector.norm() * 0.2, color=color.green, shaftwidth=0.02)

# Print results
print("Force magnitude", mag(force_vector))
print("Force direction", force_vector.norm())
#print(f"Force magnitude: {mag(force_vector)} N")
#print(f"Force direction: {force_vector.norm()}")

