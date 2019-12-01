print("Copy all files from first directory into second directory. Second directory should be created at run time and change the extention")
import os
from sys import *
import shutil


def Creat_Cpy_DIR(dir1, dir2,extension):
    access_rights = 0o777
    flag = os.path.isabs(dir1)
    # print(flag)
    if not flag:
        path = os.path.abspath(dir1)

    exists = os.path.isdir(path)

    path2 = os.path.abspath(dir2)
    flag2 = os.path.isdir(path2)
    #print(flag2)
    if not flag2:
        os.mkdir(path2, access_rights)
        #print("SSSSSSSSS")

        if exists:
            for data in os.listdir(path):
                #print("Current folder is:" + data)
                # dobj.write(folder)
                # os.path.dirname(path2)

                d1 = os.path.join(path, data)
                d2 = os.path.join(path2, data)

                if os.path.isdir(d1):
                    shutil.copytree(d1, d2)
                else:
                    if os.path.isfile(d1):
                        if d1.endswith(extension):
                            #print("DFGHJKJHGFDFGHJ")
                            shutil.copy2(d1, d2)



        else:
            print("Invalid Path")
    else:
        print("Already copied")


def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 4):
        print("Error : Invalid number of argumnets")
    try:
        Creat_Cpy_DIR(argv[1], argv[2],argv[3])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
