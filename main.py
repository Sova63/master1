from Sensor import Sensor
if __name__ =="__main__":
	sensors = []
	while True:
		chose = input("Добавить сенсор, посмотреть данные с добавленных сенсоров").lower().strip()
		if chose == "добавить":
			name = input("Введите модель сенсора")
			frashRate = input("Введите частоту опроса(1 по умолчанию)")
			if frashRate.isdigit():
				sensors.append(Sensor(name,int(frashRate)))
			else:
				sensors.append(Sensor(name))
		elif chose == "посмотреть":
			for sensor in sensors:
				sensor.Connect()
				print(sensor.GetData())



