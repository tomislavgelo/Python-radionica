import os
import shutil

def copy_files(source,destination,file_extension):
    if os.path.exists(source):
        list_of_files = os.listdir(source)
    else:
        exit()
    if not os.path.exists(destination):
        os.mkdir(destination)
    for file in list_of_files:
        if file_extension in file:
            shutil.move(
                source + '\\' + file,
                destination
            )

copy_files(os.getcwd(),os.getcwd() + '_Copy','txt')