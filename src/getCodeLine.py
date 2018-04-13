import os


target = '/Users/fox/gitRepository/redis/src'

ext = ('.js')

def foo(fatherPath):
    res = 0
    files = os.listdir(fatherPath)
    for file in files:
        curPath = os.path.join(fatherPath, file)
        if os.path.isfile(curPath):
            if os.path.splitext(curPath)[1] in ext and bool(
                    os.path.splitext(curPath)[1]):
                with open(curPath, 'r') as f:
                    res += len(f.readlines())
            
        elif os.path.isdir(curPath):
            res += foo(curPath)
        else:
            print('非目标')
    return res


print(foo(target))