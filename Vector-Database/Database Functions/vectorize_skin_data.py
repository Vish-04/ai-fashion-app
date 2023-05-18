import numpy as np
import json

# Input matrix
with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\skin_color.json", "r") as outfile:
    matrix = json.load(outfile)

# matrix = [["fef9f3"],["fef5eb"],["fdf1e3"],["fdeddc"],["fcead4"],["fce6cc"],["fce2c4"],["fbdebc"],["fbdab5"],["fad6ad"],["fad3a5"],["fad3a5"],["f9cb96"],["f9c78e"],["f9c78e"],["f8c386"],["f8c07e"],["f8bc77"],["f7b86f"],["f7b467"],["f6b05f"],["f6ac58"],["f6a950"],["f5a548"],["f5a140"],["f49d38"],["f49931"],["f49629"],["f39221"],["f38e19"],["f28a12"],["f0860c"],["e8820b"],["e17d0b"],["d9790b"],["d1750a"],["c9700a"],["c26c09"],["ba6809"],["b26309"],["aa5f08"],["a35b08"],["9b5607"],["935207"],["8b4e07"],["8b4e07"],["7c4506"],["744105"],["6c3c05"],["643805"],["5d3404"],["552f04"],["4d2b03"],["4d2b03"],["452703"],["3e2203"],["361e02"],["2e1a02"],["261501"],["1f1101"],["170d01"],["0f0800"]]

vector_db = []

for row in matrix:
    for hex_val in row:
        r = int(hex_val[0:2], 16)
        g = int(hex_val[2:4], 16)
        b = int(hex_val[4:6], 16)
        vector_db.append([r, g, b])


print(vector_db)

with open("C:\Py Projects\Fashion App\Vector Database\database\\vector\\vectorized_skin_color.json", "w") as outfile:
    json.dump(vector_db, outfile)
