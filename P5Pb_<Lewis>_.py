#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 11:03:03 2023

@author: fjames
"""
# Assignment #: Python Assignment P5A
#
# Programmer: Isaac Lewis
#
# Due Date: March 2, 2024
# PHYS 345, Spring 2024
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: Use vectors and vpython to calculate Force of Gravity of three orange masses on one yellow mass.
# Input: None


from vpython import *
from numpy import *
from math import *

# Gravitational Constant
G = 6.674e-11


# Define the spheres.  Note that sphere.mass is a created attribute
sphere0 = sphere(radius=.15,color=color.yellow)
sphere0.pos=vector(0,5,0)
sphere0.mass = 1
sphere1 = sphere(radius=.2,color=color.orange)
sphere1.pos = vector(0,0,0)
sphere1.mass = 8
sphere2 = sphere(radius=.2,color=color.orange)
sphere2.pos = vector(-2,0,0)
sphere2.mass = 8
sphere3 = sphere(radius=.2,color=color.orange)
sphere3.pos = vector(-4,0,0)
sphere3.mass = 8

rate(10)
dist_1_0 = sphere0.pos - sphere1.pos
dist_2_0 = sphere0.pos - sphere2.pos
dist_3_0 = sphere0.pos - sphere3.pos
print("Distance between sphere 1 and sphere 0:", dist_1_0)
print("Distance between sphere 2 and sphere 0:", dist_2_0)
print("Distance between sphere 3 and sphere 0:", dist_3_0)

F_1on0 = dist_1_0*(-G*sphere1.mass*sphere0.mass)/(mag(dist_1_0)**3)
F_2on0 = dist_2_0*(-G*sphere2.mass*sphere0.mass)/(mag(dist_2_0)**3)
F_3on0 = dist_3_0*(-G*sphere3.mass*sphere0.mass)/(mag(dist_3_0)**3)
Total_Force = F_1on0 + F_2on0 + F_3on0
Direction = degrees(atan2(Total_Force.y, Total_Force.x))
Force_Arrow = arrow(pos=sphere0.pos, axis=Total_Force.norm()*3, color=color.red, shaftwidth=0.1)
print(F_1on0)
print(F_2on0)
print(F_3on0)
print("Total Force", Total_Force)
print("Magnitude of Total Force:", mag(Total_Force))
print("Direction", Direction)



