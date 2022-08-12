import os
def cr_map_3(map,path):
    replacement = map[4]
    for i in range(len(map[2])):
        old=map[2][i][0]
        new=old.replace(path,replacement)
        map[3].append([new, map[2][i][1], map[2][i][2]])