import time
import random
class Sensor:
	def __init__(self,model,freshRate=1):
		self._model = model
		self._freshRate = freshRate
	def Connect(self):
		print(f"{self._model} подключен")
	def GetData(self):
		time.sleep(self._freshRate)
		return  random.randint(1,16)
	def SubscribeSensor(self,watchTime):
		while watchTime > 0:
			time.sleep(1)
			print(self.GetData())
			watchTime -=1