from collections import Counter, defaultdict
import heapq
import csv

def swapchars(a):
	return a.replace(Counter(a).most_common()[0][0], Counter(a).most_common()[-1][0])

def sortcat(*args):
	return "".join(heapq.nlargest(args[0], args[1:]))

def bluesclues(abbrev):	
	# columns = defaultdict(list)
	# path = 'states.txt'
	# with open(path) as f:
	#     reader = csv.reader(f)
	#     reader.next()
	#     for row in reader:
	#         for (i,v) in enumerate(row):
	#             columns[i].append(v)

 #   	state_dict = {}

 #   	for i in range(len(columns[0])):
 #   		state_dict[columns[1][i]] = columns[0][i]

 #   	return state_dict[abbrev]
 	(lambda __g, __y: [None for __g['bluesclues'], bluesclues.__name__ in [(lambda abbrev: (lambda __l: [[[[(lambda __items, __after, __sentinel: __y(lambda __this: lambda: (lambda __i: [[__this() for __l['state_dict'][__l['columns'][1][__l['i']]] in [(__l['columns'][0][__l['i']])]][0] for __l['i'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(len(__l['columns'][0]))), lambda: __l['state_dict'][__l['abbrev']], []) for __l['state_dict'] in [({})]][0] for __l['path'] in [('states.txt')]][0] for __l['columns'] in [(defaultdict(list))]][0] for __l['abbrev'] in [(abbrev)]][0])({}), 'bluesclues')]][0])(globals(), (lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))))


def bluesbooze(name):
	columns = defaultdict(list)
	path = 'states.txt'
	with open(path) as f:
	    reader = csv.reader(f)
	    reader.next()
	    for row in reader:
	        for (i,v) in enumerate(row):
	            columns[i].append(v)

   	state_dict = {}

   	for i in range(len(columns[0])):
   		state_dict[columns[0][i]] = columns[1][i]

   	return state_dict[name]