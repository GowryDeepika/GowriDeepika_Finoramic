class Solution:
	def threeSumClosest(self, A, B):
		closetSum = sum(A)
		for i in range(len(A)) :
			for j in range(i + 1, len(A)):
				for k in range(j + 1, len(A)):
					if abs(B - closetSum) > abs(B - (A[i] + A[j] + A[k])):
						closetSum = A[i] + A[j] + A[k]

	    return closetSum