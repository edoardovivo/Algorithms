 # Implementation of the Kadane's algorithm for the maximum subarray problem.
 # This also keeps track of the start and end indices of the maximal subarray

# For each i, we find the maximum subarray value ending at i, called B_i (max_ending_here)
# by computing max(A[i], B_{i-1} + A[i]).
# The maximum subarray value is max(B_1, B_2, ..., B_n) and we keep track of that with the variable max_so_far.
# In order to get the indices of the actual maximal subarray, we keep track of the choices:
# 	If max(A[i], B_{i-1} + A[i]) is A[i], this means that a new CANDIDATE for maximal subarray starts at i.
# 		If the candidate turns out to be the actual maximal subarray, then we set the start index also to i.
# 	If max(A[i], B_{i-1} + A[i]) is equal to B_{i-1} + A[i], then we are appending the last value to the subarray, 
# 	therefore we simply add 1 to the final index of the candidate maximal subarray.

import numpy as np


def find_max_subarray(A):
	max_ending_here = max_so_far = A[0]
	start = end = 0
	startaux = endaux = 0

	for i in range(1, len(A)):
		x = A[i]
		print("i: {}".format(i))
		print("max ending here: {}".format(max_ending_here))
		# This condition is equivalent to x > B_{i-1} + x. In this case, we have a new candidate maximal 
		# subarray starting at i. We set auxiliary start and end variables to i, and update max_ending_here.
		if (max_ending_here < 0):
			startaux = endaux = i
			max_ending_here = x
			print "startaux: {}, endaux: {}".format(startaux, endaux)
		else:
			# In this case, we append the last value to the candidate maximal subarray, so we update the end auxiliary variable
			# and max_ending_here
			endaux = endaux + 1
			max_ending_here = max_ending_here + x
			print "startaux: {}, endaux: {}".format(startaux, endaux)
		#max_ending_here = max(x, max_ending_here + x)

		#If the new candidate is better than the last candidate, we update the start and end indices,
		#as well as the variable max_so_far, which holds the value of the maximal subarray.
		if (max_so_far < max_ending_here):
			start = startaux
			end = endaux
			max_so_far = max_ending_here
		print "start: {}, end: {}".format(start, end)
		print "\n"
		#max_so_far = max(max_so_far, max_ending_here)
	return (max_so_far, start, end)




def main():
	A = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
	A1 = np.array([-2, -7, -1, -10, -12, -4, -5])
	A2 = -A1
	A3 = np.array([-2, -3, 4,-1,-2,1,5,-3])
	print A1
	msubval = find_max_subarray(A1)
	print msubval
	


if __name__ == '__main__':
	main()
