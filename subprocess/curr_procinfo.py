'''
Write a python which runs periodically and displays status of current running process
'''
import subprocess
def main():
    pinfo = subprocess.check_call("ps -A", shell = True)
    print pinfo
    
if __name__ == '__main__':
    main()
	
	
'''
OUTPUT:
PID    TTY      TIME     CMD
     1 ?        00:00:00 start-http
     9 ?        00:03:06 httpd
 42133 ?        66-03:58:48 xmrig
146980 ?        00:00:00 httpd
148962 ?        00:00:00 httpd
150719 ?        00:00:00 httpd <defunct>
156485 ?        00:00:00 httpd
159150 ?        00:00:00 httpd
163498 ?        00:00:00 sh
163499 ?        00:00:00 timeout
163500 ?        00:00:01 javac
163547 ?        00:00:00 sh
163548 ?        00:00:00 timeout
163549 ?        00:00:00 python
163550 ?        00:00:00 ps
0
'''
