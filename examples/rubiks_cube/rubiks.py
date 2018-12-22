import checkpoint
import math #used for .copysign()

""" faces affected by turning
W Y G B R O: U
    . . . .

W Y G B R O: D
    . . . .
    
W Y G B R O: L
. .     . .

W Y G B R O: R
. .     . .

W Y G B R O: F
. . . .

W Y G B R O: B
. . . .
"""

class cube:
	def __init__(self):
		#cube is orientated with white up, and red facing user
		self.cubes=[]
		self.faces="W","Y","G","B","R","O"

		for index, name in enumerate(self.faces):
			self.cubes.append([[[name]*3]*3]) #makes 3 rows of 3 columns (one face)

	def rotate(self, move): #pass a move like "U2" or "F"
		move=move.upper()
		rotation=self.parse(move)

		#these 3 if's only rotate adjecent sides, not face
		if (move[0]=="U" or move[0]=="D"):
			for i in a:
				self.cubes

	def parse(self, move): #parse between n2, n, and n'
		move=move[1:] #removes trailing character

		#would make this many lines but this seems more readable
		return (1 if move=="" else 2 if move=="2" else -1 if move=="'" else 0)

	def convert(self, move): #gets rotation and inverts it depending on face
		move=move[1:]
		rotation=self.parse(move)

		if move=="D" or move=="R" or move=="B":
			return int(math.copysign(rotation,-1)) #flips rotation
		else:
			return rotation

	def slice(self, index): #returns a slice (array) of the data that needs rotating
		pass

	def relative(self, parent, child): #find where child is relative to parent
		pass
