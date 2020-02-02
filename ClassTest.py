def line_create(coords, x):
	x1 = coords[0][0]
	y1 = coords[0][1]
	x2 = coords[1][0]
	y2 = coords[1][1]
	m = (y2 - y1) / (x2 - x1)
	y = m * (x - x1) + y1
	return y
	
	
coords = ((-10, 10), (10, 10))
x = 15
y = line_create(coords, x)
print(y)
