import random as rd
import os.path
import tkinter
from tkinter import *
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    f = open(file_name,"r")
    lst =[]
    j=0
    for x in f:
        lst.append(x)
    for i in lst:
        lst[j]=i.rstrip('\n')
        j+=1
    for i in range(len(lst)):
        lst[i]= tuple(lst[i].split())
    return lst
    

  
def print_cities(road_map):
    """
        Prints a list of cities, along with their locations.
        Print only one or two digits after the decimal point.
        """
    lst1 = []
    l = road_map
    for i in range(len(l)):
        lst1.append(l[i][1:4])

    for i in range(len(lst1)):
        lst1[i]=tuple([lst1[i][0],round(float(lst1[i][1]),2),round(float(lst1[i][2]),2)])

    print(lst1)

import math

def compute_total_distance(road_map):
    """
        Returns, as a floating point number, the sum of the distances of all
        the connections in the `road_map`. Remember that it's a cycle, so that
        (for example) in the initial `road_map`, Wyoming connects to Alabama...
        """
    d = 0
    for i in range(len(road_map)-1):
        d += math.sqrt((float(road_map[i][2]) - float(road_map[i+1][2]))**2 + (float(road_map[i][3]) - float(road_map[i+1][3]))**2)
    d+= math.sqrt((float(road_map[0][2]) - float(road_map[len(road_map)-1][2]))**2 + (float(road_map[0][3]) - float(road_map[len(road_map)-1][3]))**2)
    return d




def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple
        
    (new_road_map, new_total_distance)
        
    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    city1 = road_map[index1]
    city2 = road_map[index2]
    road_map[index1] = city2
    road_map[index2] = city1
    
    new_road_map = road_map
    
    
    
    return (new_road_map, compute_total_distance(new_road_map))

def shift_cities(road_map):
    """
        For every index i in the `road_map`, the city at the position i moves
        to the position i+1. The city at the last position moves to the position
        0. Return the new road map.
        """
    lst = []
    lst.append(road_map[len(road_map)-1])
    for i in range(0,len(road_map)-1):
        lst.append(road_map[i])
    
    
    return lst


def find_best_cycle(road_map):
    best_one = []
    new_road_map = []
    for row in road_map:
        new_road_map.append(row)
        best_one.append(row)
    cycle = 0
    lst = []
    for i in range(10000):
        coin_toss = rd.randint(0,1)
        if coin_toss == 0:      
            index1 = rd.randint(0, len(road_map) - 1)
            index2 = rd.randint(0, len(road_map) - 1)
            new_road_map = (swap_cities(new_road_map, index1, index2)[0])
            cycle = compute_total_distance(new_road_map)
            
            if (compute_total_distance(best_one)) > cycle:
                lst.append((cycle,(compute_total_distance(best_one))))
                best_one = []
                for row in new_road_map:
                    best_one.append(row)
            else:
                new_road_map = []
                for row in best_one:
                    new_road_map.append(row)
                
        elif coin_toss == 1:
            new_road_map = (shift_cities(new_road_map))
            cycle = compute_total_distance(new_road_map)

            if (compute_total_distance(best_one)) > cycle:
                lst.append((cycle,(compute_total_distance(best_one))))
                best_one = []
                for row in new_road_map:
                    best_one.append(row)
            else:
                new_road_map = []
                for row in best_one:
                    new_road_map.append(row)
    return best_one

def print_map(road_map):
    """
        Prints, in an easily understandable format, the cities and
        their connections, along with the cost for each connection
        and the total cost.
        """
    dic = {}
    for i in range(len(road_map)-2):
        dic[road_map[i][1] +' '+ 'to' + ' ' + road_map[i+1][1]] = ('Cost = %f' %compute_total_distance(road_map[i:i+2]),
           'Total Cost = %f' %compute_total_distance(road_map[0:i+2]))
    
    return dic


    
def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    finished = False
    while not finished:
        file = input('please enter file: ')
        if os.path.isfile(file):
            cities = read_cities(file)
            bc = find_best_cycle(cities)
            print('\ncity-data:\n')
            print(cities, end = '\n\n\n')
            print('best cycle:\n')
            print(bc)
            visualise(bc)
            finished = True
        else:
            print('file path not found')
            finished = True




def visualise(road_map):
    x = []
    y = []
    cities = []
    
    for i in range(len(road_map)):
        x1 = float(road_map[i][3])
        y1 = float(road_map[i][2])
        city = str(road_map[i][1])
        x.append(x1)
        y.append(y1)
        cities.append(city)
    tk = tkinter.Tk()
    tk.wm_title("Road Map")
    
    fig = Figure(figsize=(15, 14), dpi=200)
    a = fig.add_subplot(111)
    a.plot(x, y)
    
    for i in range(-1, len(road_map)-1):
        a.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]))
        a.scatter(x[i], y[i])
        a.annotate(cities[i], (x[i], y[i]), size = 7)
    canvas = FigureCanvasTkAgg(fig, master=tk)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    tkinter.mainloop()



if __name__ == "__main__": #keep this in
    main()
