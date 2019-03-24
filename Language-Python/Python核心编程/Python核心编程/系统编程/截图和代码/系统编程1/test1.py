import pdb

def getAverage(a, b):
	result = a+b
	print("result=%d"%result)
	return result

a = 100
b = 200
c = a+b
pdb.set_trace()
ret = getAverage(a, b)
print(ret)