import numpy as np
import matplotlib.pyplot as plt

try:
    # Python 2
    xrange
except NameError:
    # Python 3
    xrange = range

# counts the number of iterations until the function diverges or
# returns the iteration threshold that we check until
def countIterationsUntilDivergent(c, threshold):
    z = complex(0, 0)
    for iteration in xrange(threshold):
        z = (z*z) + c

        if abs(z) > 4:
            break
            pass
        pass
    return iteration

# takes the iteration limit before declaring function as convergent and
# takes the density of the atlas
# create atlas, plot mandelbrot set, display set
def mandelbrot(threshold, density):
    # location and size of the atlas rectangle
    # realAxis = np.linspace(-2.25, 0.75, density)
    # imaginaryAxis = np.linspace(-1.5, 1.5, density)
    realAxis = np.linspace(-0.22, -0.219, 1000)
    imaginaryAxis = np.linspace(-0.70, -0.699, 1000)
    realAxisLen = len(realAxis)
    imaginaryAxisLen = len(imaginaryAxis)

    # 2-D array to represent mandelbrot atlas
    atlas = np.empty((realAxisLen, imaginaryAxisLen))

    # color each point in the atlas depending on the iteration count
    for ix in xrange(realAxisLen):
        for iy in xrange(imaginaryAxisLen):
            cx = realAxis[ix]
            cy = imaginaryAxis[iy]
            c = complex(cx, cy)

            atlas[ix, iy] = countIterationsUntilDivergent(c, threshold)
            pass
        pass

    # plot and display mandelbrot set
    plt.imshow(atlas.T, interpolation="nearest")
    plt.show()

# time to party!!
mandelbrot(120, 1000)
