filename = "port-harcourt-weather.txt"

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
			#print int(splitted_line[0])
		except ValueError:
			pass
		dailyTempSpread.append(dailyHigh - dailyLow)
		dayList.append(dayListNum)
	#print len(dayList)
	#print len(dailyTempSpread)

weatherDict = dict(zip(dayList, dailyTempSpread))
print weatherDict


	