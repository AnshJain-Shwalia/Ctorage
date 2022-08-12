import map_dir
import map_files
import merge_files
import to_github
import cr_map_3

#let folder_name=path.split('/')[-1]
#let folder_path=paths rooted at folder_name
#let full_path=full paths(rooted at root) 

#map=[[list containing paths of all directories in folder_name rooted at folder_path],[full_paths of files in folder_name],[list of form:[[full_path of file],[start_index],[end_index]]],[[list of form:[[full_path of file],[start_index],[end_index]]]],[folder_name(does not have info regarding upper directories)],[list containing all repo_links]]

def upload(path,raw_path,token='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'):
    map=[[],[],[],[],path.split('/')[-1],[]]
    map_dir.map_dir(map,path)
    map_files.map_files(map,path)
    print('Mapping files and directory done.')
    print('Merging files.')
    merge_files.merge_files(map,raw_path)
    print('Merging done.')
    print('uploading files')
    to_github.to_github(map,raw_path,token)
    print('uploading done.')
    map[1]=[]
    cr_map_3.cr_map_3(map,path)
    map[2]=[]
    return map

