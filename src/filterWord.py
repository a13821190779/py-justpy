import os

txtPath = os.path.join(os.path.abspath('.'), 'filtered_word.txt')

with open(txtPath) as f:
	arr = f.read().split('\n')
	
def judgeIfIn(str):
	condition = False
	for item in arr:
		if item in str:
			print(str.replace(item, '**'))
			condition = not condition
			break
	print(condition)
	


judgeIfIn('北京欢迎您')
