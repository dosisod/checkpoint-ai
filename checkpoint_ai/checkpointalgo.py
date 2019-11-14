class CheckpointAlgo():
	def __init__(self, points):
		self.checkpoints=points

	def __call__(self):
		for cp in self.checkpoints:
			#send the checkpoint to the handler
			self.dispatch(cp)

	def dispatch(self, cp):
		#stores how many iterations each checkpoint has done
		iter=0

		while True:
			#if able to iterate, and checkpoint is not done, keep running
			if (iter<cp.max or cp.max==-1) and not cp.done:
				cp()

			else:
				break

			#add to iterations if max is not infinite
			if cp.max!=-1:
				iter+=1