import os
from os.path import isfile, join

import shutil

import move_files
import time

yes_list = ['y', 'yes']
exit_list = ['exit', 'shutdown', 'sudo kill', 'kill', 'fiasco']
downloads_folder_names_list = ['downloads', '.']
downloads_folder_path = join(os.path.expanduser('~'), 'Downloads')


def are_you_sure_check():
    while True:
        if input().lower() in yes_list:
            return True
        else:
            return False



def delete_folders_in_a_folder(path=os.path.join(os.path.expanduser('~'), 'Downloads')):
    print('Are you sure you want to delete all folders from ', str(path))
    if are_you_sure_check():
        pass
    else:
        return
    folders = [f for f in os.listdir(path) if not isfile(join(path, f))]
    for f in folders:
        print(f, end='')
        print(' deleted')
        shutil.rmtree(os.path.join(path, f))
    print('All files deleted successfully')

def delete_everything_in_a_folder(path=os.path.join(os.path.expanduser('~'), 'Downloads')):
    files = [f for f in os.listdir(path) if isfile(join(path, f))]
    folders = [f for f in os.listdir(path) if not isfile(join(path, f))]
    print('It will delete everything from the folders')
    delete_files_in_a_folder(path)
    delete_folders_in_a_folder(path)



def delete_files_in_a_folder(path=join(os.path.expanduser('~'), 'Downloads')):
    print('Are you sure you want to delete all files from ', str(path))
    if are_you_sure_check():
        pass
    else:
        return

    print(path)
    files = [f for f in os.listdir(path) if isfile(join(path, f))]
    # print(files)
    for f in files:
        print(f, end='')
        print(' deleted')
        os.remove(os.path.join(path, f))
    print('All files deleted successfully')

print('Welcome!')
while True:
    print('Choose what would you like to do:')
    print('1 - put files into folders (recommended to be done before deleting)')
    print('2 - delete files')
    print('If you want to exit type in \'exit\' or \'suicide\'')
    cmd = input().lower()
    if cmd in exit_list:
        print('See you next time')
        time.sleep(1)
        break
    if cmd == str(1):
        move_files.starting(move_files.get_folder_names())
    if cmd == str(2):
        print('Choose directory (type in . or Downloads to stay in current directory)')
        directory_name = input().lower()
        if directory_name not in downloads_folder_names_list:
            current_path = os.path.join(downloads_folder_path,directory_name)
        else:
            current_path = downloads_folder_path
        print('1) delete all files in directory', current_path)
        print('2) delete all folders in directory', current_path)
        print('3) delete everything in directory', current_path)
        print('Enter command number')
        deletion_command = input()
        if deletion_command == str(1):
            delete_files_in_a_folder(current_path)
        if deletion_command == str(2):
            delete_folders_in_a_folder(current_path)
        if deletion_command == str(3):
            delete_everything_in_a_folder(current_path)

