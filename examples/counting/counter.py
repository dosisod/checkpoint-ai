from checkpoint_ai import CheckpointAlgo, Checkpoint
from random import randint

class CounterCheckpoint(Checkpoint):
	def __init__(self):
		self.start=self.counter=0

	def run(self):
		#add either -1, 0, or 1 to counter
		self.counter+=randint(-1, 1)

		if self.counter>5:
			print(len(self.diffs))
			self.done=True

		return self.counter

if __name__=="__main__":
	cp=CounterCheckpoint()

	algo=CheckpointAlgo([cp])
	algo()
