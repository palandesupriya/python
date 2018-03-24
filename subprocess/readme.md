EXECUTE ON : https://www.tutorialspoint.com/execute_python_online.php

>>import subprocess
>>print subprocess.call(["ls", "-l"])
	total 4
	-rw-r--r-- 1 apache apache 91 Mar 24 04:57 main.py
	0
	
>>import subprocess
>>z =  subprocess.check_output(["ls", "-l"])
>>print z
	total 4
	-rw-r--r-- 1 apache apache 135 Mar 24 05:00 main.py
	
	
>>import subprocess
>>z =  subprocess.check_output("echo $PATH")
>>print z
	Traceback (most recent call last):
  File "main.py", line 4, in <module>
    z =  subprocess.check_output("echo $PATH")
  File "/usr/lib64/python2.7/subprocess.py", line 568, in check_output
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
  File "/usr/lib64/python2.7/subprocess.py", line 711, in __init__
    errread, errwrite)
  File "/usr/lib64/python2.7/subprocess.py", line 1327, in _execute_child
    raise child_exception
  OSError: [Errno 2] No such file or directory
  
>>import subprocess
>>z =  subprocess.check_output("echo $PATH", shell = True)
>>print z
	/home/cg/root/GNUstep/Tools:/usr/GNUstep/Local/Tools:/
	
>>import subprocess
>>z =  subprocess.check_output("ifconfig", shell = True)
>>print z

>>import subprocess
>>z =  subprocess.call("cp 1", shell = True)		#does not raise exception
>>print z
	1
	cp: missing destination file operand after '1'
	Try 'cp --help' for more information.
	
>>import subprocess
>>z =  subprocess.check_call("cp 1", shell = True)	# raises exception
>>print z
	cp: missing destination file operand after '1'
	Try 'cp --help' for more information.
	Traceback (most recent call last):
	  File "main.py", line 4, in <module>
		z =  subprocess.check_call("cp 1", shell = True)
	  File "/usr/lib64/python2.7/subprocess.py", line 542, in check_call
		raise CalledProcessError(retcode, cmd)
	subprocess.CalledProcessError: Command 'cp 1' returned non-zero exit status 1
	
-->> return value by check_call is stored in file a.txt	
>>import subprocess
>>fd = open("a.txt", "w")
>>z =  subprocess.check_call("ls -l", shell = True, stdout = fd)
>>fd.close()
>>fd = open("a.txt", "r")
>>print fd.read()
>>fd.close()
	total 4
	-rw-r--r-- 1 apache apache   0 Mar 24 05:18 a.txt
	-rw-r--r-- 1 apache apache 228 Mar 24 05:18 main.py

	***************PIPE**************
>>import subprocess
>>proc = subprocess.Popen("cat -", shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
>>stdout_value = proc.communicate("hello Supp")[0] #[0] signifies write to pipe
>>print repr(stdout_value)
	'hello Supp'
	
	
import subprocess
def foo():
    print("I am executed before child process is executed!!")
    
def main():
    proc = subprocess.Popen("cat -", shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, preexec_fn = foo)
    stdout_value = proc.communicate("hello Supp")[0]
    print repr(stdout_value)
    
if __name__ == '__main__':
    main()
