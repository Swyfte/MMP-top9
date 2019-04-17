import csv

def csvWriteRow(filename, data):
	with open((filename + ".csv"), mode="w") as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(data)

def csvReadRow(filename, row):
	with open((filename + ".csv")) as csv_file:
		data = [row for row in csv.reader(csv_file, delimiter=',')]
	return data[row]

def csvWrite(filename, data):
	with open((filename + ".csv"), mode="w") as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerows(data)

def csvRead(filename):
	with open((filename + ".csv")) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line = 0
		for row in csv_reader:
			if line == 0:
				print(f"Columns:{', '.join(row)}")
				line += 1
			else:
				print(f"\t{', '.join(row)}")

testData1 = [
	["Title1","Title2","Title3"],
	[13,"Word1",True],
	[65,"Word2",False],
	[91,"Word3",True],
	[22,"Word4",False],
	[1,"Word5",True],
	[767,"Word6",False],
]

testData2 = [
	["Title1","Title2"],
	[13,"Word1"],
	[65,"Word2"],
	[91,"Word3"],
	[22,"Word4"],
	[1,"Word5"],
	[767,"Word6"],
]

csvWrite("Test1",testData1)
csvWrite("Test2",testData2)

csvWriteRow("Test3",testData1[3])
csvWriteRow("Test4", testData2[6])
