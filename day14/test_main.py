from main import first

def test_first():
  assert first("test.txt", 10) == 1588

def test_second():
  assert first("test.txt", 40) == 2188189693529