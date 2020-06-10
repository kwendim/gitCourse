#This is a template for the grader

from onpit import Grader
from os.path import join

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "git clone https://github.com/kwendim/IntroductionToOs.git" or inputCommand == "git clone https://github.com/kwendim/IntroductionToOs":
			return True

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		pass

	@Grader.addStep(name='step3')
	def step3(self, workingDir, inputCommand):
		pass

