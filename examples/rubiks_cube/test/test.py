from ..rubiks import Cube

#this test file will eventually use pytest

class Test:
	def __init__(self):
		self.cube=Cube()

	def test_parse(self):
		assert self.cube.parse("U2") == self.cube.parse("u2") == 2
		assert self.cube.parse("D") == self.cube.parse("d") == 1
		assert self.cube.parse("L'") == self.cube.parse("l'") == -1
		assert self.cube.parse("R2") == self.cube.parse("r2") == 2
		assert self.cube.parse("F") == self.cube.parse("f") == 1
		assert self.cube.parse("B'") == self.cube.parse("b'") == -1

if __name__=="__main__":
	tester=Test()

	tester.test_parse()

	print("All tests passed")
