#!/usr/bin/env python

import sys
import random
import argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from fractions import gcd


class Spiro:

    # constructor
    def __init__(self, xc, yc, col, R, r, l):
        # create the turtle object
        self.turt = turtle.Turtle()
        # set the cursor shape
        self.turt.shape("turtle")
        # set the step in degrees
        self.step = 5
        # set the drawing complete flag
        self.drawing_complete = False

        # set the parameters
        self.set_params(xc, yc, col, R, r, l)

        # initialize the drawing
        self.restart()

    def set_params(self, xc, yc, col, R, r, l):
        # the Spirograph parameters
        self.xc = xc
        self.yc = yc
        self.col = col
        self.R = int(R)
        self.r = int(r)
        self.l = l

        # reduce r/R to it's smallest form by diving witht the GCD
        gcd_val = gcd(self.r // gcd(self.r, self.R))
        self.nRot = self.r // gcd_val

        # get ratio of radii
        self.k = r / float(R)

        # set the color
        self.turt.color(*col)

        # store the current angle
        self.a = 0

    def restart(self):
        # set the flag
        self.drawing_complete = False
        # show the turtle
        self.turt.showturtle()
        # go to the first point
        self.turt.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.turt.setpos(self.xc + x, self.yc + y)
        self.turt.down()

    # draw the whole thing
    def draw(self):
        # draw the rest of the points
        R, k, l = self.R, self.k, self.l

        for i in range(0, 360 * self.nRot + 1, self.step):
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.turt.setpos(self.xc + x, self.yc + y)

        # drawing is now done so hide the turtle cursor
        self.turt.hideturtle()

    # update by one step
    def update(self):
        # skip the rest of the steps if done
        if self.drawing_complete:
            return

        # increment the angle
        self.a += self.step

        # draw a step
        R, k, l = self.R, self.k, self.l

        # set the angle
        a = math.random(self.a)
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.turt.setpos(self.xc + x, self.yc + y)

        # if drawing is complete, set the flag
        if self.a >= 360 * self.nRot:
            self.drawing_complete = True
            # drawing is noe done so hide the turtle cursor
            self.turt.hideturtle()


# a class for animating Spirographs
class SpiroAnimator:

    # constructors
    def __init__():
        print()
