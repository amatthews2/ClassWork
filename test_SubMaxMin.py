@pytest.mark.parametrize("num1, num2, output, expected", [
	(4, 1, 3, True),
    (4, 2, 2, True),
    (5, 2, 2, False)
])

def test_subtract_num(num1, num2, output, expected):
    from SubMaxMin.py import subtract_num
	sub_result = num1 - num2
    assert sub_result == expected