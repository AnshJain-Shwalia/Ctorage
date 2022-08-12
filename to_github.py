import os
from github import Github
from push import push
from commit import commit

def to_github(map,raw_path,token):
    validate_token(token)
    g=Github(token)
    user=g.get_user()
    username=user.login
    origin_path_sub = f'https://{username}:{token}@github.com/{username}/'
    base=map[4]
    for elem in os.listdir(raw_path):
        new = os.path.join(raw_path, elem)
        stat = os.system(f'cd {new}')
        if stat != 0:
            raise Exception(f"Couldn't change directories to {new}.")
        # initialising repo in {new}
        stat = os.system(f'cd {new}; git init')
        print(f'Initialised repo in {new}')
        print(base)
        print(elem)
        repo_name = base + '_' + elem
        # Creating repo
        repo = g.get_user().create_repo(repo_name,private=True)
        print(f"Created github repo")
        # Adding repo_link to map
        repo_link = f'https://github.com/{username}/{repo_name}.git'
        map[5].append(repo_link)
        # adding remote origin
        origin_path = origin_path_sub + repo_name + '.git'
        stat2 = os.popen(f'cd {new};git remote add origin {origin_path}')
        print(f'origin added at {origin_path}')
        # adding file to staging area
        stat = os.system(f'cd {new}; git add -A')
        print('Files added to staging area')
        # setting up config info
        stat = os.system(f'cd {new}; git config user.name "ligma"')
        stat = os.system(f'cd {new}; git config user.email ligma@balls.bitch')
        print('User config added')
        # commiting files
        #stat0 = os.popen(f'cd {new}; git commit -a -m "here."')
        commit(new)
        print(f'Files in {new} commited')
        # pushing commits
        stat1 = os.popen(f'cd {new}; git branch -M main')
        push(new)
        print(f'Files in {new} pushed to origin')
        #print(stat2.read())
        print(f'done with {new}')



def validate_token(token):
    #validates token by gettting and printing username
    print('Validating token.')
    try:
        g=Github(token)
        user=g.get_user()
        username=user.login
        print(f'Username={username}')
        print(f'token validated.')
        return username
    except:
        raise ValueError('Could not validate token,Validation falied.')