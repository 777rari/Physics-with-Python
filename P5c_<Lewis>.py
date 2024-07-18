#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:24:43 2024

@author: Isaac
"""

# Assignment #: Python Assignment P5B
#
# Programmer: Isaac Lewis
#
# Due Date: March 11, 2024
# PHYS 345, Spring 2024
# Pledge: I have neither given nor received unauthorized aid
# on this program.
# Description: Use a while loop to calculate gravitational force of a rod on a sphere
# Input: Distance of shere from rod
# Gravitational Constant
#from numpy import *
from numpy import *
#define constants 
Length = 0.005     
segments = 1000       #number of segments
G = 6.674e-11
Mass = 10
Point_Mass = 1
segment_mass = Mass/segments

segment_length = Length / segments
center_offset = segment_length / 2 # center of a segment
#User Input for distance of point mass to rod
x = float(input("X position point mass (meters from end of rod): "))

#Ways of generating a list of coordinates

index_vector=[]
Forces = []
index = 0
while index < segments:
    index = index + 1
    segment_coord = (index -1)*segment_length + center_offset
    index_vector.append(segment_coord)
    r = (x - segment_coord)
    Force = (-G*segment_mass*Point_Mass)/(r**2)
    Forces.append(Force)
        

Total_Force = sum(Forces)
print("Total Force Value:", Total_Force, "Newtons in the negative x direction")
print("Magnitude of Force is:", abs(Total_Force), "Newtons")
print(r)
#print(segment_mass)
















#print(type(index_vector))
#print(index_vector)
#print("The first element is ",index_vector[0])
#print()
    
### Usine linspace
#np.linspace(start, stop, num, …)
#print("Using linspace")
#list=linspace(0,Length,segments,endpoint=False) + center_offset
#print(type(list))
#print(list)
#print("The first element is ",list[0])
#print()

## using arange
##np.arange(start, stop, step, …)
#print("Using arange")
#list_arange = arange(center_offset,Length,segment_length)
#print(type(list_arange))
#print(list_arange)
##print("The first element is ",list_arange[0])
#print()
#Print the list of coordinates one at a time using for
#for i in (list_arange):
    #print(i)
