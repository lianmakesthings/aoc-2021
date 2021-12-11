from main import first, second

def test_first():
  assert first("test.txt") == 1656

def test_second():
  assert second("test.txt") == 195
