"""
Двоичное дерево поиска
В заданном двоичном дереве поиска с дубликатами найдите все наиболее часто встречающиеся элементы.
Считайте, что двоичное дерево поиска определено следующим образом:

    Левое поддерево узла состоит только из узлов с ключами, меньшими либо равными ключу данного узла.
    Правое поддерево узла состоит только из узлов с ключами, большими либо равными ключу данного узла.
    Левое поддерево и правое поддерево также являются двоичными деревьями поиска.

Примечание: в случае, если наиболее часто встречающихся элементов более одного, их можно возвращать в любом порядке. 
"""

class Node() :
	def __init__(self) :
		self.val = int()

	def giveValue(self,val, n1, n2):
		self.val = val
		self.right = n1
		self.left = n2




def foundTheCommon(lst, node): # lst - list of numbers for each value,  so it means we need to know the high of the tree to build a list or dynamicly  expand it
	if (lst[node.val] is None):
		lst[node.val] = 1
	else:
             	lst[node.val] +=1
             	if (node.left  is not None): 
             		foundTheCommon(lst, node.left)
             	if (node.right  is not None): 
             		foundTheCommon(lst, node.right)




	



