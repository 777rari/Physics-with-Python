#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:58:06 2024

@author: Isaac
"""
# Assignment #: Python Assignment P7
#
# Programmer: Isaac Lewis
#
# Due Date: April 4, 2024
# PHYS 345, Spring 2024
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: This code finds the gravitiational force a uniform density model of the Earth with similar mass and radius units has on a one kilogram test mass at a distance of twice the radius from the earth.
# Input: No inputs
from vpython import *
import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11  # Gravitational constant

def gravitational_force_on_mass(Mass_Earth, Point_Mass, R, x, y, z):
    density = Mass_Earth / ((4/3)*np.pi*(R**3))
    segment_volume = (2*R/L)**3
    segment_mass = density*segment_volume
    force_vector = vector(0, 0, 0)
    
    # Generate Lattice
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                # Eliminate points greater than L from the origin
                pos = vector((i/L)*2*R,(j/L)*2*R,(k/L)*2*R)
                distance = vector(x,y,z) - pos
                if mag(distance) > 0:
                    Forces = distance*(-G * segment_mass * Point_Mass / mag(distance)**3)
                    force_vector += Forces
    
    return force_vector

def force_position_plot(Mass_Earth, Point_Mass, R, beginning, end, y, z, label):
    positions = np.linspace(beginning, end, 100)
    Force = [mag(gravitational_force_on_mass(Mass_Earth, Point_Mass, R, x, y, z)) for x in positions]
    
    plt.plot(positions, Force, label=label)

# Parameters
Mass_Earth = 5.97219e24 # Mass of Earth in kilograms
L = 20 # Number of segments along the axis
R = 6378100 # Radius of the Earth in meters
Point_Mass = 1 # Mass of the point mass in kg
x = R # Position of the point mass
y = 0
z = 0

#Radius_Small_Spheres = 100

results = gravitational_force_on_mass(Mass_Earth, Point_Mass, R, x, y, z)
print(results)

# First line: Through the center of the ring
force_position_plot(Mass_Earth, Point_Mass, R, (-R*2)+0.5, (R*2)+0.5, 0, 0, 'Line at Center Plane')

# Second line: Parallel and halfway to the edge
#force_position_plot(Mass_Ring,Point_Mass, R, -R*2, R*2, radius / 2, 0, 'Parallel Line')

plt.xlabel('Position (m)')
plt.ylabel('Gravitational Force (N)')
plt.title('Gravitational Force vs. Position')
plt.legend()
plt.show()
print("The criteria used to determine if the graph is correct is if the force increases as we approach the shell of the ring as the shell is where the gravitational force is the strongest")