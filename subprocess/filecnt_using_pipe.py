import subprocess
def main():
    fd = open("main.py", "r")
    pipeHandle = subprocess.Popen("wc", shell = True, stdout = subprocess.PIPE, stdin = fd)
    stdout_val = pipeHandle.communicate()
    print stdout_val
    fd.close()
if __name__ == '__main__':
    main()
    
    
    '''
    (' 10  31 269\n', None)
    '''
