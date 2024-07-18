#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:01:35 2024

@author: Isaac
"""

# Assignment #: Python Assignment P1
#
# Programmer: Isaac Lewis
#
# Due Date: February 25, 2024
# PHYS 345, Spring 2023
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: Use Euler's method to calculate free fall under constant acceleration then plot using graphical tools, such as vpython to animate the position of two spheres that follow the position and exact position.
# Input: None
# Output: Output is a vpython animation of a red spheres free fall position as a function of time and also an animation of a green sphere's free fall position with air resistance as a function of time. Output also includes the final values for time, simulation position values, and velocities.

from vpython import *

#Starting Conditions
start = vector(0,500,0)	#starting positon
startv = vector(0,0,0)	#starting velocity

# constant acceleration set here
g = 9.8

# Mass of Object
m = 2

# Drag constant
c = 0.5

# Force
F = vector(0,-g,0)*m
# Acceleration Due to Force and Mass
a = F/m	

# model parameters
initial_time = 0	# starting time	
time_step = 0.00025	# step size
#time_step_y_r = 0.00025 # Step size for ball with air resistance

#Initialize Lists
#timepoints = []
#ypoints = []
#y_rpoints = []

# Initialize Spheres
ball = sphere(pos=vector(0,start,0),size=vector(50,50,50), color=color.red)
#bally_r = sphere(pos=vector(55,start,0),size=vector(50,50,50), color=color.green)

#Calculate new postion and time using Euler's Method
time = initial_time
y = start
y_r = start
vy = startv
vy_r = startv


while True:
    F = vector(0,-g,0)*m
    #F_r = -m*g - c*vy_r
    a = F/m
    #a_r = F_r/m
    time = time + time_step
    vy = vy + a * time_step
    #vy_r = vy_r + a_r * time_step
    y = y + vy * time_step
    #y_r = y_r + vy_r * time_step
    timepoints.append(time)
    ypoints.append(y)
    #y_rpoints.append(y_r)
    rate(40000)
    #y = max(y, 0)
    #y_r = max(y_r, 0)
    ball.pos = vector(0,y,0)
    #bally_r.pos = vector(55,y_r,0)
    if y <= 0:
        break

final_time = time    
final_value_y = y
#final_value_y_r = y_r + vy_r * time_step
final_vy = vy
#final_vy_r = vy_r
print("Time when Red Sphere hits ground", time)
print("Position With no Resistance", y)
print("Position with Resistance", final_value_y_r)
print("Final Velo With No Resistance", vy)
print("Final Velo With Resistance", vy_r)

from pylab import plot,show,xlabel,ylabel
plot(timepoints,ypoints)
xlabel("time")
ylabel("position")
show()
plot(timepoints,y_rpoints)
xlabel("time")
ylabel("Y_r Position")
show()
