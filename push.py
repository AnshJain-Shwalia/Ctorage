import os
def push(new):
    #git pushes at new
    stat = os.system(f'chmod +x push.sh')
    stat = os.system(f'./push.sh {new}')
