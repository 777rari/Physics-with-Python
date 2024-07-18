#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:43:47 2024

@author: Isaac
"""
# Assignment #: Python Assignment P6b
#
# Programmer: Isaac Lewis
#
# Due Date: March 18, 2024
# PHYS 345, Spring 2024
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: This code finds the gravitational force a ring exert on a point mass across the x axis of the ring and also a point mass parallel to the axis which is half the radius a away from the original axis and the edge of the sphere. Code then plots gravitational force vs. position.
# Input: Inputs for mass off ring, radius of ring
from vpython import *
import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11  # Gravitational constant

def gravitational_force_on_mass(Mass_Ring, Point_Mass, radius, x, y, z, segments=100):
    segment_mass = Mass_Ring / segments
    force_vector = vector(0, 0, 0)
    
    
    for i in range(segments):
        theta = 2 * np.pi * i / segments
        pos = vector(radius * np.cos(theta), radius * np.sin(theta), 0)
        
        r = vector(x, y, z) - pos

        if mag2(r) > 0:
            force_magnitude = G * segment_mass * Point_Mass / mag2(r)
            force_vector += norm(r) * force_magnitude
    
    return force_vector

def force_position_plot(Mass_Ring, Point_Mass, radius, beginning, end, y, z, label):
    positions = np.linspace(beginning, end, 100)
    Force = [mag(gravitational_force_on_mass(Mass_Ring, Point_Mass, radius, x, y, z)) for x in positions]
    
    plt.plot(positions, Force, label=label)

# Parameters
Mass_Ring = float(input("Mass of Ring (kilograms): ")) # kg
radius = float(input("Radius of Ring (meters): ")) # meters
Point_Mass = 1 # kg

# First line: Through the center of the ring
force_position_plot(Mass_Ring,Point_Mass, radius, -radius*2, radius*2, 0, 0, 'Line at Center Plane')

# Second line: Parallel and halfway to the edge
force_position_plot(Mass_Ring,Point_Mass, radius, -radius*2, radius*2, radius / 2, 0, 'Parallel Line')

plt.xlabel('Position (m)')
plt.ylabel('Gravitational Force (N)')
plt.title('Gravitational Force vs. Position')
plt.legend()
plt.show()
print("The criteria used to determine if the graph is correct is if the force increases as we approach the shell of the ring as the shell is where the gravitational force is the strongest")