class Checkpoint:
	""" self params
	start    stores initial data of checkpoint
	done     stores whether checkpoint has been completed
	diffs    state of each iteration between checkpoint init and completion
	max      maximum number of iterations before termination
	         when max is -1, max is infinite
	"""

	start=None
	done=False
	diffs=[]
	max=-1

	def run(self): #override action to be ran for the checkpoint
		pass

	def __call__(self): #calling instance will run self.run()
		self.diffs.append(self.run())