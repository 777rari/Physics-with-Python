# Program or Assignment #: Final Project
#
# Programmer: Isaac Lewis
#
# Due Date: 5/10/24
# PHYS 345, Spring 2023
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: In this code I am utilizing vpython to model the motion of a charged particle through a solenoid. We we will use the equation for the magnetic field of a solenoid to get the strength of the magnetic field and we will use the Lorentz force equation to calculate the motion of the charged particle.
# Input: None
# Output: Running this code produces a visual representation of a charged particle moving through a solenoid. Since the magnetic field in the solenoid is uniform in the direction of the solenoid, the charegd particle, which is moving in the x-direction will continue in a straight path.
from vpython import *
from math import pi

# Constants
mu_0 = 4 * pi * 1e-7  # Permeability of free space

# Canvas
scene = canvas(width=1200, height=800)

# Solenoid Parameters
solenoid_length = 10
solenoid_radius = 3
number_of_turns = 20
current = 5

# Calculate turns per unit length and the magnetic field inside the solenoid
turns_per_length = number_of_turns / solenoid_length
magnetic_field_strength = mu_0 * turns_per_length * current

# Define the solenoid as a cylinder for visual background
solenoid = cylinder(pos=vector(-solenoid_length/2, 0, 0), axis=vector(solenoid_length, 0, 0), radius=solenoid_radius, color=color.cyan, opacity=0.3)

# Calculate coil spacing
coil_spacing = solenoid_length / (number_of_turns - 1)

# Add a helical coil for the solenoid
coil = helix(pos=vector(-solenoid_length/2, 0, 0), axis=vector(solenoid_length, 0, 0), radius=solenoid_radius, color=color.yellow, thickness=0.05, coils=number_of_turns, pitch=coil_spacing)

# Define the charged particle starting outside the solenoid
electric_charge = sphere(radius=0.1, color=color.red, pos=vector(-solenoid_length/2 - 1, 0, 0), make_trail=True)
electric_charge.q = 0.1  # Charge
electric_charge.mass = 0.06
electric_charge.velocity = vector(5, 0, 0)  # Initial velocity directed towards the solenoid

# Time setup
t = 0
dt = 0.001

# Simulation Loop
while True:
    rate(100)
    electric_charge.pos += electric_charge.velocity * dt

    # Apply Lorentz force only inside the solenoid
    if -solenoid_length/2 <= electric_charge.pos.x <= solenoid_length/2:
        magnetic_field = vector(magnetic_field_strength, 0, 0)  # Uniform field inside the solenoid
    else:
        magnetic_field = vector(0, 0, 0)

    lorentz_force = electric_charge.q * cross(electric_charge.velocity, magnetic_field)
    acceleration = lorentz_force / electric_charge.mass
    electric_charge.velocity += acceleration * dt

t += dt
