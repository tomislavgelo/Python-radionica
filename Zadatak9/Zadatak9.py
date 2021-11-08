import os
import shutil
source = os.getcwd()
destination = source + '_Copy'
list_of_files = os.listdir()
def copy_files(source,destination,file_extension):
    list_of_files = os.listdir()
    t1 = source
    t2 = destination
    t3 = file_extension
    if not os.path.exists(t2):
        os.mkdir(t2)
    for file in list_of_files:
        if t3 in file:
            shutil.copy(
                file,
                destination
            )
copy_files(source,destination,'bmp')