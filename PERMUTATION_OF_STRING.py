cll=[]
def tostring(lista):
	return ''.join(lista)


def permute(a, l, r):
	if l==r:
		cll.append(tostring(a))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack


string = "chef"
n = len(string)
a = list(string)
permute(a, 0, n-1)

print(cll)
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
