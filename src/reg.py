import re
email = '945039036@qq.com'

res = re.match('(\d+)(@.+)(\.\w+)', email)

index = 0
try: 
	while True:
		print(res.group(index))
		index += 1
except BaseException as e:
	print(e)