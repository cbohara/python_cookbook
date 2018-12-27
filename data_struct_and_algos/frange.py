"""
generator only runs in response to iteration
generator function only runs in response to “next” operations carried out in iteration
"""
def frange(start, stop, increment):
	x = start
	while x <= stop:
		yield x
		x += increment

for n in frange(0.0, 5.0, 0.5):
	print(n)

print(list(frange(0.0, 5.0, 0.5)))
