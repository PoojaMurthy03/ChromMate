import numpy as np
import pandas as pd

# Define the options
options = ['12', '8', '15', '7']

# Generate random weights
weights = np.random.rand(len(options))
weights /= np.sum(weights)  # Normalize weights so they sum up to 1

# Function to generate weighted input features for the ML model
def generate_weighted_input(option, weights):
    weighted_input = np.zeros(len(weights))
    if option in options:
        idx = options.index(option)
        weighted_input[idx] = weights[idx]
    return weighted_input

# Example of generating weighted input for each option
weighted_inputs = {}
for option in options:
    weighted_inputs[option] = generate_weighted_input(option, weights)

# Printing the weighted inputs for each option
for option, weighted_input in weighted_inputs.items():
    print(f"Weighted Input for '{option}':", weighted_input)
