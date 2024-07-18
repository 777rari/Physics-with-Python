#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:59:46 2024

@author: Isaac
"""

from vpython import *

canvas(width=1200, height=800)

south_pole = box(size=vector(6, 1, 6), color=color.blue, pos=vector(0, 2, 0), opacity=0.2)
north_pole = box(size=vector(6, 1, 6), color=color.red, pos=vector(0, -2, 0), opacity=0.2)

for j in range(29):
    for i in range(29):
        line = cylinder(radius=0.002, color=color.yellow,
                        axis=vector(0, -1, 0), length=4, opacity=0.2,
                        pos=vector(-2.9 + 0.2 * i, 2, -2.9 + 0.2 * j))

electric_charge = sphere(radius=0.08, color=color.red,
                        pos=vector(-6, 0, -2), make_trail=True)

electric_charge.q = 0.1
electric_charge.mass = 0.06
electric_charge.velocity = vector(6, 0, 0)

magnetic_field = vector(0, 2.56, 0)

t = 0
dt = 0.002

while 1:
    rate(50)
    electric_charge.pos += electric_charge.velocity * dt
    if north_pole.size.x / 2 > electric_charge.pos.x > -north_pole.size.x / 2:
        if north_pole.size.z / 2 > electric_charge > -north_pole.size.z / 2:
            lorentz_force = electric_charge.q * cross(electric_charge.velocity, magnetic_field)
            acceleration = lorentz_force / electric_charge.mass
            electric_charge.velocity += acceleration * dt

    t += dt