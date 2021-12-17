from main import first, second

def test_first_a():
  assert first("test-a.txt") == 16

def test_first_b():
  assert first("test-b.txt") == 12

def test_first_c():
  assert first("test-c.txt") == 23

def test_first_d():
  assert first("test-d.txt") == 31

def test_second_a():
  assert second("test-e.txt") == 3

def test_second_b():
  assert second("test-f.txt") == 54

def test_second_c():
  assert second("test-g.txt") == 7

def test_second_d():
  assert second("test-h.txt") == 9

def test_second_e():
  assert second("test-i.txt") == 1

def test_second_f():
  assert second("test-j.txt") == 0

def test_second_g():
  assert second("test-k.txt") == 0

def test_second_h():
  assert second("test-l.txt") == 1
