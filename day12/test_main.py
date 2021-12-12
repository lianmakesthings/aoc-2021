from main import first

def test_first_a():
  assert first("test-a.txt") == 10

def test_first_b():
  assert first("test-b.txt") == 19

def test_first_c():
  assert first("test-c.txt") == 226
