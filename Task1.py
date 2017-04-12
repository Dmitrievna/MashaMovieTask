"""
Название фильма
Маша хочет иметь возможность "испортить" название фильма. 
Она придумала такой алгоритм. 
Все буквы в названии фильма надо отсортировать по частоте их встречаемости (начиная с самых частых).
Например, название "Arrival" превратится в "rrAival" (возможно и "rrlAiva", и другие варианты), 
потому что буква "r" встречается два раза, а остальные один раз. 
Algorithm for scrambling letters in a movie title: from the most popular to the least popular
"""
inputName = list(input())
numberForEach = list()
setOfLetters = set(inputName)
for letter in setOfLetters:
	numberForEach.append(letter*inputName.count(letter))
numberForEach.sort(key=len, reverse=True)
print(*numberForEach, sep='')

