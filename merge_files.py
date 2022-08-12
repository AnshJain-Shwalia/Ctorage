import os

MAX_SIZE=50*1000*1000       #50mb
NUM_FILES=10

def merge_files(map,path2):
    '''path2 is the location of raw files.'''
    if not(os.path.isdir(path2)):
        raise ValueError('location for processed files must be a directory.')
    num=0
    index=0
    data=b''
    for file in map[1]:
        file_stats = os.stat(file)
        size = file_stats.st_size
        map[2].append([file,index,index+size])
        index+=size
        if len(data)+size<=MAX_SIZE:
            with open(file,'rb') as tp:
                data+=tp.read()
        else:
            temp=len(data)
            with open(file,'rb') as tp:
                data+=tp.read(MAX_SIZE-temp)
                data_file_name=file_name(num,path2)
                with open(data_file_name,'wb') as cf:
                    cf.write(data)
                    data=b''
                    num+=1
                already_read=MAX_SIZE-temp
                while size-already_read>MAX_SIZE:
                    data=tp.read(MAX_SIZE)
                    data_file_name = file_name(num, path2)
                    with open(data_file_name, 'wb') as cf:
                        cf.write(data)
                        already_read+=MAX_SIZE
                        data = b''
                        num += 1
                data=tp.read()
    data_file_name = file_name(num, path2)
    with open(data_file_name, 'wb') as cf:
        cf.write(data)
        data = b''
        num += 1





def file_name(num,path2):
    q,r=divmod(num,NUM_FILES)
    dir_path=os.path.join(path2,str(q))
    if os.path.isdir(dir_path):
        qwerty=3+4
    else:
        os.makedirs(dir_path)
    result=os.path.join(dir_path,str(num))
    result+='.baz'
    return result
