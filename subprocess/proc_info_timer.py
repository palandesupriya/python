import subprocess
import time
def main():
    iCnt = 0
    iEndCnt = 10
    while True:
        pinfo = subprocess.check_call("ps", shell = True)
        print pinfo
        iCnt += 3
        if iCnt > iEndCnt:
            break
        time.sleep(2000)
    
if __name__ == '__main__':
    main()
