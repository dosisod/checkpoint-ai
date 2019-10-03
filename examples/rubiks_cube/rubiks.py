from colorama import Back
import math

from checkpoint_ai import CheckpointAlgo, Checkpoint

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

class Cube:
	def __init__(self):
		#cube is orientated with white up, and red facing user
		self.faces=[]

		#id and color table:
		self.colors=(
			Back.WHITE,   #0
			Back.GREEN,   #1
			Back.RED,     #2
			Back.BLUE,    #3
			Back.MAGENTA, #4  #orange cannot be printed (by default), use magenta instead
			Back.YELLOW   #5
		)

		#for index, name in enumerate(self.faces):
		for index in range(6):
			self.faces.append([[index]*3]*3) #makes 3 rows of 3 columns (one face)

	def rotate(self, move): #pass a move like "U2" or "F"
		move=move.upper()
		rotation=self.parse(move)

		#tbd

	def parse(self, move): #parse between n2, n, and n'
		move=move[1:] #removes trailing character

		if move=="":
			return 1 #CW turn
		elif move=="2":
			return 2 #2x turn
		elif move=="'":
			return -1 #CCW turn
		return 0

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

	def display(self): #print the current state of the cube out
		rows=[] #stores faces to be drawn

		rows+=self.faces[0] #add each white layer

		for row in range(3):
			for face in range(4):
				rows.append(self.faces[face+1][row])

		rows+=self.faces[5] #add each yellow layer

		for index, row in enumerate(rows):
			ii=index//3
			if ii==0 or ii==5:
				print("   ", end="")

			for pindex, piece in enumerate(row):
				print(self.colors[piece]+" "+Back.RESET, end="")

			if ii==0 or ii==5 or (ii!=0 and ii!=5 and index%4==2):
				print("")

if __name__=="__main__":
	AI=CheckpointAlgo([])
	
	cube=Cube()
	cube.display()
