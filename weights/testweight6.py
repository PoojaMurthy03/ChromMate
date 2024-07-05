import numpy as np
import pandas as pd

# Define the options and their associated weights
options = ['12', '8', '15', '7']
weights = [0.8, 0.2, 0.05, 0.5]  # Adjust weights based on your confidence or relevance

# Function to generate weighted input features for the ML model
def generate_weighted_input(option, weights):
    weighted_input = np.zeros(len(weights))
    if option in options:
        idx = options.index(option)
        weighted_input[idx] = weights[idx]
    return weighted_input

# Example of generating weighted input for option '12'
weighted_input_12 = generate_weighted_input('12', weights)
print("Weighted Input for '12':", weighted_input_12)

# Example of generating weighted input for option '8'
weighted_input_8 = generate_weighted_input('8', weights)
print("Weighted Input for '8':", weighted_input_8)

# Example of generating weighted input for option '15'
weighted_input_15 = generate_weighted_input('15', weights)
print("Weighted Input for '15':", weighted_input_15)

# Example of generating weighted input for option '7'
weighted_input_7 = generate_weighted_input('7', weights)
print("Weighted Input for '7':", weighted_input_7)
