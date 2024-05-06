'''How might you calculate the total size of all files ending with .txt that aren’t symlinks in
a directory? If your first answer was using os.path, also try it with pathlib, and vice
versa.'''

#using os
# import glob 
# import os
# found_list=glob.glob('*.txt')
# print(found_list)
# for file in found_list:
#     print("size of file ",file,'is: ',os.path.getsize(os.path.abspath(file)))

#using pathlib
from pathlib import Path


def calculate_total_size(directory):
    new_path=directory.joinpath('backup')
    for path in Path(directory).rglob('*.txt'):
        if not path.is_symlink():
            print(f'size of file {path.name} is: {path.stat().st_size}')
            path.rename(new_path.joinpath(path.name))
    


current_dir=Path.cwd()
(current_dir / 'backup').mkdir(exist_ok=True)
calculate_total_size(current_dir)

'''Write some code that builds off your solution to move the same .txt files in the lab
question to a new subdirectory called backup in the same directory.
'''
