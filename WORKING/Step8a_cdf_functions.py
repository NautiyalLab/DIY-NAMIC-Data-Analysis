import numpy as np

## From Stephanie's Code --> Need this portion to use matplotlib and tkinter?
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot as plt



### Actual Plotting (CUMULATIVE DENSITY FUNCTION PLOTTING)
### ECDF
## Error Handling

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # x-data for the ECDF after dropping nan values: x
    x = np.sort(data)
    n = len(data)

    # # percentage values
    y = np.arange(1, n + 1) / n

    return x, y

## Simple CDF Function

def plot_cdf(control_x, control_y, exp_x, exp_y):
    fig, ax = plt.subplots()

    ax.plot(control_x, control_y, marker=".", linestyle='none', ms=5, color='red', label="Control Group")
    ax.plot(exp_x, exp_y, marker=".", linestyle='none', ms=5, color='blue', label="Experimental Group")

    ax.legend(loc='best', bbox_to_anchor=(1.01, 1.01))
