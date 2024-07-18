#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:14:56 2024

@author: Isaac
"""
# Assignment #: Python Assignment P1
#
# Programmer: Isaac Lewis
#
# Due Date: February 15, 2024
# PHYS 345, Spring 2023
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: Use Euler's method to calculate free fall under constant acceleration
# Description Cont: with gravity as our constant acceleration. The object has an initial height of 100 meters and a mass of 2 kg. The simulation will run for 5 seconds with a time step of 0.0025 seconds. We will utilize a while loop to run our simulation. 
# Input: None
# Output: Output is time, coresponding position, exact position, Error


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
    print (time, y, vy, y_e, Error)
    

