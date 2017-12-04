import numpy as np
import math
import sys




def merge(A, B):

	L = A
	R = B
	L = np.append(L, np.inf)
	R = np.append(R, np.inf)
	i = j = 0
	merged = list(A) + list(B)
	for k in range(0, np.size(merged)):
		if (L[i] > R[j]):
			merged[k] = R[j]
			j = j+1
		else:
			merged[k] = L[i]
			i = i+1
	return np.array(merged)





def mergesort(A):

	if (np.size(A) == 1):
		return A[0:1]
	q = int(np.floor(np.size(A)/2))
	a1 = A[0:q]
	a2 = A[q:]
	a1_ordered = mergesort(a1)
	a2_ordered = mergesort(a2)
	a_ordered = merge(a1_ordered, a2_ordered)
	return a_ordered




def main():
	A = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
	A1 = np.array([-2, -7, -1, -10, -12, -4, -5])
	A2 = -A1
	A3 = np.array([-2, -3, 4,-1,-2,1,5,-3])
	A4 = np.array([2, 1])

	arr = A1
	print arr
	sorted_array = mergesort(arr)#, 0, np.size(A4)-1)
	print sorted_array
	


if __name__ == '__main__':
	main()
