import os

MAX_SIZE = 50*1000*1000       # 80mb
NUM_FILES = 10


def recreate(map, raw_path,recreation_path):
    for file in map[3]:
        name = os.path.join(recreation_path,file[0])
        start = file[1]
        end = file[2]
        size = end-start
        q1, r1, folder_number1 = info(start)
        q2, r2, folder_number2 = info(end)
        if q2 > q1:
            new_foldername1=map[4]+'_'+str(folder_number1)
            with open(os.path.join(raw_path, new_foldername1, str(q1))+'.baz', 'rb') as tp:
                data = tp.read()[r1:]
            with open(name, 'ab') as f_ile:
                f_ile.write(data)
            while q2 > q1+1:
                new = q1+1
                folder_number = q_to_dir_num(new)
                new_foldername = map[4] + '_' + str(folder_number)
                read_location = os.path.join(raw_path, new_foldername, str(new))+ '.baz'
                with open(read_location, 'rb') as tp:
                    data = tp.read()
                with open(name, 'ab') as f_ile:
                    f_ile.write(data)
                q1 = new
            new_foldername2 = map[4] + '_' + str(folder_number2)
            read_location = os.path.join(raw_path, new_foldername2, str(q2)) +'.baz'
            with open(read_location, 'rb') as tp:
                data = tp.read()[:r2]
            with open(name, 'ab') as f_ile:
                f_ile.write(data)
        else:
            folder_number = q_to_dir_num(q1)
            new_foldername = map[4] + '_' + str(folder_number)
            read_location = os.path.join(raw_path, new_foldername, str(q1))+ '.baz'
            with open(read_location, 'rb') as tp:
                data = tp.read()[r1:r2]
            with open(name, 'ab') as f_ile:
                f_ile.write(data)


def q_to_dir_num(q):
    return q//NUM_FILES


def info(start):
    q, r = divmod(start, MAX_SIZE)
    folder_number = q//NUM_FILES
    return q, r, folder_number
