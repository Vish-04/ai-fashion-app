import json

# Convert color palettes to vectors
def convert_to_vectors(palettes):
    vectors = []
    for palette in palettes:
        vector = []
        for color in palette:
            hex_value = int(color, 16)
            red = (hex_value >> 16) & 0xFF
            green = (hex_value >> 8) & 0xFF
            blue = hex_value & 0xFF
            vector.append([red, green, blue])
        vectors.append(vector)
    return vectors

# Define function to find closest palettes to a given color
with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\palette_data.json", "r") as readfile:
    palettes = json.load(readfile) 
print(len(palettes))
vectors = convert_to_vectors(palettes)
with open("C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_palette_data.json", "w") as outfile:
    json.dump(vectors, outfile)