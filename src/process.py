import os

print(os.getpid())
pid = os.fork()
if pid == 0:
	print('我是子进程：%s， 我的父进城是：%s' %(os.getpid(), os.getppid()))
else:
	print('我：%s刚刚创建了子进程: %s' %(os.getpid(), pid))