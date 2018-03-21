'''Return the square root of c.'''
def sqrt(c):
	if c < 0:
		return
	err = 1e-15
	t = c
	while abs(t**2 - c) > err:
		t = (t + c/t)/2
	return t

if __name__ == '__main__':
	print(sqrt(-1))
