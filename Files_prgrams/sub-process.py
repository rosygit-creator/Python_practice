import subprocess

def list_dir_recursive_error(path):
    pattern='error'

    command=f"grep -r { pattern } { path }| wc -l"

    #If you pass a single string to subprocess.run() without shell=True,
    # Python attempts to run the entire string as a single executable name, which typically doesn't exist.

    # Method 1
    # subprocess.run("ls -l | grep error /Users/rosyagarwal/gitWork/Python_practice/logs/*", shell=True)

    # Method 2 , out put is 12
    result=subprocess.run(command, shell=True)





    # print("STDERR:", result.stderr)


    return result.returncode


ans=list_dir_recursive_error('/Users/rosyagarwal/gitWork/Python_practice/logs')
assert ans==0