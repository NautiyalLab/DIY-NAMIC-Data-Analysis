## From Stephanie's Code --> Need this portion to use matplotlib and tkinter?
import matplotlib
import numpy as np

matplotlib.use("TkAgg")


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

