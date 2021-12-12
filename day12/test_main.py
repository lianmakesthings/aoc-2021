from main import first, second

def test_first_a():
  assert first("test-a.txt") == 10

def test_first_b():
  assert first("test-b.txt") == 19

def test_first_c():
  assert first("test-c.txt") == 226

def test_second_a():
  assert second("test-a.txt") == 36

def test_second_b():
  assert second("test-b.txt") == 103

def test_second_c():
  assert second("test-c.txt") == 3509