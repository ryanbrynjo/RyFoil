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

def plotter(folder:str):
    x, y, _ = coordinates(folder)

    # Example grid + simple uniform flow
    X, Y = np.meshgrid(
        np.linspace(-1, 2, 200),
        np.linspace(-1, 1, 200)
    )
    U = 1.0 * np.ones_like(X)   # uniform U-velocity
    V = 0.0 * np.ones_like(Y)   # uniform V-velocity

    fig, ax = plt.subplots(figsize=(8,4))

    # Streamlines
    ax.streamplot(X, Y, U, V, density=2.0)

    # Airfoil geometry
    ax.plot(x, y, 'k', linewidth=2)

    ax.set_aspect('equal')
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(min(y)-0.2, max(y)+0.2)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Airfoil with Uniform Flow Streamlines")

    plt.show()

menu("assets\\coordinates")
plotter("assets\\coordinates")



