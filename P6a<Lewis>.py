#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:02:21 2024

@author: Isaac
"""
# Assignment #: Python Assignment P6a
#
# Programmer: Isaac Lewis
#
# Due Date: March 18, 2024
# PHYS 345, Spring 2024
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: This code calculates the gravitational force exerted by a ring on a point mass inside the ring, on the ring, and outside the ring.
# Input: X, Y, and Z positions of three different point masses
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
x2 = float(input("X_2 coordinate of point mass (meters): "))
y2 = float(input("Y_2 coordinate of point mass (meters): "))
z2 = float(input("Z_2 coordinate of point mass (meters): "))
x3 = float(input("X_3 coordinate of point mass (meters): "))
y3 = float(input("Y_3 coordinate of point mass (meters): "))
z3 = float(input("Z_3 coordinate of point mass (meters): "))


# Create the ring
ring_points = []
for i in range(segments):
    theta = 2 * np.pi * i / segments
    pos = vector(radius * np.cos(theta), radius * np.sin(theta), 0)
    point = sphere(pos=pos, radius=0.02, color=color.white)
    ring_points.append(point)

# Point mass
point_mass = sphere(pos=vector(x, y, z), radius=0.05, color=color.red)
point_mass2 = sphere(pos=vector(x2, y2, z2), radius=0.05, color=color.red)
point_mass3 = sphere(pos=vector(x3, y3, z3), radius=0.05, color=color.red)

# Calculate force
force_vector1 = vector(0, 0, 0)
force_vector2 = vector(0, 0, 0)
force_vector3 = vector(0, 0, 0)
for point in ring_points:
    r = point_mass.pos - point.pos
    r2 = point_mass2.pos - point.pos
    r3 = point_mass3.pos - point.pos
    if mag2(r) > 0:  
        force_magnitude1 = G * segment_mass / mag2(r)
        force_vector1 += norm(r) * force_magnitude1
    if mag2(r2) > 0:  # Check for the second point mass
        force_magnitude2 = G * segment_mass / mag2(r2)
        force_vector2 += norm(r2) * force_magnitude2
    if mag2(r3) > 0:  # Check for the third point mass
        force_magnitude3 = G * segment_mass / mag2(r3)
        force_vector3 += norm(r3) * force_magnitude3

# Display force
force_arrow = arrow(pos=point_mass.pos, axis=force_vector1.norm() * 0.2, color=color.yellow, shaftwidth=0.02)
force_arrow2 = arrow(pos=point_mass2.pos, axis=force_vector2.norm() * 0.2, color=color.yellow, shaftwidth=0.02)
force_arrow3 = arrow(pos=point_mass3.pos, axis=force_vector3.norm() * 0.2, color=color.yellow, shaftwidth=0.02)

# Print results
print("Force magnitude", mag(force_vector1))
print("Force direction", force_vector1.norm())
print("Force magnitude", mag(force_vector2))
print("Force direction", force_vector2.norm())
print("Force magnitude", mag(force_vector3))
print("Force direction", force_vector3.norm())
## To adapt this code for a spherical shell we would need to have a mass for each point on the sphere and since it is a three dimensional object have an angle for theta and phi. We would then calulate as seen in line 35 but with theta and phi and also with a value for z. 