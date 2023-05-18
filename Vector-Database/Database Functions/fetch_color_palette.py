import json
import numpy as np
from scipy.spatial.distance import cosine
import heapq

with open(r"C:\Py Projects\Fashion App\Vector Database\database\matrix\skin_palettes.json", "r") as readfile:
    palettes = json.load(readfile) 
with open("C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_skin_palettes.json", "r") as readfile:
    vectors = json.load(readfile) 
with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\closest_colors.json", "r") as readfile:
    colors = json.load(readfile)

def find_closest_palettes(color, vectors, palettes, k=5):

    hex_value = int(color, 16)
    red = (hex_value >> 16) & 0xFF
    green = (hex_value >> 8) & 0xFF
    blue = hex_value & 0xFF
    query_vector = np.array([red, green, blue])
    closest_palettes = []
    for i, vector in enumerate(vectors):
        distance = cosine(query_vector, np.mean(vector, axis=0))
        if len(closest_palettes) < k:
            heapq.heappush(closest_palettes, (-distance, i))
        else:
            heapq.heappushpop(closest_palettes, (-distance, i))
    closest_palettes = sorted(closest_palettes, reverse=True)
    return [palettes[i] for _, i in closest_palettes]

def find_palette(color, palettes):
    palette_list = []
    for row in palettes:
        if color in row:
            palette_list.append(row)
    return palette_list

def unwrap_palettes():

    with open(r"C:\Py Projects\Fashion App\Vector Database\database\matrix\skin_palettes.json", "r") as readfile:
        palettes = json.load(readfile) 
    with open("C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_skin_palettes.json", "r") as readfile:
        vectors = json.load(readfile) 
    with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\closest_colors.json", "r") as readfile:
        colors = json.load(readfile)

    final_palettes = []
    for color in colors:
        for palette in find_palette(color=color, palettes=palettes):
            final_palettes.append(palette)
    # print("FINAL PALETTE:", final_palettes)
    with open("C:\Py Projects\Fashion App\Vector Database\database\\final_palette.json", "w") as outfile:
        json.dump(final_palettes, outfile)

# closest_palettes = find_closest_palettes(color, vectors, palettes, k=10)


