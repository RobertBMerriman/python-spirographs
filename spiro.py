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
            # drawing is now done so hide the turtle cursor
            self.turt.hideturtle()


# a class for animating Spirographs
class SpiroAnimator:

    # constructors
    def __init__(self, N):
        # set the timer value in milliseconds
        self.delta_t = 10
        # get the window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()

        # creeate the Spiro objects
        self.spiros = []

        for i in range(N):
            # generate random parameters
            r_params = self.gen_random_params()
            # set the spiro parameters
            spiro = Spiro(*rparams)

            self.spiros.append(spiro)

        # call timer
        turtle.ontimer(self.update, self.delta_t)

    # generate random parameters
    def gen_random_params(self):
        width, height = self.width, self.height

        xc = random.randint(-width // 2, width // 2)
        yc = random.randint(-height // 2, height // 2)
        col = (random.random(), random.random(), random.random())
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)

        return (xc, yc, col, R, r, l)

    # restart spiro drawing
    def restart(self):
        for spiro in self.spiros:
            # clear
            spiro.clear()
            # generate random parameters
            r_params = self.gen_random_params()
            # set the spiro parameters
            spiro.set_params(*rparams)
            # restart drawing
            spiro.restart()

    def update(self):
        # update all spiros
        num_complete = 0
        for spiro in self.spiros:
            # update
            spiro.update()
            # count completed spiros
            if spiro.drawing_complete:
                num_complete += 1

        # restart if all spiros are complte
        if num_complete == len(self.spiros):
            self.restart()
        # call the timer
        turtle.ontimer(self.update, self.delta_t)

    # toggle turtle cursor on and off
    def toggle_turtles(self):
        for spiro in self.spiros:
            if spiro.turt.isvisible():
                spiro.turt.hideturtle()
            else:
                spiro.turt.showturtle()

    # save drawings as PNG files
    def save_drawing():
        # hide the turtle cursor
        turtle.hideturtle()
        # generate unique filenames
        date_str = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        file_name = "spiro-" + date_str
        print("Saving drawing to %s.eps/png" % file_name)
        # get the tkinter canvas
        canvas = turtle.getcanvas()
        # save the drawing as a postscript image
        canvas.postscript(file=file_name + ".eps")
        # use the Pillow module to convert the postscript image file to PNG
        img = Image.open(file_name + ".eps")
        img.save(file_name + ".png", 'png')
        # show the turtle cursor
        turtle.showturtle()


def main():
    parser = argparse.ArgumentParse(description=desc_str)
    # add expected arguments
    parse.add_argument("--sparams", nargs=3, dest="sparams", required=False, help="The three arguments in sparams: R, r, l")
    # parse args
    args = parser.parse_args()

    # set the width of the drawing window to 80 percent of the screen width
    turtle.setup(width=0.8)
    # set the curor shape to turtle
    turtle.shape("turtle")
    # set the title to Spirographs!
    turtle.title("Spirographs!")
    # add the key hanfler to save our drawings
    turtle.onkey(saveDrawing, 's')
    # start listening
    turtle.listen()

    # hide the main turtle curosr
    turtle.hideturtle()

    # check for any arguments sent to --sparams and draw the Spirograph
    if args.sparams:
        params = [float(x) for x in args.sparams]
        # draw the Spirograph with the given parameters
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        # create the animator object
        spiro_anim = SpiroAnimator(4)
        # add a key handler to toggle the turtle cursor
        turtle.onkey(spiro_anim.toggle_turtles, 't')
        # add a key handler to restart the animation
        turtle.onkey(spiroAnim.restart, 'space')

    # start the turtle main loop
    turtle.mainloop()
