import checkpoint
import rubiks

def main():
	ML=checkpoint.checkpointML([])
	
	QB=rubiks.cube()
	print(QB.cubes)

if __name__=="__main__":
	main()