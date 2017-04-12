import random
"""
Маша хочет создать каталог своих любимых фильмов. 
В этом каталоге ей нужны операции добавления и удаления фильма.
Еще она хочет получать название случайного фильма (с равномерным распределением) из каталога. 
При этом все методы должны работать быстро — в среднем за O(1). 

List of favourite movies with O(1) functions
"""
class FavouriteMovies(object):
	def __init__(self):
		self.titles = {} # connection title - index
		self.indexes = {} # connection index- title
		self.len = 0
		self.nextIndex = 0 # index of the next item in collections

	def __len__(self):
	    return self.len

	def add(self, title):
	    if (title in self.titles): # check if movie is already there
	        return False
	    else:
	        self.titles[title] = self.nextIndex
	        self.indexes[self.nextIndex] = title
	        self.len += 1
	        self.nextIndex += 1
	        return True

	def delete(self, title):
		try:
			index = self.titles[title]
			del self.titles[title]
			del self.indexes[index]
			self.len -= 1
			if (index != self.nextIndex - 1):                                                 # swap for proper search in randomChoice
				buf = self.indexes[self.nextIndex -1]
				self.titles[buf] = index
				self.indexes[index] = self.indexes[self.nextIndex -1]
				del self.titles[buf]
				del self.indexes[self.nextIndex -1]
				
			self.nextIndex -=1
			    	
			return True
		except KeyError:
		    return False	

	def randomChoice(self):    #choose random movie                                 
	    if (self.len == 0):
	        raise KeyError
	    else:
	    	randIndex = random.randint(0, self.len - 1)
	    	return self.indexes[randIndex]


	def printList(self):
		print("titles: ", self.titles)
		print("indexes: ", self.indexes)






