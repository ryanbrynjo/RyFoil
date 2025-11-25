import matplotlib.pyplot as plt
import numpy as np
import os


print("Welcome to Ry-Foil, an Airfoil Solver and Analyzer")
print("---------------------------------------------------")
print("Select an airfoil (1-105)")
print("---------------------------------------------------")



def listairfoils(folder:str):
    files = sorted(os.listdir(folder))
    newfile = []
    for i, file in enumerate(files):
        newfile.append((i,file))
    return newfile


def menu(folder:str):
    tuples = listairfoils(folder)
    for i,e in tuples:
        print(F"{i} {e}")

def coordinates(folder:str):
    number = input()
    tuples = listairfoils(folder)
    _,a = tuples[int(number)]
    coords = np.loadtxt(F"assets\\coordinates\\{a}", skiprows = 1)
    x = coords[:,0]
    y = coords[:,1]
    print(x,y)

    return x,y,coords


menu("assets\\coordinates")
coordinates("assets\\coordinates")



