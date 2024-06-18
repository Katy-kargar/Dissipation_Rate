#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the first-order exponential decay model function
def first_order_exponential(x, A, B, C):
    return A * np.exp(-B * x) + C

# Setup the figure and gridspec
fig = plt.figure(figsize=(18, 15))
grid = plt.GridSpec(6, 4, hspace=0.5, wspace=0.5)

# Time and data for all scenarios
times = np.array([0.5, 6, 24])  # Time in hours

# Data organized by (wipes, flow, data array)
data_specs = [
    (10, 2.5, np.array([9.4, 0.85, 0.23])),
    (15, 2.5, np.array([11.4, 0.98, 0.25])),
    (20, 2.5, np.array([12.2, 1.03, 0.27])),
    (25, 2.5, np.array([9.4, 0.9, 0.24])),
    (30, 2.5, np.array([9.0, 0.95, 0.25])),
    (10, 10, np.array([23.8, 2.75, 0.83])),
    (15, 10, np.array([21, 2.5, 0.72])),
    (20, 10, np.array([16.4, 1.53, 0.43])),
    (25, 10, np.array([15.8, 1.55, 0.43])),
    (30, 10, np.array([10.2, 0.88, 0.23])),
    (10, 27, np.array([23.2, 3.75, 1.67])),
    (15, 27, np.array([22, 2.5, 0.74])),
    (20, 27, np.array([19.4, 2.22, 0.58])),
    (25, 27, np.array([13.4, 1.57, 0.46])),
    (30, 27, np.array([9, 0.87, 0.39]))
]

# Plotting each scenario in the specified grid
for wipes, flow, data_wipes in data_specs:
    row_idx = wipes // 5 - 1  # Calculate row index based on wipes
    col_idx = int(flow / 7.5)  # Column index calculated based on flow rate

    # Fit the model
    params, covariance = curve_fit(first_order_exponential, times, data_wipes, p0=[10, 0.1, 0], maxfev=5000)
    x_values = np.linspace(0.5, 24, 400)
    predicted_y = first_order_exponential(x_values, *params)
    
    # Plot for the scenario
    ax = fig.add_subplot(grid[row_idx, col_idx])
    ax.scatter(times, data_wipes, color='green')
    ax.plot(x_values, predicted_y, color='blue')
    ax.set_title(f'{wipes} Wipes, {flow} L/s', fontsize=10)
    ax.set_xlabel('Time (hr)', fontsize=10)
    ax.set_ylabel('Dissipation Rate', fontsize=10)
    ax.set_ylim(0, 30)  # Consistent y-axis range across all plots
  
    # Equation inside the graph in the upper right corner
    eq_text = f"y = {params[0]:.2f} * exp(-{params[1]:.2f} * x) + {params[2]:.2f}"
    ax.text(0.95, 0.95, eq_text, fontsize=10, verticalalignment='top', horizontalalignment='right', transform=ax.transAxes)

plt.show()


# In[ ]:




