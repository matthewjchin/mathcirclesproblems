n_gon = 6 # start with hexagon
top_faces = 1 # start with 1 "top tile"
side_faces = 2 # start with 2 "bottom tiles"

# Top tile count starts at 1, side tiles count starts at 2
# Total of first stage of tiles is 3. Use that total as the next
# top tile count and each side tiles count appends by 1. 
# Each subsequent count of tiles will be the number of top tiles
# (the total previous tiling of n-gon, increased by 2) plus the 
# number of side tilings plus 1 each iteration. 
# 
# In total, for a 2020-gon, there are 509545 total tilings with a 
# top tiling of 508536 and side tiling of 1009. 


print("All are total faces.")
for x in range(n_gon, 2021, 2):
    print("Top:", top_faces, "\t Side:", side_faces, "\t Total:", 
        top_faces + side_faces, "\t n-gon:", x)
    top_faces += side_faces # top faces value now the total faces for next top faces iteration
    side_faces += 1 # keep appending to side faces value by 1