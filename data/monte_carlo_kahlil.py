import numpy as np
import matplotlib.pyplot as plt
from random import random
import ROOT

points = input('How many points would you like to test? ')
point_num = int(points)
circ_rad = 0.5
#intiialize the counters
pointcirc = 0
pointtot = 0
#create arrays to hold circle in and circle out points
incircx = []
incircy = []
outcircx = []
outcircy = []
#run through this code for each point
for i in range(point_num):
    # Generate a random x and y pair
    xrandom_num = 0.5 - random()
    yrandom_num = 0.5 - random()
    pointtot += 1
    # test to see if the random number is incide or outside of the circle and put it in the appropriate array
    if (xrandom_num ** 2 +  yrandom_num ** 2) <= circ_rad ** 2:
        pointcirc += 1
        incircx.append(xrandom_num)
        incircy.append(yrandom_num)

    else:
        outcircx.append(xrandom_num)
        outcircy.append(yrandom_num)
piq = 4 * pointcirc/pointtot
#print relavent information
print('estimate for pi = ' + str(piq))
print('points in = ' + str(pointcirc))
print('points total = ' + str(pointtot))
# create a histogram of the circle with where the hits are landing.
h2 = ROOT.TH2D("h2", "Histogram of Points in Circle", 100, -1, 1, 100, -1, 1)
for i in range(len(incircx)):
    h2.Fill(incircx[i], incircy[i])
mycan = ROOT.TCanvas("c1","c1",1000, 1000)
h2.Draw("colz")
mycan.Print("pointsincirc.pdf")
#create histogram where out of circle points are landing
h3 = ROOT.TH2D("h2", "Histogram of Points Out of Circle", 100, -1, 1, 100, -1, 1)
for i in range(len(outcircx)):
    h3.Fill(outcircx[i], outcircy[i])
mycan2 = ROOT.TCanvas("c2","c2", 1000, 1000)
h3.Draw("colz")
mycan2.Print("pointsoutcirc.pdf")

