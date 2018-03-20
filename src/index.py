#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 相当于es6中的...  ==>  可变参数写法 
# def foo(*args):
	# print(args)
	# print(type(args))
	
# foo(1, 2, 3)


# 传入dict，即对象  ==> 关键字参数写法
# def foo(name, age, **obj):
# 	print(name)
# 	print(age)
# 	print(obj)
# 	print(obj['city'])

# foo('fox', 23, city='天津', sex='男性')


# ==> 命名关键字参数写法 这快报错，回家研究吧
def foo(name, *, age, sex):
	print(name)
	print(age)
	print(sex)

foo('fox', age=23, sex='man')

