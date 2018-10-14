#coding: utf-8

#filter函数。此时lambda函数用于指定过滤列表元素的条件。
#例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来.
li = [i for i in xrange(1, 10)]
print filter(lambda x:x%3 == 0, li)
#Result:[3, 6, 9]

#sorted函数。
#此时lambda函数用于指定对列表中所有元素进行排序的准则。sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序。
print sorted(li, key=lambda x:abs(5-x))
#Results:[5, 4, 6, 3, 7, 2, 8, 1, 9]

#map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。
print map(lambda x:x*x, li)
#Results: [1, 4, 9, 16, 25, 36, 49, 64, 81]

#reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。
print reduce(lambda a, b: '{}+{}'.format(a, b), li)
#Results:1+2+3+4+5+6+7+8+9
