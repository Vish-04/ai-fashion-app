import json
import numpy as np


# Define a function to calculate the Euclidean distance between two colors
def distance(color1, color2):
    return np.sqrt(np.sum((color1 - color2)**2))

# Define a function to find the closest color to a given hex code
def find_closest_color(hex_code):

    # Load the vector database from the JSON file
    with open('C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_skin_color.json', 'r') as f:
        vector_db = json.load(f)

    # Convert the vector database to a numpy array
    vector_db = np.array(vector_db)

    # Convert the hex code to an RGB color
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    color = np.array([r, g, b])
    
    # Calculate the distances between the given color and all colors in the vector database
    distances = [distance(color, c) for c in vector_db]
    
    # Find the index of the color in the vector database with the smallest distance to the given color
    idx = np.argmin(distances)
    
    # Return the closest color as a hex code
    closest_color = vector_db[idx]
    closest_hex = ''.join([hex(int(c))[2:].zfill(2) for c in closest_color])
    return closest_hex

# # Test the function with a sample input
# hex_code = input("Enter a hex code: ")
# closest_hex = find_closest_color(hex_code)
# print("Closest color:", closest_hex)
