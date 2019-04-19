import csv

def csvWriteRow(filename, data):
	with open((filename + ".csv"), mode="a", newline="") as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(data)

def csvWrite(filename, data):
	with open((filename + ".csv"), mode="w", newline="") as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerows(data)

def csvReadRow(filename, row):
	with open((filename + ".csv")) as csv_file:
		data = list(csv.reader(csv_file, delimiter=','))
		if row > len(data):
			return ["No data, out of range"]
		else:
			return data[row]

def csvRead(filename):
	with open((filename + ".csv")) as csv_file:
		data = list(csv.reader(csv_file, delimiter=','))
		return data

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

"""print("Test writing")
csvWrite("Test1",testData1)
csvWrite("Test2",testData2)

print("Test writing one row to a csv")
csvWriteRow("Test3",testData1[3])
csvWriteRow("Test3", testData2[6])

print("Test reading table")
print(csvRead("Test1"))
print("Test reading one line table")
print(csvRead("Test3"))
print("Test reading one row")
print(csvReadRow("Test1",3))
print("Test out of limits row")
print(csvReadRow("Test2",10))"""