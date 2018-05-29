import numpy as np
import random as rand
import collections as coll
from math import *
from numpy  import array
from scipy.spatial import distance
import networkx as nx
import matplotlib.pyplot as plt
from Queue import Queue
from Queue import PriorityQueue

# function to form the world and select cities out of it
def construct_world():
    # world height width
    width,height = 100,100
    c_width,c_height = 26,26
    # world matrix
    world = [[0for x in range(width)] for y in range (height)]
    city = [[0for x in range(c_width)] for y in range (c_height)]
    # world cities
    cities = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # define dictionary
    cordinates = coll.defaultdict(list)
    # looping and adding random values
    for x in range(0, 26):
        x_coordinate = rand.randint(0,100)
        y_coordinate = rand.randint(0,100)
        cordinates["vertex_x"].append(x_coordinate)
        cordinates["vertex_y"].append(y_coordinate)
        cordinates["vertex"].append(cities[x])
    # return the cordinate dictionary
    return cordinates
