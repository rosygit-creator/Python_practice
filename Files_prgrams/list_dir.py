import os

def list_directory(path):
    names=[]

    # print(os.listdir(path))
    names=os.listdir((path))
    # print(names)
    for n in names:
        if os.path.isdir(n):
            print(n)
        if os.path.isfile(n):
            print(n)


    return 0


ans=list_directory("/Users/rosyagarwal/gitWork/Python_practice/Files_prgrams")