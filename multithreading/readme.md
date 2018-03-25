Multithreaded application is slower than unithreaded application in python which is why python is not used in RTOS
GIL - David Basely video. Global Interpreter Lock which serialises all threads.

threadhandle.start()
threadhandle.sleep(timemillisec)
threadhandle.join() - waits for child to complete its execution. It resukts in blocking.
