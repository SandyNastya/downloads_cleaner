#encoding: utf-8
import os
import shutil
from os.path import isfile, join

folders_name = ["installers", "images", "documents", "music", "archives", "video", "others"]

def get_folder_names():
    return folders_name

def create_folders(path, folders_name):
    for name in folders_name:
        os.chdir(path)
        while True:
            print("Do you need '%s' folder?(yes or no)" % name)
            answer = input().lower()
            if answer == "yes":
                if (os.path.isdir(os.path.expanduser('~/Downloads/%s' % name))):
                    return
                else:
                    os.mkdir(name)
            elif answer == "no":
                folders_name.remove(name)
                return
            else:
                continue
    return

def move_files(path):
    os.chdir(path)
    onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
    for f in onlyfiles:
        file_name = f.split('.')[-1]
        if "installers" in folders_name and file_name in 'exe':
            shutil.move(f, os.path.expanduser('~/Downloads/installers'))
        elif "images" in folders_name and file_name in 'gifjpgpngtifjpeg':
            shutil.move(f, os.path.expanduser('~/Downloads/images'))
        elif "documents" in folders_name and file_name in 'txtdocxodtrtfpdfchmdjvu':
            shutil.move(f, os.path.expanduser('~/Downloads/documents'))
        elif "music" in folders_name and file_name in 'midimp3wavwmaraaacac3amrcdaimelodyimyflacm4aoggqcpxmf':
            shutil.move(f, os.path.expanduser('~/Downloads/music'))
        elif "archives" in folders_name and file_name in 'zip7zacearjcabrartarhaiso':
            shutil.move(f, os.path.expanduser('~/Downloads/archives'))
        elif "video" in folders_name and file_name in 'avi3gpaafflvmp4mpegmovvobwmvmts':
            shutil.move(f, os.path.expanduser('~/Downloads/video'))
        elif "others" in folders_name:
            shutil.move(f, os.path.expanduser('~/Downloads/others'))
        else:
            continue
    return

def starting(folders_name):
    path = os.path.expanduser('~/Downloads')
    create_folders(path, folders_name)
    move_files(path)
    print('Folders created')
    return


