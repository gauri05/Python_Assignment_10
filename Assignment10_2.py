print ("Rename all files with first file extension with the second file extenntion....")
import os
from sys import *


def Rename_file_extension(path,oldreplace, extension):
    print("The path is", path)
    flag = os.path.isabs(path)
    #print("Flag::", flag)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for folder, subfolders, filenames in os.walk(path):
            # print("Current folder is:" + folder)
            for fils in filenames:
                fobj = fils.endswith(oldreplace)
                # print("File inside " + folder + "is:" + fils)
                if fobj:
                    n_file=fils.replace(oldreplace,extension)
                    print("The files are----", n_file)
            print(' ')
    else:
        print("Invalid Path")


def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 4):
        print("Error : Invalid number of argumnets")
    try:
        Rename_file_extension(argv[1],argv[2],argv[3])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
