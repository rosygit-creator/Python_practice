import os

# path
path = '/Users/rosyagarwal/gitWork/Python_practice/Files_prgrams/f1.txt'

# Get Stat Information of a File
status = os.stat(path)

# Print the status
print(status)

# get file size in bytes

print(os.path.getsize(path))

# get file size
print(os.stat(path).st_size)

#/Users/rosyagarwal/gitWork/Python_practice/Files_prgrams/os_stats_progs
print(os.getcwd())

# 0o represents octal integer
os.chmod(path, 0o655) # changed the permission for the file