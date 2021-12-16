from main import first

def test_first_a():
  assert first("test-a.txt") == 16

def test_first_b():
  assert first("test-b.txt") == 23

def test_first_c():
  assert first("test-c.txt") == 31