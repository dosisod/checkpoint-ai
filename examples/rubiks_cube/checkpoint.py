import os

class checkpoint:
	def __init__(self, data, limit, minimum):
		""" init params
		data     Relevant checkpoint data
		limit    Run no more then N times
		minimum  Run at least N times
		"""

		self.data=data
		self.limit=limit
		self.minimum=minimum

		self.done=False #whether or not ML is done

		self.good=[] #successful attempts stored here
		self.bad=[] #unsuccessful attempts stored here

		self.pattern=None

	def pattern(self, test):
		pass

class checkpointML():
	def __init__(self, obj):
		self.obj=obj