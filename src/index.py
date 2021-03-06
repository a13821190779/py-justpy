#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# pip freeze 显示所有依赖包
# pip install -r 包含所有依赖的文件

# import stringio
# import process
# import reg
# import buildIn

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
# def person(name, age, *, city, job):
#     print(name, age, city, job)

# person('fox', 23, city='天津', job='coder')

# def readFile(path):
#     try:
#         file = open(path, 'r')
#         print(file.read())
#     except BaseException as e:
#         print('错误信息:', e)
#     finally:
#         if (file):
#             file.close()

# def writeFile(path):
#     try:
#         file = open(path, 'a')
#         file.write('这次会append模式，而不是默认的替换模式了')
#     except BaseException as e:
#         print('错误信息:', e)
#     finally:
#         if (file and not file.closed):
#             file.close()

# writeFile('/Users/fox/testProject/b.txt')
# readFile('/Users/fox/testProject/b.txt')

# 爬头条
# import fetchDynamic
# import web

# import fr

# 图片上写文字
# import writeText

# 生成 200 个激活码
# import generateCode

# 获取文件内容长度
# import getCountOfTxt

# 统计代码行数
# import getCodeLine

# 分析html
# import getHtml

# 生成字母验证码图片
# import generateCodeImg

# 敏感文字
# import filterWord

# txt excel相互转换
# import txt2Excel

# 声音控制