# Getting started: https://code.visualstudio.com/docs/python/python-tutorial

# I. Shortcut
## Run: Shift + Enter
## Insert line below: Alt + Enter

# II. Create a project-specific virtual environment for the workspace containing a copy of a global interpreter (to avoid package incompatability issues)
## https://code.visualstudio.com/docs/python/environments
## For Windows | macOS: py -3 -m venv .venv | python3 -m venv .venv (choose "yes" for the pop-up)
## Conda environment: conda create -n env-01 python=3.10 scipy=0.15.0 astroid babel
#### pip freeze > requirements.txt (pip3 on macOS): Create a requirements.txt file, describing the packages installed in the virtual environment.
#### pip install -r requirements.txt: Restore the packages on other computers.

# III. Install packages (in Pytho "shell" not interpreter)
## For Windows | Mac: python -m pip install matplotlib | python3 -m pip install matplotlib

# IV. Type "deactivate" in the terminal window to deactivate the virtual environment, once finished.

# V. Use conda
## Command Palette: Select Interpreter


#%%

msg = "Hello World"
print(msg)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

# %%
