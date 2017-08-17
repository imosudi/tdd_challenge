filename = "port-harcourt-weather.txt"

def weatherReport():
	with open(filename) as file:
		dayList = []
		dailyTempSpread = []
		file.next()
		file.next()
		for line in file:
			line.strip()
			splitted_line = line.split()
			try:
				dayListNum = int(splitted_line[0])
				dailyHigh = int(splitted_line[1])
				dailyLow = int(splitted_line[2])
			except ValueError:
				pass
			dailyTempSpread.append(dailyHigh - dailyLow)
			dayList.append(dayListNum)

	weatherDict = dict(zip(dayList, dailyTempSpread))
	print weatherDict
	print min(sorted(weatherDict, values=weatherDict.get))
	return dayList, dailyTempSpread, weatherDict


weatherReport()
	