def subsets(arr):
	if arr == []:
            return []
	result = []
	arr = sorted(arr)
	def CAA(A, i):
		if (i == len(arr)-1):
			result.append(A)
			result.append(A + [arr[i]])
			return
		CAA(A, i + 1)
		CAA(A + [arr[i]], i + 1)
	CAA([], 0)
	return sorted(result)

print subsets([ 15, 20, 12, 19, 4 ])