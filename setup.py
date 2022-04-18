# Getting started: https://code.visualstudio.com/docs/python/python-tutorial

# I. Shortcut
## Run: Shift + Enter
## Insert line below: Alt + Enter

# II. Create a project-specific virtual environment for the workspace containing a copy of a global interpreter (to avoid package incompatability issues)
## https://code.visualstudio.com/docs/python/environments

## 1) Conda env
## Update conda in the default env: $ conda upgrade --all
## Create a new env with conda: $ conda create -n [my-env-name] python=[python-version]
## Activate the env created: $ conda activate [my-env-name]
##                           $ source activate [my-env-name] (if source specified, e.g., /Users/lihuaxiao/opt/anaconda3/bin/activate)
## Remove an env: $ conda env remove --name [my-env-name]
## Deactivate env: conda deactivate

#### pip freeze > requirements.txt (pip3 on macOS): Create a requirements.txt file, describing the packages installed in the virtual environment.
#### pip install -r requirements.txt: Restore the packages on other computers.

## 2) Local env 
## For Windows | macOS: py -3 -m venv .venv | python3 -m venv .venv (choose "yes" for the pop-up)

# III. Install packages (in Python "shell" not interpreter)
## Install pip in the virtual env: $ conda install pip
## Install Tensorflow CPI version: $ pip3 install --updrade tensorflow
## Install Keras: $ pip install Keras
## Install scikit-learn: $ pip install scikit-learn

# Conclusion:
## Command Palette: Select Interpreter: Pick "conda/envs/lihua"

# Test program:
#%%

msg = "Hello World"
print(msg)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot