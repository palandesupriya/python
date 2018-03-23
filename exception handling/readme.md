Exceptions:

1. Caught exception.
2. Uncaught exceptions.

-Compile time exceptions
-Run time exceptions
-User define exceptions

Syntax:
try:
	anticipate exceptions in code
except Exception as e:
	print e
except ArithmaticError as e:
	print e
finally 	//	Finally execute every time(exception occure or not) , either give "except" or "finally" block, u can't give only "try" block.

try
	--
except
	--
else:	//	Execute if no exception occure.
