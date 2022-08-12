import os
def commit(new):
    stat = os.system(f'chmod +x commit.sh')
    stat = os.system(f'./commit.sh {new}')