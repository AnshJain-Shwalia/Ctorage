import os
import upload
import download
import json


def main():
    while True:
        a=input('What do you wanna do?(D(download)/U(upload)/Q(quit))')
        a=a.lower()
        if a=='u':
            path=input('Enter path.')
            validate_directory(path)
            raw_path=input('Enter raw_path.')
            validate_directory_empty(raw_path)
            token=input('Enter token.')
            #Token Validation
            upload.to_github.validate_token(token)
            #----------------
            map=upload.upload(path,raw_path,token)
            print('uploading done.')
            map_path=input('Enter directory path in which to place .map file.')
            while not os.path.isdir(map_path):
                print(f'{map_path} is not a valid path.')
                map_path=input('Enter another one...,Enter directory path in which to place .map file.')
            map_path=os.path.join(map_path,map[4])+'.map'
            with open(map_path,'w') as file:
                string=json.dumps(map)
                file.write(string)
            print(f'.map file created at {map_path}')
            print(f'Upload process is done and .map file is created at {map_path}')
            print(f'please take care of deleting files in {raw_path}')
        elif a=='d':
            path=input('Enter path to .map file.(ex->directory_path/file_name.map)')
            try:
                with open(path,'r') as file:
                    map=json.loads(file.read())
            except:
                raise Exception('Error loading .map file.')
            folder_path=input('Enter destination dir.')
            validate_directory_empty(folder_path)
            download_path,destination_path=download_and_destination_path(folder_path)
            token=input('Enter token.')
            #Token Validation
            username=upload.to_github.validate_token(token)
            download.download(map,download_path,destination_path,token,username)
            print(f'download process is done and files have been re-created at {destination_path}.')
            print(f'please take care of deleting files in {download_path}')
        elif a=='q':
            quit()
        else:
            raise ValueError('Wrong input')


def download_and_destination_path(folder_path):
    #returns tuple of download_path and destination_path and creates these folders in folder_path
    download_path=os.path.join(folder_path,'download_path')
    os.makedirs(download_path)
    destination_path=os.path.join(folder_path,'recreation')
    os.makedirs(destination_path)
    return download_path,destination_path

def validate_directory(path):
    if not os.path.isdir(path):
        raise Exception(f'{path} is not a directory or does not exists.')

def validate_directory_empty(path):
    #continues if directory at path exists and is empty
    if not os.path.isdir(path):
        raise Exception(f'{path} is not a directory or does not exists.')
    if len(os.listdir(path)) != 0:
        raise Exception(f'{path} is not empty.')

if __name__=="__main__":
    main()