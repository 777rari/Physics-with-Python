#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:18:03 2024

@author: Isaac
"""

# Assignment #: Python Assignment P7
#
# Programmer: Isaac Lewis
#
# Due Date: March 24, 2024
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
    segment_mass = density*((4/3)*np.pi*(R**3))
    force_vector = vector(0, 0, 0)
    
    
    for i in range(-2*R,2*R+1):
        for j in range(-2*R,2*R+1):
            for k in range(-2*R,2*R+1):
                # Eliminate points greater than L from the origin
                distance = vector(x,y,z)
                if mag(distance)<=2*R:
                    pos=vector(x,y,z)
                    r = vector(x,y,z) - pos
                    force_magnitude = G * segment_mass * Point_Mass / mag(r)
                    force_vector += force_magnitude
    
    return force_vector

def force_position_plot(Mass_Earth, Point_Mass, R, beginning, end, y, z, label):
    positions = np.linspace(beginning, end, 1000)
    Force = [mag(gravitational_force_on_mass(Mass_Earth, Point_Mass, R, x, y, z)) for x in positions]
    
    plt.plot(positions, Force, label=label)

# Parameters
Mass_Earth = 5.97219e24 # Mass of Earth in kilograms
R = 6378100 # Radius of the Earth in meters
Radius_Small_Spheres = 100


Point_Mass = 1 # kg

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