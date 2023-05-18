import json
from vectorize_data import convert_to_vectors



# Define a function to find the palettes that match a given hex code
def find_skin_palettes(hex_code):

    # Load the matrix from the JSON file
    with open('C:\Py Projects\Fashion App\Vector Database\database\matrix\palette_data.json', 'r') as f:
        matrix = json.load(f)

    palettes = []
    for palette in matrix:
        if palette[0] == hex_code:
            palettes.append(palette)

    with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\skin_palettes.json", "w") as outfile:
        json.dump(palettes, outfile)

    vectors = convert_to_vectors(palettes)
    with open("C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_skin_palettes.json", "w") as outfile:
        json.dump(vectors, outfile)

    return palettes

# Test the function with a sample input
# hex_code = input("Enter a hex code: ")
# palettes = find_palettes(hex_code)
# print("Matching palettes:", palettes)