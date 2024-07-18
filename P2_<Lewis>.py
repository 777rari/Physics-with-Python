#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 11:48:54 2024

@author: Isaac
"""

# Assignment #: Python Assignment P1
#
# Programmer: Isaac Lewis
#
# Due Date: February 18, 2024
# PHYS 345, Spring 2023
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: Use Euler's method to calculate free fall under constant acceleration then plot using graphical tools
# Input: None
# Output: Output is a plot of position as a function of time


#Starting Conditions
start = 100 	#starting positon
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

#Calculate new postion and time using Euler's Method
time = initial_time
y = start
vy = startv

while time < final_time:
    F = -m*g
    a = F/m
    time = time + time_step
    vy = vy + a * time_step
    y = y + vy * time_step
    y_e = start + startv * time + (0.5)*a*(time*time)
    Error = y_e - y
    timepoints.append(time)
    ypoints.append(y)
    y_epoints.append(y_e)
   # print (time, y, vy, y_e, Error)
    
from pylab import plot,show,xlabel,ylabel
plot(timepoints,ypoints)
xlabel("time")
ylabel("position")
show()
plot(timepoints,y_epoints)
xlabel("time")
ylabel("Exact Postion")
show()

    
