"""
У Маши есть список ее любимых фильмов, но они хранятся в необычной структуре — списке списков, 
которые могут иметь произвольную вложенность.
Она хочет преобразовать их в простой плоский список. 
Dealing with nested lists like ["a", ["b", "c", ["d"], "e"]]
result of algorithm should be ["a", "b", "c", "d", "e"].
"""																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																
def extractList(lst):
	for item in lst:
		print(item, " ", isinstance(item,list))
		if isinstance(item, list):
			extractList(item)
		else:
		    resultList.append(item)	



resultList = list()
tempList = ['A','B',['C','D',['E'],'F']]
tempList1 =['A',['B']]
extractList(tempList)
print(resultList)
