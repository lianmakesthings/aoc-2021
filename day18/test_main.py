from main import first, explode

def test_explode_a():
  assert explode("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"

def test_explode_b():
  assert explode("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]"

def test_explode_c():
  assert explode("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]"

def test_explode_d():
  assert explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"