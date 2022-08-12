import os
import cr_dir
import recreate

def download(map, download_path, recreation_path,token,username):
    for elem in map[5]:
        modified=elem[:8]+str(username)+':'+str(token)+'@'+elem[8:]
        stat = os.system(f'cd {download_path}; git clone {modified}')
    cr_dir.cr_dir(map, recreation_path)
    recreate.recreate(map, download_path, recreation_path)
