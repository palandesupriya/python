import subprocess
def main():
    fd = open("main.py", "r")
    pipeHandle = subprocess.Popen("cat -", shell = True, stdout = subprocess.PIPE, stdin = fd)
    stdin_val = pipeHandle.communicate()
    szStr = str(stdin_val)
    fd.close()
    iTemp = 0
    iWordCnt = 0
    iCharCnt = 0
    iLineCnt = 1
    while (iTemp < len(szStr)):
        ch = szStr[iTemp]
        if '\n' == ch:
            iWordCnt += 1
            iLineCnt += 1
            iCharCnt += 1
        elif ' ' == ch:
            iWordCnt += 1
            iCharCnt += 1
        else:
            iCharCnt += 1
        iTemp += 1
    print("Number of words:{}".format(iWordCnt))
    print("Number of lines:{}".format(iLineCnt))
    print("Number of characters:{}".format(iCharCnt))
if __name__ == '__main__':
    main()
