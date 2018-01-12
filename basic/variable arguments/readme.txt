def VarArgDemo(*args)
  print(type(args))
  for i in args:
    print i
    
    
call above fucntion with multiple parameters:
VarArgDemo(10,20)
VarArgDemo(10,20,"Hi",10.25)
VarArgDemo(10,20, 40 ,40)
VarArgDemo(10,20, "hello", "bye")
