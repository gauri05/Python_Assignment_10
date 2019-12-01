print("Accept dir name and display all the file of specific extention......")
import os
from sys import *


def Check_DirNExtention(path, extension):
    print("The path is", path)
    flag = os.path.isabs(path)
    print("Flag::", flag)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for folder, subfolders, filenames in os.walk(path):
            # print("Current folder is:" + folder)
            for sub in subfolders:
                print("Subfolder:::" + folder + "is:" + sub)
            for fils in filenames:
                fobj = fils.endswith(extension)
                # print("File inside " + folder + "is:" + fils)
                print("The files are----", fobj)
            print(' ')
    else:
        print("Invalid Path")


def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 3):
        print("Error : Invalid number of argumnets")
    try:
        Check_DirNExtention(argv[1], argv[2])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
