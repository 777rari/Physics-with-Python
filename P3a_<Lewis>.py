#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:10:46 2024

@author: Isaac
"""

# Assignment #: Python Assignment P1
#
# Programmer: Isaac Lewis
#
# Due Date: February ?, 2024
# PHYS 345, Spring 2023
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: Use Euler's method to calculate free fall under constant acceleration then plot using graphical tools, such as vpython to animate the position of two spheres that follow the position and exact position.
# Input: None
# Output: Output is a vpython animation of spheres position as a function of time and also an animation of a sphere's exact position as a function of time. Output also includes the final values for time, simulation position value, and exact position value.

from vpython import *

#Starting Conditions
start = 100	#starting positon
startv = 0	#starting velocity

# constant acceleration set here
g = 9.8

# Mass of Object
m = 2

# Force
F = -m*g
# Acceleration Due to Force and Mass
a = F/m	

# model parameters
initial_time = 0	# starting time
final_time = 5		# ending time	
time_step = 0.0025	# step size

#Initialize Lists
timepoints = []
ypoints = []
y_epoints = []

# Initialize Spheres
ball = sphere(pos=vector(0,start,0),size=vector(5,5,5), color=color.red)
bally_e = sphere(pos=vector(8,start,0),size=vector(5,5,5), color=color.blue)

#Calculate new postion and time using Euler's Method
time = initial_time
y = start
vy = startv



while time < final_time:
    F = g*-m
    a = F/m
    time = time + time_step
    vy = vy + a * time_step
    y = y + vy * time_step
    y_e = start + startv * time + (0.5)*a*(time*time)
    #Error = y_e - y
    timepoints.append(time)
    ypoints.append(y)
    y_epoints.append(y_e)
    rate(400)
    ball.pos = vector(0,y,0)
    bally_e.pos = vector(8,y_e,0)
    #print (time, y, vy, y_e, Error)
    
final_value_y = y
final_value_y_e = start + startv * time + (0.5)*a*(time*time)
y_e = final_value_y_e
final_time = time
print("Final Value of Position:", y)
print("Final Value Exact Position:", y_e)
print("Final Time:", time)

#from pylab import plot,show,xlabel,ylabel
#plot(timepoints,ypoints)
#xlabel("time")
#ylabel("position")
#show()
#plot(timepoints,y_epoints)
#xlabel("time")
#ylabel("Exact Postion")
#show()

