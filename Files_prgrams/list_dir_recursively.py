import os

def list_dir_recursive(path):


    # for dirnames, filenames, dirpath in os.walk(path):
    #     for f in filenames:
    #         # print(f)
    #         if 'eclipse' in f:
    #             print(f)

    #     file_names.extend(filenames) this will create one list

# print all filenames only
    for dirnames,filenames,dirpath in os.walk(path):
        # print(filenames)
        for f in filenames:
            print(f)
            # prints directory names and filenames

# print all dirnames only
#     for dirnames,filenames,dirpath in os.walk(path):
#         print(dirnames)
#         # result: /Users/rosyagarwal/gitWork/selenium-practice/.metadata/.mylyn path of directory
#
#     for dirnames, filenames, dirpath in os.walk(path):
#         # if dirpath: # non empty
#             print(dirpath)

    return 0


ans=list_dir_recursive("/Users/rosyagarwal/gitWork/selenium-practice/.metadata")