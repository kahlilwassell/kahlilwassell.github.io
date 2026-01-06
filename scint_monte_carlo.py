#import libraries
import numpy as np
import matplotlib.pyplot as plt
import ROOT
# get number of triggers from a user
muons = input("How many cosmic muons make it to just above the scintillator? ")
muon_num = int(muons)
# set rectangle edges
x = 0.25
yedge = 0.5
z = 0.5
# Create the two different scintillator surfaces by offsetting the bottom part
dist = 1.0
zbedge = ztedge - dist
# create an array to hold x and y values for muons that hit the scintillator
x_hit = []
y_hit = []
z_hit = []
# iterate over the values of the input muons
for i in range(muon_num):
    # generate random values
    x = np.random.uniform(-1.5,1.5)
    y = np.random.uniform(-1.5,1.5)
    z = np.random.uniform(-1.5,1.5)
    # if the points fall in the either rectangular prism add them to an array
    if -xedge < x < xedge and -yedge < y < yedge and 0.25 < z < ztedge or -xedge < x < xedge and -yedge < y < yedge and zbedge < z < -0.25:
        x_hit.append(x)
        y_hit.append(y)
        z_hit.append(z)
# create a histogram
h3 = ROOT.TH3D("h3", "Histogram of Hits on the Scintillator", 100, -1, 1, 100, -1, 1, 100, -1, 1)
# iterate through points in the array to fill the histogram
for k in range(len(x_hit)):
     h3.Fill(x_hit[k], y_hit[k], z_hit[k])
can = ROOT.TCanvas("c1","c1", 1000, 1000)
h3.Draw("box")
can.Print("beginscint.pdf")
