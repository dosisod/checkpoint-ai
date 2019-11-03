class CheckpointAlgo():
	def __init__(self, points):
		self.checkpoints=points

	def __call__(self):
		for cp in self.checkpoints:
			iter=0
			while True:
				#run checkpoint if max iter has not been reached and checkpoint is not completed
				if (iter<cp.max or cp.max==-1) and not cp.done:
					cp()
				else:
					break

				#add to iterations if max is not infinite
				if cp.max!=-1:
					iter+=1