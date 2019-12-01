print ("Accept dir name and display all the file of specific extention......")
import os
from sys import *

def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 3):
        print("Error : Invalid number of argumnets")
    try:
        Check_DirNExtention(argv[1],argv[2])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
