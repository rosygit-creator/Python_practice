import os

# path
path = '/Users/rosyagarwal/gitWork/Python_practice/Files_prgrams/f6.txt'

# st_atim;  /* time of last access */
# st_mtim;  /* time of last modification */
# st_ctim;  /* time of last status change */



# Get Stat Information of a File
status = os.stat(path)

# Print the status
print(status)


# get file size in bytes
assert os.path.getsize(path)==58



# get file permission before and after and compare
permission=os.stat(path).st_mode
# convert to octal
# oct(permission)

opermisson=oct(permission & 0o777) # convert to octal and extract only the 3 permission bits
print(opermisson)

assert opermisson=='0o655'

#/Users/rosyagarwal/gitWork/Python_practice/Files_prgrams/os_stats_progs
print(os.getcwd())

# 0o represents octal integer
os.chmod(path, 0o655) # changed the permission for the file