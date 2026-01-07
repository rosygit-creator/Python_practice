import subprocess

def list_dir_recursive_error(path):

    command='echo "error"'
    subprocess.run(command)



# print all filenames only
#     for dirnames,filenames,dirpath in os.walk(path):
#         # print(filenames)
#         for f in filenames:
#             print(f)
#             # prints directory names and filenames
#

    return 0


ans=list_dir_recursive_error("/Users/rosyagarwal/gitWork/Python_practice/logs")