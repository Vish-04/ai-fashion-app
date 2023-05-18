import json

   # Convert color palettes to vectors
def convert_to_vectors(colors):
    vectors = []
    for color in colors:
        hex_value = int(color, 16)
        red = (hex_value >> 16) & 0xFF
        green = (hex_value >> 8) & 0xFF
        blue = hex_value & 0xFF
        vectors.append([red, green, blue])
    return vectors

def unique_color_seperation_and_vectorization():
    with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\skin_palettes.json", "r") as f:
        matrix = json.load(f)

    unique_matrix = []
    for row in matrix:
        for element in row:
            if element not in unique_matrix:
                unique_matrix.append(element)

    # print("UNIQUE MATRIX COLOR:", unique_matrix)

    with open(r"C:\Py Projects\Fashion App\Vector Database\database\matrix\unique_color.json", "w") as outfile:
        json.dump(unique_matrix, outfile)

    vector_db = convert_to_vectors(unique_matrix)

    with open("C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_unique_color.json", "w") as outfile:
        json.dump(vector_db, outfile)
