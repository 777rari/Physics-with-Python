#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:30:03 2024

@author: Isaac
"""
# Assignment #: VPython Mini-Project
#
# Programmer: Isaac Lewis
#
# Due Date: April 21, 2024
# PHYS 345, Spring 2024
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: This code models a spring mass oscillating and takes into account damping. There is a 3D visual accompanied with a plot.
# Input: No inputs
from vpython import *
from math import *
from time import *
scene = canvas(width=700, height=700, align='left')

support = box(size=vector(1, 0.01, 1),texture=textures.wood_old, pos=vector(0, 2, 0))

spring = helix(radius=0.1, coils=40, texture=textures.metal, axis=vector(0, -1, 0)*2, pos=vector(0, 2, 0))
spring.constant = 10

mass_block = box(size=vector(0.5, 0.5, 0.5),texture=textures.stucco)
mass_block.mass = 1
mass_block.v = vector(0,0,0)

drag = 0.4
plot = graph(ymin=-3,ymax=3,xmin=0,xmax=60,width=700,height=700,scroll=True,align='right',canvas = scene)

y_plot = gcurve(graph=plot, color=color.red, label="Displacement Vs. Time")

t = 0
dt = 0.05


while t < 100:
    rate(50)
    weight = vector(0, -9.81, 0)* mass_block.mass
    spring_force = -mass_block.pos* spring.constant
    Force = spring_force + weight - mass_block.v * drag 
    a = Force / mass_block.mass
    mass_block.v += a * dt
    mass_block.pos += mass_block.v * dt
    spring.axis = mass_block.pos - spring.pos
    y_plot.plot(t, mass_block.pos.y)
    t += dt