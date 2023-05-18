import json
import numpy as np


def find_closest_unique_colors(hex_code):
    with open(r"C:\Py Projects\Fashion App\Vector Database\database\matrix\unique_color.json", "r") as f:
        colors = json.load(f)

    with open("C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_unique_color.json", "r") as f:
        vectorized_colors = json.load(f)
    # with open("C:\Py Projects\Fashion App\Clothing Segmentation\src\json\kclustering.json", "r") as f:
    #     color = json.load(f)
    # closest_colors = find_closest_palettes(color="{:02x}{:02x}{:02x}".format(color[0][0], color[0][1], color[0][2]), vectors=vectorized_colors, palettes=colors, k=8)
    
    closest_colors = find_closest_color(hex_code=hex_code, vector_db=vectorized_colors, colors=colors)

    with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\closest_colors.json", "w") as f:
        json.dump(closest_colors, f)


def distance(color1, color2):
    return np.sqrt(np.sum((color1 - color2)**2))

# Define a function to find the closest color to a given hex code
def find_closest_color(hex_code, vector_db, colors, k=10):
    # Convert the hex code to an RGB color
    hex_value = int(hex_code, 16)
    r = (hex_value >> 16) & 0xFF
    g = (hex_value >> 8) & 0xFF
    b = hex_value & 0xFF
    # r = int(hex_code[0:2], 16)
    # g = int(hex_code[2:4], 16)
    # b = int(hex_code[4:6], 16)
    color = np.array([r, g, b])
    
    # Calculate the distances between the given color and all colors in the vector database
    distances = [distance(color, c) for c in vector_db]
    

    # Find the index of the color in the vector database with the 5 smallest distances to the given color
    idxs = np.argsort(distances)[:k]
    
    closest_color_array = []
    for idx in idxs:
        # Append the closest color as a hex code
        closest_color_array.append(colors[idx])
    
    return closest_color_array
