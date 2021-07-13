from pathlib import Path
import shutil
import os
from numpy import random


"""
TODO:
check if folder is empty
check if file is already in folder
build small interface
check on windows

"""


def copy_jpgs(inp_path):
    
    raw_path = _select_folder_by_number(inp_path)

    folder_name = input('What should the event be called?')
    
    image_folder = Path('/data/creative/raws/')
    
    exp_path = os.path.join(image_folder, folder_name, 'jpgs')
    os.makedirs(exp_path, exist_ok=True)

    filenames = sorted(Path(raw_path).rglob('*'))
    for filename in filenames:
        print(filename)
        if (str(filename).endswith('.jpg') or str(filename).endswith('.JPG') or str(filename).endswith(
                '.JPEG') or str(filename).endswith('.jpeg')):
            shutil.copy(filename, exp_path)


def copy_raws(drive_with_dcim):
    #  events = os.listdir('/data/creative/raws/')
    
    
    selection_folder = _select_folder_by_number('/data/creative/raws/', dcim=False)
    image_folder = Path('/data/creative/raws/')
    exp_path = os.path.join(image_folder, selection_folder, 'raws')
    os.makedirs(exp_path, exist_ok=True)
    
    exp_path_mov = os.path.join(image_folder, selection_folder, 'mov')
    os.makedirs(exp_path_mov, exist_ok=True)

    selection_pics = [os.path.splitext(os.path.split(filename)[1])[0] for filename in sorted(Path(selection_folder).rglob('*'))]

    raw_path = _select_folder_by_number(drive_with_dcim)
    
    counter = 0
    for file in sorted(Path(raw_path).rglob('*')):
        if random.random()<0.1:
            print(counter * 100//len(selection_pics),'%')

        _, tail = os.path.split(file)
        file_name = os.path.splitext(tail)
        if file_name[0] in selection_pics and file_name[1] == '.CR2':
            counter += 1
            shutil.copy(file, exp_path)
        elif file_name[1] == '.MP4' or file_name[1] == '.MOV':
            shutil.copy(file, exp_path)
            
    print('Successfully transfered selected raws and videos.')
    

def _select_folder_by_number(drive_with_dcim, dcim=True):
    """
    Takes String-Path to Folder as input, returns Path to per input chosen subfolder
    """
    
    if  dcim:
        dcim_folder = os.path.join(drive_with_dcim, "DCIM")
        
    else:
        dcim_folder = Path(drive_with_dcim)
        
    events = os.listdir(dcim_folder)
    

    for i, event in enumerate(events):
        print(i, event)

    print(events[0])
    
    cond = False
    while not cond:
        try:
            selected_folder = int(input('What folder do you want to get the raws from? Type the number: '))
            cond = True
        except:
            print('Try again.')
            
    raw_path = os.path.join(dcim_folder, events[selected_folder])
    return raw_path


def action():
    x = input("To copy all jpegs to the selection folder type '1',\nto get the raws and movies type '2'")
    if x == "1":
        y = input("What drive is the Card? . for Linux def")
        if y == '.':
            y = '/media/jake/EOS_DIGITAL'
        copy_jpgs(y)
    if x == "2":
        y = input("What drive is the Card? . for Linux def")
        if y == '.':
            y = '/media/jake/EOS_DIGITAL'
        copy_raws(y)
    else:
        print("Not a valid action, try again")
        action()
        
    action()


if __name__ == '__main__':
    action()
