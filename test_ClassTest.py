def test_ClassTest():
	from ClassTest import line_create
	coords = [(-10, 10), (10, 10)]
	x = 15
	answerY = line_create(coords, x)
	y = 10
	assert answerY == y