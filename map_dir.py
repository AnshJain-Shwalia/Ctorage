import os
def sub_map_dir(map,path):
    '''map must be in the form of map=[[]] i.e. there must be a list within a list'''
    all_dir=map[0]
    if not(os.path.isdir(path)):
        raise ValueError('Given path is not a directory.')
    else:
        sub=os.listdir(path)
        all_dir.append(path)
        for elem in sub:
            new=os.path.join(path,elem)
            if os.path.isdir(new):
                sub_map_dir(map,new)




def map_dir(map,path):
    '''map must be [[]]'''
    '''Changes map(list) so that it contains paths of all the sud-directories and file within directory at path variable and uses the directory at path as the root, at index 0.'''
    sub_map_dir(map,path)
    thing=path.split('/')
    replacement=thing[-1]
    for i in range(len(map[0])):
        map[0][i]=map[0][i].replace(path,replacement)



if __name__=="__main__":
    map=[[]]
    path='/home/ansh/Downloads'
    map_dir(map,path)
    print(map)