from checkpoint_ai import CheckpointAlgo, Checkpoint
from random import randint

class CounterCheckpoint(Checkpoint):
	def __init__(self):
		self.start=self.counter=0

	def run(self):
		print(self.counter)

		#add either -1, 0, or 1 to counter
		self.counter+=randint(-1, 1)

		if self.counter>5:
			self.done=True

if __name__=="__main__":
	cp=CounterCheckpoint()

	algo=CheckpointAlgo([cp])
	algo()
