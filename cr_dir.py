import os
def sub_cr_dir(map):
    for elem in map[0]:
        if os.path.isdir(elem):
            a=3+4
        else:
            os.makedirs(elem)


def cr_dir(map,path):
    '''Makes directories at paths in map[0].'''
    for i in range(len(map[0])):
        map[0][i]=os.path.join(path,map[0][i])
    sub_cr_dir(map)



