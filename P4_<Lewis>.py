#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:20:15 2024

@author: Isaac
"""
# Assignment #: Python Assignment P4
#
# Programmer: Isaac Lewis
#
# Due Date: February 29, 2024
# PHYS 345, Spring 2023
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: Build vpython model to animate orbit of two spheres around a sun
# Input: None
# Output: Output is a vpython animation of orbital motion with a trail to denote path taken around sun.


from vpython import *
from numpy import *
from math import *

# Gravitational Constant
G = 6.674e-11

# model parameters
initial_time = 0	# starting time	
time_step = 1000	# step size

#Initialize Lists

#Mass of Object 1 & 2 in kilograms
massobj_1 = 100
massobj_2 = 60
# Mass of Sun 
sun_mass = 200

# Radius of Orbits
r_01 = 100
r_02 = 100*(4**(1/3))



# Velocity Obj 1 and 2
velocity_c_obj_1 = sqrt((G*sun_mass)/r_01)
velocity_c_obj_2 = sqrt((G*sun_mass)/r_02)

#Start Vector
start_obj1 = vector(r_01,0,0)
start_obj2 = vector(r_02,0,0)

#Initial Positions For Objcects
sun = sphere(pos=vector(0,0,0),radius=4,color=color.orange)
obj_1 = sphere(pos=vector(r_01,0,0),radius=2,color=color.blue, make_trail=True)
obj_2 = sphere(pos=vector(r_02,0,0),radius=2,color=color.cyan, make_trail=True)




# Vector velocities
sun_velocity = vector(0,0,0)
obj_1_velocity = vector(0,velocity_c_obj_1,0)
obj_2_velocity = vector(0,velocity_c_obj_2,0)

# Euler method
time = initial_time
pos_obj_1 = start_obj1
pos_obj_2 = start_obj2

#print(velocity_c_obj_1)
#print(velocity_c_obj_2)
#duration = (100*2*pi)/(velocity_c_obj_1)
#print(duration)


while True:
    rate(4000)
    time += time_step
    radius_vec1 = pos_obj_1
    radius_vec2 = pos_obj_2
    F_1 = radius_vec1*(-G*sun_mass*massobj_1)/(mag(radius_vec1)**3)
    F_2 = radius_vec2*(-G*sun_mass*massobj_2)/(mag(radius_vec2)**3)
    a_1 = F_1/massobj_1
    a_2 = F_2/massobj_2
    obj_1_velocity += a_1*time_step
    obj_2_velocity += a_2*time_step
    pos_obj_1 += obj_1_velocity*time_step 
    pos_obj_2 += obj_2_velocity*time_step
    obj_1.pos = pos_obj_1
    obj_2.pos = pos_obj_2


    






