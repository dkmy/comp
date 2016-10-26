from collections import Counter

def swapchars(a):

	a = list(a)

	most_common = Counter(a).most_common()[0][0]
	least_common = Counter(a).most_common()[-1][0]
	most_common_indices = [i for i in range(len(a)) if a[i] == most_common]
	least_common_indices = [i for i in range(len(a)) if a[i] == least_common]
	for indices in most_common_indices:
		a[indices] = least_common

	for indices in least_common_indices:
		a[indices] = most_common

	return "".join(a)

